import pdfplumber 
def extract_text_from_pdf(file_path):
    text=""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

resume_path="resumes/main_sample-data-analyst-resume.pdf"
resume_text=extract_text_from_pdf(resume_path)
print(resume_text)

import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def preprocess(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z ]','',text)
    words=text.split()
    words=[word for word in words if word not in stopwords.words('english')]
    return " ".join(words)
cleaned_text=preprocess(resume_text)
print("\n\nCLEANED TEXT:\n")
print(cleaned_text)

job_description="""we are looking for a data analyst with skills in python, SQL, Data analysis,machine learning,and data visualization using tools like tableau"""
cleaned_job=preprocess(job_description)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
vectors=vectorizer.fit_transform([cleaned_text,cleaned_job])
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors[0],vectors[1])
score=similarity[0][0]*100
print("\nMATCH SCORE:",score)

resume_path="resumes/main_sample-data-analyst-resume.pdf"
resume_text=extract_text_from_pdf(resume_path)
print(resume_text)

import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def preprocess(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z ]','',text)
    words=text.split()
    words=[word for word in words if word not in stopwords.words('english')]
    return " ".join(words)
cleaned_text=preprocess(resume_text)
print("\n\nCLEANED TEXT:\n")
print(cleaned_text)

job_description="""we are looking for a data analyst with skills in python, SQL, Data analysis,machine learning,and data visualization using tools like tableau"""
cleaned_job=preprocess(job_description)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ngram_range=(1,2))
vectors=vectorizer.fit_transform([cleaned_text,cleaned_job])
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors[0],vectors[1])
score=similarity[0][0]*100
print("\nMATCH SCORE:",score)

skills_list = ["python", "sql", "machine learning", "data analysis", "tableau", "excel"]

def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

resume_skills = extract_skills(cleaned_text)
job_skills = extract_skills(cleaned_job)

print("\nRESUME SKILLS:", resume_skills)
print("JOB SKILLS:", job_skills)
missing_skills = list(set(job_skills) - set(resume_skills))
print("\nMISSING SKILLS:", missing_skills)
common_words = set(cleaned_text.split()).intersection(set(cleaned_job.split()))
print("\nMATCHED KEYWORDS:", list(common_words))

print("\nSUGGESTIONS:")

if missing_skills:
    print("- Add these skills to your resume:", ", ".join(missing_skills))

if score < 50:
    print("- Improve your resume by adding relevant projects and experience")

if score > 70:
    print("- Your resume is a strong match!")