# ResumeJDMatcherDescription
A tool that intelligently matches resumes with job descriptions, highlighting key skills and experiences.
This is a Resume Matcher Web App built using Python and Streamlit. It automatically analyzes how well a candidate’s resume matches a job description (JD) by extracting and comparing the textual content of both PDF files. The system uses TF-IDF and cosine similarity to calculate a match score and highlights matched and missing keywords.

## 🚀 Features
- Upload resume and job description PDFs.
- Extracts and cleans text using NLP techniques.
- Calculates match score using **TF-IDF** and **Cosine Similarity**.
- Displays:
  - ✅ Matched Keywords (your strengths)
  - ⚠ Missing Keywords (areas to improve)
- Score-based feedback: Great / Average / Low Match.
- Clean and interactive UI with **Streamlit**.
 
## 🧠 How It Works
1. Extract text from the uploaded PDF files using `PyPDF2`.
2. Clean the text by:
   - Lowercasing
   - Removing punctuation
   - Removing stopwords using `nltk`
3. Convert the text into vectors using `TfidfVectorizer`.
4. Calculate cosine similarity between resume and job description.
5. Output score and show keyword insights.

## 🛠 Tech Stack
| Tool        | Purpose                           |
|-------------|-----------------------------------|
| Python      | Core programming language         |
| Streamlit   | Web interface                     |
| scikit-learn| TF-IDF and cosine similarity      |
| nltk        | Stopwords removal                 |
| PyPDF2      | PDF text extraction               |
| re (regex)  | Text preprocessing                |

## ▶️ Running the App
pip install -r requirements.txt
streamlit run resume_job_matcher.py
