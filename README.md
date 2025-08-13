# 📄 AI Resume to Job Finder

An AI-powered **Streamlit** web app that:
- Extracts **skills** from your resume using **Groq LLM**.
- Predicts your **best-fit job title**.
- Searches for relevant jobs using **Serper API** (Google Search API).
- Explains **why each job is a good match** based on your skills.

---

## 🚀 Features

✅ Upload your **resume (PDF)**  
✅ **AI skill extraction** using `llama-3.1-8b-instant`  
✅ Automatic **job title prediction**  
✅ **Job search** from LinkedIn & Indeed via **Serper API**  
✅ AI-generated **reasons for suitability** for each job  
✅ Clean and **professional UI** built with Streamlit  

---

## 🖥️ Demo


## 📦 Installation

### 1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-resume-job-finder.git
cd ai-resume-job-finder
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 API Keys
You will need two API keys to run this project:

Groq API Key → Get here

Serper API Key → Get here

Both keys can be entered directly in the Streamlit sidebar when running the app.

▶️ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Steps:

Enter your Groq API Key and Serper API Key in the left sidebar.

Upload your resume PDF.

Click "Show Extracted Skills".

View:

Predicted job title

Top matching job links

AI-generated reasons why each job is suitable

📂 Project Structure
bash
Copy
Edit
📦 ai-resume-job-finder
 ┣ 📜 app.py            # Main Streamlit application
 ┣ 📜 requirements.txt  # Python dependencies
 ┣ 📜 README.md         # Project documentation
 ┣ 📂 screenshots       # Screenshots for README
⚙️ Tech Stack
Python 3.9+

Streamlit – UI framework

LangChain – LLM pipeline

Groq LLM – AI for skill & job title extraction

Serper API – Job search from LinkedIn & Indeed

HuggingFace – Embeddings & text processing

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Groq – High-speed LLM APIs

Serper.dev – Job search integration

Streamlit – Simple & beautiful UI framework

yaml
Copy
Edit

---

This version has:
- Proper blank lines so GitHub renders sections cleanly.
- Emoji aligned with text.
- Code blocks fenced correctly.
- Consistent heading sizes.

If you want, I can also **add badges** (Python, Streamlit, License, Stars) to the top so it looks even more professional.  
That’ll make your README look like a polished open-source project.  

Do you want me to add those badges?
