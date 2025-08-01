import streamlit as st 
import google.generativeai as genai 
import os 
import PyPDF2 as pdf 
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
else:
    genai.configure(api_key=api_key)

# Gemini response
def get_gemini_response(input_text):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(input_text)
    return response.text 

# PDF reading
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Prompt template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage match based 
on the JD and list missing keywords with high accuracy.

resume: {text}
description: {jd}

I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 48px;
    }
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #333333 !important;
        font-size: 16px !important;
    }
    .stButton button {
        background-color: #1abc9c;
        color: white;
        font-size: 18px;
        padding: 0.5em 2em;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #16a085;
        color: #fff;
    }
    .result-box {
        background-color: #ecf0f1;
        border-radius: 10px;
        padding: 1em;
        font-size: 16px;
        white-space: pre-wrap;
        color: #2c3e50;
        border: 1px solid #bdc3c7;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Streamlit UI ----------
st.markdown("<h1>📄 Smart ATS Resume Evaluator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#7f8c8d;'>🚀 Boost your resume and get past the bots!</h4>", unsafe_allow_html=True)

jd = st.text_area("📌 Paste the Job Description here")
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type="pdf", help="Only PDF format is supported")

submit = st.button("🔥 Evaluate Resume")

if submit:
    if uploaded_file is not None and jd.strip() != "":
        text = input_pdf_text(uploaded_file)
        final_prompt = input_prompt.format(text=text, jd=jd)
        response = get_gemini_response(final_prompt)
        
        st.markdown("### ✅ ATS Evaluation Result")
        st.markdown(f'<div class="result-box">{response}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload a resume and paste a job description.")
