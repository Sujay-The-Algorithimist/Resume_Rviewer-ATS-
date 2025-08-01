# 🧠 ATS Resume Scorer using Gemini API

This project is an intelligent Applicant Tracking System (ATS) built with Streamlit and Gemini Pro (Google's GenAI model). It allows users to upload resumes and get real-time scoring based on a Job Description (JD), along with AI-generated suggestions for improvement. It visually displays a pie chart showing the match percentage and lists missing skills, tools, or keywords.

---

## 🚀 Features

- ✅ Upload a resume (PDF format)
- 📄 Paste or type a Job Description (JD)
- 📊 See a colored pie chart showing JD-Resume match %
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
5. **Visualization:** A pie chart is displayed showing how closely your resume matches the JD.
6. **Suggestions:** AI-generated recommendations for missing skills/tools appear beside the chart.

---
