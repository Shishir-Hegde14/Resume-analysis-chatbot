import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import re

# Function to get the API key
def get_api_key(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

# Configure API for Gemini LLM
genai.configure(api_key=get_api_key('key.txt'))

# Initialize the Gemini LLM with instructions
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=[
        """
        You are an AI resume analyzer. When a resume is provided, first provide an overview analysis based on the 
        sections in the resume, including personal information, experience, skills, qualifications, and hobbies.
        Follow up by allowing the user to ask questions or discuss any section in detail.
        """
    ]
)

# Streamlit app title and PDF uploader
st.title("Resume Analysis Chatbot with Gemini LLM")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = "".join(page.extract_text() for page in reader.pages)
    return text

# Function to split resume content into sections
def split_resume_sections(text):
    sections = {"personal_info": "", "experience": "", "skills": "", "qualifications": "", "hobbies": ""}
    current_section = None

    # Patterns for identifying each section
    section_patterns = {
        "personal_info": r"(name|contact|email|phone|address)",
        "experience": r"(experience|employment|work history)",
        "skills": r"(skills|expertise|proficiencies)",
        "qualifications": r"(education|qualifications|certifications)",
        "hobbies": r"(hobbies|interests|extracurricular)"
    }

    # Split text line by line and classify content
    for line in text.splitlines():
        line_lower = line.lower()
        for section, pattern in section_patterns.items():
            if re.search(pattern, line_lower):
                current_section = section
                break
        
        if current_section:
            sections[current_section] += line + "\n"
    
    return sections

# Function to generate default analysis
def generate_default_analysis(resume_data):
    analysis = "### Resume Analysis:\n"
    if resume_data["personal_info"]:
        analysis += f"**Personal Information:**\n{resume_data['personal_info']}\n\n"
    if resume_data["experience"]:
        analysis += f"**Experience:**\n{resume_data['experience']}\n\n"
    if resume_data["skills"]:
        analysis += f"**Skills:**\n{resume_data['skills']}\n\n"
    if resume_data["qualifications"]:
        analysis += f"**Qualifications:**\n{resume_data['qualifications']}\n\n"
    if resume_data["hobbies"]:
        analysis += f"**Hobbies/Interests:**\n{resume_data['hobbies']}\n\n"
    return analysis

# If a PDF is uploaded, process it
if uploaded_file:
    # Extract and split resume content
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_data = split_resume_sections(resume_text)

    # Generate and display a default analysis
    default_analysis = generate_default_analysis(resume_data)
    st.subheader("Resume Analysis Summary:")
    st.markdown(default_analysis)

    # Initialize chat session if not already started
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(
            history=[{"role": "user", "parts": [default_analysis]}]
        )

    # Display chat history
    for message in st.session_state.chat_session.history:
        st.chat_message("user" if message.role == "user" else "model").markdown(message.parts[0].text)

    # User interaction through chat input
    user_prompt = st.chat_input("Ask about your resume, or discuss your skills and experience")
    
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        
        # Adding resume data (skills section for now) as context for the model
        full_prompt = user_prompt + "\n\nResume Skills:\n" + resume_data.get("skills", "No skills listed.")
        
        # Send message to Gemini model and get response
        response = st.session_state.chat_session.send_message(full_prompt)
        
        # Display the response
        st.chat_message("model").markdown(response.text)
