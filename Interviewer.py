import google.generativeai as genai
import streamlit as st
import requests
def get_api_key(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
    
genai.configure(api_key=get_api_key('key.txt'))
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

st.set_page_config(
    page_title="Interviewer",
    page_icon=":glasses:",  
    layout="wide",
)

model2 = genai.GenerativeModel('gemini-1.5-flash',
                               system_instruction=['''
                                You extract the qualifications, skills and experience from the prompts. 
                                Here are a few examples on how to go about it:
                                 <EXAMPLE>
                                Input: My qualifications are BTech in Computer Science At PESU, MTech In AI & Machine Learning at IIT Bombay, PhD In IISc Bangalore. My Skills Include Leadership, Complex Problem Solving, C++, Jawa And Python. I have Experience working as an assistsant professor at PESU and have been a visiting professor at IIT Delhi & DTU
                                Output: Qualifications - BTech in Computer Science At PESU; MTech In AI & Machine Learning at IIT Bombay; PhD In IISc Bangalore. Skills - Leadership; Complex Problem Solving; C++; Jawa; Python. Experience - Assistsant professor at PESU; Visiting professor at IIT Delhi & DTU.
                                </EXAMPLE>  
                                <EXAMPLE>
                                Input:  I have experience working as an senior art consultant at Chitrakala Parishat and have been a feautured Artist at the annual regional art display in Bengaluru. My qualifications are Bachelor in Arts from the National Institute of Design, Masters in Graphic Design at IIT Delhi. My Skills Include Unreal engine, Character Modeling, Technical Illustration And Visual Art Creation.
                                Output: Qualifications - Bachelor in Arts from the National Institute of Design; Masters in Graphic Design at IIT Delhi. Skills - Unreal engine; Character Modeling; Technical Illustration And Visual Art Creation. Experience - Senior Art Consultant at Chitrakala Parishat; feautured Artist at the annual regional art display in Bengaluru.
                                </EXAMPLE>
                                <EXAMPLE>
                                Input: Hey
                                Output: NULLNORESPONSE
                                </EXAMPLE>
                                '''
                               ])

# maieutic prmopting
model3 = genai.GenerativeModel('gemini-1.5-flash',
                              system_instruction=[
                                  '''
                                  You are a helpful chatbot who's role is to act as an interviewer and to take the user's resume and ask them around 3 questions about their qualifications, experience and skills.
                                  <EXAMPLE>
                                    Input : Qualifications - Bachelor in Arts from the National Institute of Design; Masters in Graphic Design at IIT Delhi. Skills - Unreal engine; Character Modeling; Technical Illustration And Visual Art Creation. Experience - Senior Art Consultant at Chitrakala Parishat; feautured Artist at the annual regional art display in Bengaluru.
                                    Output : So about your qualifications, How was your experience at the National Institute Of Design?
                                  </EXAMPLE>
                                  ''',
                                  '''Wait for the user's response on the first output and then ask around 2 more questions with respect to their response, after which move onto other qualifications and do the same. And after that repeat the same for experience then add 2 questions on top, after which move onto other experiences. And after that repeat the same for skills then add 2 questions on top, after which move onto other skills. And then after which end the session after you are finished with asking questions for every category(Qualifications, Experience, Skills) ''',
                                  '''If response is "NULL" go on with asking questions and consider that the user has given a response.'''
                                  '''In the end, give the user a score out of 100, based on their answers and give the user a few suggestions in the form of the a list'''
                              ],
                              generation_config={
                                  "temperature":1,
                                  "top_p":0.95,
                                  "top_k":30,
                                  "stop_sequences":[
                                  ],
                                  "max_output_tokens":1000,                                  
                              },
                              safety_settings={
                                  genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: 
                                      genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
                              })
# chat_session=model.start_chat(
#     history=[ 
#                 # {
#                 #     "role":"user",
#                 #     "parts":[
#                 #         "Can I want to go to sweden"
#                 #     ],
#                 # },
#                 # {
#                 #     "role":"model",
#                 #     "parts":[
#                 #         "Sure! let me know what kind of a trip you are looking for"
#                 #     ],
#                 # },
#     ]
# )
st.title("Interviewer")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model3.start_chat(history1 = [])
    
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
    
prompt = st.chat_input("Answer Here!")
if prompt:
    st.chat_message("user").markdown(prompt)
    resume = model2.generate_content(prompt)
    question = resume.text.strip()
    if question!= "NULLNORESPONSE":
        question_maybe = question
        combined_prompt = f"{prompt}"
        resp = st.session_state.chat_session.send_message(combined_prompt)
        with st.chat_message("assistant"):
            st.markdown(resp.text)
    else:
        resp = st.session_state.chat_session.send_message(prompt)
        with st.chat_message("assistant"):
            st.markdown(resp.text)
    # resp = st.session_state.chat_session.send_message(prompt)
    # with st.chat_message("assistant"):
    #     st.markdown(resp.text)

# if prompt:=st.chat_input("Please enter your query here "):
#     st.chat_message("user").markdown(prompt)
#     resp = f"{chat_session.send_message(prompt).text}"
#     with st.chat_message("assistant"):
#         st.markdown(resp)

# prompt = ""
# while prompt!='exit':
#     prompt = input("Please enter your query or type exit: ")
#     # resp = model.generate_content(prompt)
#     resp = chat_session.send_message(prompt)
#     print(resp.text)

