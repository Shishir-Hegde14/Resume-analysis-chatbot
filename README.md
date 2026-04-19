# Resume Analysis Chatbot with Gemini LLM

## Overview
This project is a Streamlit-based Resume Analysis Chatbot that allows users to upload a resume in PDF format, extract its content, generate a structured summary, and interact with an AI chatbot for further discussion and analysis.

The application uses Google Gemini to provide intelligent feedback on sections such as personal information, experience, skills, qualifications, and hobbies or interests.

---

## Features
- Upload resume in PDF format
- Extract text from uploaded PDF resumes
- Identify and organize common resume sections
- Generate a default structured resume analysis
- Chat interactively with an AI model about the resume
- Maintain conversation history during the session

---

## Tech Stack
- **Python**
- **Streamlit** – for the web interface
- **PyPDF2** – for PDF text extraction
- **Google Generative AI (Gemini)** – for AI-powered resume analysis
- **Regex (`re`)** – for section identification and parsing

---

## How It Works
1. The user uploads a resume PDF through the Streamlit interface.
2. The application extracts text from the PDF using `PyPDF2`.
3. The extracted text is split into sections like:
   - Personal Information
   - Experience
   - Skills
   - Qualifications
   - Hobbies / Interests
4. A default analysis summary is generated and displayed.
5. A Gemini chat session is started using that summary as initial context.
6. The user can ask follow-up questions about the resume.
7. The model responds based on the uploaded resume context.

---

## Project Structure
- `app.py` – main Streamlit application
- `key.txt` – stores the Gemini API key locally
- `requirements.txt` – Python dependencies

---

## Libraries Used
### Streamlit
Used to create the frontend interface for:
- file upload
- text display
- chat interaction
- session management

### PyPDF2
Used to:
- read uploaded PDF files
- extract text page by page

### google.generativeai
Used to:
- configure Gemini API access
- initialize the Gemini model
- create and manage a chat session
- generate AI-based responses

### re
Used to:
- detect section headings in resume text
- split content into structured categories

---

## Key Functional Components

### 1. API Key Loader
Reads the Gemini API key from `key.txt`.

### 2. PDF Text Extraction
Extracts resume text from all pages of the uploaded PDF.

### 3. Resume Section Splitter
Uses regex patterns to classify text into sections like experience, skills, and qualifications.

### 4. Default Analysis Generator
Creates a formatted initial summary of the extracted resume data.

### 5. Chat Session
Starts a Gemini chat session and allows the user to ask follow-up questions about the resume.

---

## Example Use Case
A student uploads a resume PDF and receives:
- an initial structured analysis
- feedback on skills and qualifications
- the ability to ask follow-up questions such as:
  - “How can I improve my resume?”
  - “What are my strongest skills?”
  - “Is my experience section good enough?”

---

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
