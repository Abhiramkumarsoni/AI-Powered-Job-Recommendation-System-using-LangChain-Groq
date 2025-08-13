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
<img width="1912" height="951" alt="Screenshot 2025-08-13 213341" src="https://github.com/user-attachments/assets/2b18bed3-cf41-4d9f-87da-f99c1d852005" />

<img width="1901" height="960" alt="Screenshot 2025-08-13 213414" src="https://github.com/user-attachments/assets/cd2c66a9-a023-4714-b65d-c7b0d30522ad" />

<img width="1896" height="957" alt="image" src="https://github.com/user-attachments/assets/75cb40b1-2072-4cff-8689-f05d5810594d" />




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


