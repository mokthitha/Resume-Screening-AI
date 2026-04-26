# Resume-Screening-AI

📌 Project Description

This project is a Resume Screening AI that compares a candidate's resume with a given job description and calculates a match score using Natural Language Processing (NLP) techniques. It also identifies relevant skills, missing skills, and provides suggestions to improve the resume.

---

🚀 Features

- Extracts text from PDF resumes
- Cleans and preprocesses text using NLP
- Calculates match score using TF-IDF and cosine similarity
- Identifies skills present in the resume
- Detects missing skills based on job description
- Provides suggestions to improve resume quality

---

🛠️ Tech Stack

- Python
- scikit-learn
- NLTK
- pdfplumber

---

⚙️ How It Works

1. Load the resume PDF file
2. Extract text using pdfplumber
3. Preprocess text (lowercase, remove symbols, remove stopwords)
4. Convert text into numerical form using TF-IDF
5. Compute similarity using cosine similarity
6. Display:
   - Match Score
   - Resume Skills
   - Missing Skills
   - Suggestions

---

▶️ How to Run

pip install pdfplumber nltk scikit-learn
python app.py

---

📊 Sample Output

MATCH SCORE: 25.97%

RESUME SKILLS: ['python', 'sql']
JOB SKILLS: ['python', 'sql', 'machine learning', 'data analysis', 'tableau']

MISSING SKILLS: ['machine learning', 'data analysis', 'tableau']

SUGGESTIONS:
- Add these skills to your resume: machine learning, data analysis, tableau
- Improve your resume by adding relevant projects and experience

---

🔮 Future Improvements

- Use advanced NLP models like BERT for better accuracy
- Improve skill extraction using NLP techniques
- Build a user interface using Streamlit
- Support multiple resume comparison and ranking

---

📁 Project Structure

resume-screening-ai/
│── app.py
│── resumes/
│   └── sample_resume.pdf
│── README.md

---

💡 Conclusion

This project demonstrates how NLP techniques can be used to automate resume screening and help candidates improve their chances of getting shortlisted.

---
