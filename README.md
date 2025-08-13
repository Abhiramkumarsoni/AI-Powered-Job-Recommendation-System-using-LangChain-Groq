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

![App Screenshot](screenshot.png)  
*Replace with a real screenshot of your app.*

---

## 📦 Installation
2️⃣ Install dependencies

pip install -r requirements.txt

---
🔑 API Keys
You will need two API keys to run this project:

Groq API Key

Serper API Key 

Both keys can be entered directly in the Streamlit sidebar when running the app.

---

▶️ Usage

Run the Streamlit app:

streamlit run app.py
Steps:

Enter your Groq API Key and Serper API Key in the left sidebar.

Upload your resume PDF.

Click "Show Extracted Skills".

View:

Predicted job title

Top matching job links

AI-generated reasons why each job is suitable

---


📂 Project Structure

📦 ai-resume-job-finder

 ┣ 📜 app.py     
 ┣ 📜 check.py
 ┣ 📜 requirements.txt  
 ┣ 📜 README.md       


 ---
⚙️ Tech Stack
  Python 3.9+

Streamlit – UI framework

LangChain – LLM pipeline

Groq LLM – AI for skill & job title extraction

Serper API – Job search from LinkedIn & Indeed

HuggingFace – Embeddings & text processing

---
📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Groq – High-speed LLM APIs

Serper.dev – Job search integration

Streamlit – Simple & beautiful UI framework


