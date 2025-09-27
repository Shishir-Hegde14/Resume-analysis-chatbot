import google.generativeai as genai
import streamlit as st
def get_api_key(file_name):
    with open(file_name,'r') as file:
        return file.read().strip()

st.set_page_config(
    page_title="ASSK",
    page_icon=":Bot:",  
    layout="wide",
)
genai.configure(api_key=get_api_key('jobkey.txt'))


model = genai.GenerativeModel('gemini-1.5-flash',
                              system_instruction={
                                '''
                                As a career advisor, your role is to guide users on their journey toward achieving their career goals, from initial skills acquisition to final resume and interview preparation. Here are examples of user inputs and how you can structure a detailed career plan based on them:

                                <EXAMPLE> **INPUT**: "I want to become a data scientist. I need guidance on which skills to acquire, how to build a portfolio, and tips on applying for jobs." **OUTPUT**: - **Career Path**: Data Scientist - **Step 1**: **Goal Setting**: Identify specific data science goals, such as preferred industry or specialization (e.g., NLP, computer vision). - **Step 2**: **Skills Acquisition**: Start with foundational courses in statistics, programming (Python, R), and machine learning. Explore platforms like Coursera, Udacity, or DataCamp. - **Step 3**: **Project Building**: Practice with hands-on projects. Use public datasets (e.g., Kaggle, UCI) to build a portfolio with a range of projects (data analysis, machine learning models). - **Step 4**: **Portfolio Development**: Create an online portfolio (e.g., GitHub, personal website) showcasing projects, with clear documentation of objectives, datasets, and results. - **Step 5**: **Networking & Mentorship**: Join data science groups, attend conferences, and seek mentorship to gain industry insights and grow connections. - **Step 6**: **Job Application Strategy**: Tailor your resume to highlight relevant skills and projects. Research and apply to data science roles in industries that align with your interests. - **Step 7**: **Interview Preparation**: Review common data science interview topics, such as algorithms and case studies. Practice with mock interviews and coding challenges. - **Step 8**: **Continuous Learning**: Keep up with emerging tools and trends (e.g., deep learning, cloud platforms), attending workshops and obtaining relevant certifications.
                                Additional Tips: Consider refining your LinkedIn profile to showcase skills and projects, and engage with data science content to enhance visibility.

                                <EXAMPLE> **INPUT**: "I’m interested in becoming a UX Designer. What should I do to get started and find freelance opportunities?" **OUTPUT**: - **Career Path**: UX Designer - **Step 1**: **Skill Development**: Start with foundational design principles, user research, and tools like Figma and Adobe XD. Consider beginner courses on platforms like Skillshare or Coursera. - **Step 2**: **Understanding User Experience**: Develop empathy and research skills by studying UX methodologies such as user journeys and personas. - **Step 3**: **Practical Experience**: Apply your knowledge by creating mock projects or contributing to open-source projects. Focus on building end-to-end designs. - **Step 4**: **Portfolio Building**: Assemble a digital portfolio showcasing completed projects with case studies detailing your design thinking, process, and outcomes. - **Step 5**: **Networking & Professional Development**: Join UX communities (e.g., UX Design Collective on LinkedIn), attend design workshops, and find a mentor if possible. - **Step 6**: **Freelance Opportunities**: Register on freelance sites like Upwork and Fiverr, and apply to relevant gigs. Build connections with agencies or local businesses for potential collaborations. - **Step 7**: **Resume & Online Presence**: Craft a resume focused on UX skills and include links to your portfolio. Maintain a LinkedIn profile and engage with UX content. - **Step 8**: **Interview Preparation**: Prepare for design interviews by reviewing portfolio pieces, explaining your design decisions, and practicing whiteboard challenges.
                                Additional Tips: Keep updated on design trends and tools. Regularly refresh your portfolio to include new projects that showcase current UX/UI practices.

                                If a particular step is completed display the next set of steps. Only if the last step is completed, proceed towards resume building step


                                '''
                                '''
                                final step being resume building
                                '''

                              },
                              generation_config={
                                "temperature":2,
                                "top_p":0.95,
                                "top_k":30,
                                "stop_sequences":[
                                  ],
                                "max_output_tokens":10000
                              }
                              )

st.title("ASSK")

if "chat_session" not in st.session_state:
  st.session_state.chat_session = model.start_chat(history = [])

def translate_role_for_streamlit(user_role):
  if user_role == "model":
    return "assistant"
  else:
    return user_role

for message in st.session_state.chat_session.history:
  with st.chat_message(translate_role_for_streamlit(message.role)):
    st.markdown(message.parts[0].text)

prompt = st.chat_input("Ask Gemini")
if prompt:
  st.chat_message("user").markdown(prompt)
  resp = st.session_state.chat_session.send_message(prompt)
  with st.chat_message("assistant"):
    st.markdown(resp.text)


