# 🧠 ATS Resume Scorer using Gemini API

🚀 Built an AI-powered Applicant Tracking System that uses Google Gemini to evaluate PDF resumes against job descriptions. The system parses and analyzes resumes, and provides an automatic Accept/Reject decision with match score and suggestions — streamlining the recruitment process using GenAI.
---

## 🚀 Features

- ✅ Upload a resume (PDF format)
- 📄 Paste or type a Job Description (JD)
- 🤖 AI-generated suggestions to improve your resume
- 🔍 Displays missing keywords/skills from the JD
- 💡 Feedback box with summary & enhancement ideas
- 🎨 Clean, interactive UI built with Streamlit

---

## 🧠 How It Works

1. **Upload Resume:** The system reads and parses your resume from PDF.
2. **Paste Job Description:** The JD is analyzed for keywords and expected roles.
3. **Prompt Creation:** The resume + JD are used to generate a structured prompt.
4. **Gemini AI Call:** The prompt is sent to Gemini Pro via its API for scoring and suggestions.
5. **Suggestions:** AI-generated recommendations for missing skills/tools appear beside the chart.

---
