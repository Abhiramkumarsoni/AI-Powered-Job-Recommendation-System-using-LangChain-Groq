import streamlit as st
import re
import requests
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# ---- Page Config ----
st.set_page_config(page_title="AI Resume to Job Finder", page_icon="📄", layout="wide")

# ---- Sidebar for API Keys ----
st.sidebar.header("🔑 API Keys")
groq_api_key = st.sidebar.text_input("Enter Groq API Key", type="password")
serper_api_key = st.sidebar.text_input("Enter Serper API Key", type="password")
st.sidebar.markdown("---")
st.sidebar.info("Your API keys are used only for this session and are not stored.")

# ---- Helper functions ----
def clean_text(text):
    text = str(text).replace("\n", " ")
    text = " ".join(text.split())
    return text

def extract_skills_from_resume(llm, resume_text):
    response = llm.invoke(
        f"Based on this content {resume_text}, extract only the skills of the candidate "
        f"and give me clean output without any numbers, bullet points, or other symbols "
        f"except for commas between skills."
    )
    return clean_text(response.content if hasattr(response, 'content') else response)

def extract_job_title_with_regex(skills_text):
    match = re.search(r'\*\*(.*?)\*\*', skills_text)
    return match.group(1) if match else "Data Scientist"

def search_jobs_serper(job_title, api_key):
    search_query = f"{job_title} India, site:linkedin.com/jobs OR site:indeed.com"
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {"q": search_query}

    response = requests.post(url, headers=headers, json=payload)
    results_list = []

    if response.status_code == 200:
        results = response.json()
        if "organic" in results:
            for item in results["organic"][:5]:
                results_list.append({
                    "title": item.get("title"),
                    "link": item.get("link")
                })
    return results_list

def explain_job_match(llm, skills, job_title_from_link):
    prompt = (
        f"Candidate skills: {skills}\n"
        f"Job title: {job_title_from_link}\n\n"
        "Explain in 2-3 sentences why this job is suitable for the candidate "
        "based on their skills."
    )
    response = llm.invoke(prompt)
    return clean_text(response.content if hasattr(response, 'content') else response)

# ---- Main Page ----
st.title("📄 AI Resume to Job Finder")
st.markdown(
    "<p style='color: gray;'>Upload your resume and instantly find matching jobs with AI-powered skill extraction, job title prediction, and suitability reasoning.</p>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📤 Upload Resume PDF", type=["pdf"], help="Upload your resume in PDF format.")

if uploaded_file and groq_api_key and serper_api_key:
    # Save uploaded file temporarily
    temp_path = "temp_resume.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load and process PDF
    loader = PyPDFLoader(temp_path)
    docs = loader.load()
    docs = [clean_text(doc) for doc in docs]
    documents = [Document(page_content=doc) for doc in docs]

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    final_documents = text_splitter.split_documents(documents)
    full_resume_text = " ".join([doc.page_content for doc in final_documents])

    with st.expander("📄 Resume Text Preview", expanded=False):
        st.write(full_resume_text[:1000] + "...")


    # ---- Load LLM ----
    os.environ["GROQ_API_KEY"] = groq_api_key
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )


    # ---- Skill Extraction ----
    if st.button("🔍 Show Extracted Skills"):
        with st.spinner("Extracting skills from resume..."):
            skills = extract_skills_from_resume(llm, full_resume_text)
        st.success("✅ Skills extracted successfully!")
        st.markdown(f"**Skills:** {skills}")

        # ---- Job Title Extraction ----
        job_title = extract_job_title_with_regex(skills)
        st.markdown(f"**Predicted Job Title:** {job_title}")

        # ---- Search Jobs ----
        with st.spinner("Searching for jobs..."):
            job_results = search_jobs_serper(job_title, serper_api_key)

        # ---- Display Jobs with AI Reasoning ----
        if job_results:
            st.subheader("💼 Top Matching Job Links & AI Reasons")
            for job in job_results:
                st.markdown(f"**[{job['title']}]({job['link']})**")
                with st.spinner("Analyzing suitability..."):
                    reason = explain_job_match(llm, skills, job['title'])
                st.write(f"💡 {reason}")
        else:
            st.warning("No job results found.")
elif uploaded_file and (not groq_api_key or not serper_api_key):
    st.warning("Please enter both Groq and Serper API Keys in the sidebar to proceed.")
