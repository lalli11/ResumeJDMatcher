import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import re
import PyPDF2

# Download stopwords (do only once)
nltk.download('stopwords')

# --- Function to extract text from uploaded PDF ---
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# --- Clean the extracted text ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# --- Calculate match score using TF-IDF & Cosine Similarity ---
def match_score(resume_text, jd_text):
    documents = [resume_text, jd_text]
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(documents)
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2), tfidf.get_feature_names_out(), vectors

# --- Compare matched and missing keywords ---
def get_keywords_difference(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    missing_keywords = jd_words - resume_words
    matched_keywords = resume_words & jd_words
    return list(matched_keywords), list(missing_keywords)

# --- Streamlit UI ---
st.set_page_config(page_title="PDF Resume Matcher", layout="centered")
st.title("📄 Resume & JD Matcher from PDF")
st.write("Upload your Resume and Job Description in PDF format. The system will show match score, strengths, and areas to improve.")

# --- File uploaders ---
resume_pdf = st.file_uploader("📄 Upload Resume PDF", type=["pdf"])
jd_pdf = st.file_uploader("📝 Upload Job Description PDF", type=["pdf"])

# --- On button click ---
if st.button("🔍 Match Now"):
    if resume_pdf and jd_pdf:
        resume_raw = extract_text_from_pdf(resume_pdf)
        jd_raw = extract_text_from_pdf(jd_pdf)

        resume_clean = clean_text(resume_raw)
        jd_clean = clean_text(jd_raw)

        score, _, _ = match_score(resume_clean, jd_clean)
        matched, missing = get_keywords_difference(resume_clean, jd_clean)

        st.success(f"✅ Match Score: {score}%")

        if score >= 70:
            st.info("Great Match! 🚀 You're close to the job requirements.")
        elif score >= 50:
            st.warning("Average Match. You might need to tailor your resume.")
        else:
            st.error("Low Match. Consider revising your resume.")

        st.subheader("✅ Strengths (Matched Keywords)")
        st.write(", ".join(matched))

        st.subheader("⚠ Improvements Needed (Missing Keywords)")
        st.write(", ".join(missing))
    else:
        st.error("❌ Please upload both Resume and JD PDF files.")