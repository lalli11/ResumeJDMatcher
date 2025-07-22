# ResumeJDMatcher
A tool that intelligently matches resumes with job descriptions, highlighting key skills and experiences
ResumeJDMatcher Description
This is a Resume Matcher Web App built using Python and Streamlit. It automatically analyzes how well a candidate’s resume matches a job description (JD) by extracting and comparing the textual content of both PDF files. The system uses TF-IDF and cosine similarity to calculate a match score and highlights matched and missing keywords.

⭐ Key Features
📄 Upload and analyze Resume and JD in PDF format

🤖 Automatic text extraction and cleaning

📊 Computes a match score between resume and JD using NLP

✅ Displays matched keywords (strengths)

⚠ Shows missing keywords (areas for improvement)

💡 Visual feedback based on score (success, warning, or error)

Tech Stack
Frontend/UI: Streamlit – for creating interactive web apps

Backend & ML/NLP:

scikit-learn – TF-IDF vectorization and cosine similarity

nltk – for stopwords removal

PyPDF2 – for extracting text from PDF files

re – regular expressions for text cleaning
🚀 How to Run:
pip install -r requirements.txt
streamlit run "ml.py"
