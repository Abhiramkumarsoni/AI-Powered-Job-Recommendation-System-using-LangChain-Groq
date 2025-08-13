# 📄 AI Resume to Job Finder

An AI-powered Streamlit web app that:
- Extracts **skills** from your resume using **Groq LLM**.
- Predicts your **best-fit job title**.
- Searches for relevant jobs using **Serper API** (Google Search API).
- Explains **why each job is a good match** based on your skills.

---

## 🚀 Features
- ✅ Upload your **resume (PDF)**.
- ✅ **AI skill extraction** using `llama-3.1-8b-instant`.
- ✅ Automatic **job title prediction**.
- ✅ **Job search** from LinkedIn & Indeed via **Serper API**.
- ✅ AI-generated **reasons for suitability** for each job.
- ✅ Clean and **professional UI** built with Streamlit.

---

## 🖥️ Demo
![App Screenshot](screenshot.png)  
*(Add your app screenshot here)*

---

## 📦 Installation

1. **Clone the repository**
git clone https://github.com/yourusername/ai-resume-job-finder.git
cd ai-resume-job-finder
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
🔑 API Keys
You need two API keys to use this project:

Groq API Key → Get here

Serper API Key → Get here

▶️ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Then:

Enter your Groq API Key and Serper API Key in the sidebar.

Upload your resume PDF.

Click "Show Extracted Skills".

View predicted job title & top matching job links with AI reasoning.

📁 Project Structure
bash
Copy
Edit
📦 ai-resume-job-finder
 ┣ 📜 app.py            # Main Streamlit app
 ┣ 📜 requirements.txt  # Python dependencies
 ┣ 📜 README.md         # Documentation
 ┣ 📂 screenshots       # App images
⚙️ Tech Stack
Python

Streamlit – UI framework

LangChain – LLM integration

Groq LLM – AI skill & job title extraction

Serper API – Job search (LinkedIn, Indeed)

HuggingFace – Embedding & text processing

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Groq for their lightning-fast LLM API.

Serper.dev for job search API.

Streamlit for the easy-to-use UI.

yaml
Copy
Edit

---

If you want, I can also give you a **`requirements.txt`** file so your GitHub project is plug-and-play for anyone. That way they can just run `pip install -r requirements.txt` and start your app instantly.







You said:
what should be written in the description 


ChatGPT said:
For your GitHub repository description (the short text that appears under the repo name), you want something clear, concise, and keyword-rich so people instantly understand the project.

Here are a few good options you could use:

Option 1 (Simple & Clear)

AI-powered Streamlit app that extracts skills from resumes, predicts best-fit jobs, and finds matching job listings with AI reasoning.

Option 2 (More Keyword-Focused)

Resume analysis and job search tool using Groq LLM, LangChain, and Serper API — extract skills, predict job titles, and get AI-suggested job matches.

Option 3 (Catchy)

Upload your resume → Get AI-powered job title & skills → Instantly see matching jobs with reasons why you’re a great fit.

