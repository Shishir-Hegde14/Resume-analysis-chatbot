import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit as st
st.set_page_config(
    page_title="Carrer Guidance",
    page_icon=":robot:",  
    layout="wide",
)


# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown('''<style>
            [data-testid="stAppViewContainer"] {
                background-image: url('file:///C:/Users/sushr/projects/IOproject/career.jpg');
                background-image: linear-gradient(to bottom right, purple, blue);
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
            }
</style>''', unsafe_allow_html=True)


from requirements import (
    finance_accounting_requirements,
    healthcare_social_work_requirements,
    engineering_technology_requirements,
    creative_arts_design_requirements,
)
import streamlit as st
import requests

def main():

    st.title("Career Requirements Overview")

    st.header("Select a Field to Learn More:")
    field = st.selectbox(
        "Choose a field:",
        ("Finance or Accounting", "Healthcare or Social Work", "Engineering or Technology", "Creative Arts or Design")
    )

    if field == "Finance or Accounting":
        st.subheader("Requirements:")
        requirements = finance_accounting_requirements()
    elif field == "Healthcare or Social Work":
        st.subheader("Requirements:")
        requirements = healthcare_social_work_requirements()
    elif field == "Engineering or Technology":
        st.subheader("Requirements:")
        requirements = engineering_technology_requirements()
    elif field == "Creative Arts or Design":
        st.subheader("Requirements:")
        requirements = creative_arts_design_requirements()

    
    for key, value in requirements.items():
        if isinstance(value, list):
            value = ', '.join(value)
        st.write(f"**{key}:** {value}")

if __name__ == "__main__":
    main()


career_questions = [
    {"question": "1. Do you enjoy working with numbers?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
    {"question": "2. Are you interested in helping others?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Healthcare or Social Work"},
    {"question": "3. Do you like solving complex problems?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Engineering or Technology"},
    {"question": "4. Do you enjoy creating art or designs?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Creative Arts or Design"},
    {"question": "5. Are you comfortable with financial planning?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
    {"question": "6. Do you have a passion for healthcare?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Healthcare or Social Work"},
    {"question": "7. Are you interested in technology advancements?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Engineering or Technology"},
    {"question": "8. Do you like working on creative projects?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Creative Arts or Design"},
    {"question": "9. Do you enjoy financial analysis?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
    {"question": "10. Would you like to work in social services?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Healthcare or Social Work"},
    {"question": "11. Are you interested in designing systems?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Engineering or Technology"},
    {"question": "12. Do you have a talent for graphic design?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Creative Arts or Design"},
    {"question": "13. Do you enjoy budgeting and finance?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
    {"question": "14. Do you want to work with mental health?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Healthcare or Social Work"},
    {"question": "15. Are you excited by engineering projects?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Engineering or Technology"},
    {"question": "16. Do you enjoy performing arts?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Creative Arts or Design"},
    {"question": "17. Do you like working in a structured environment?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
    {"question": "18. Are you interested in public health?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Healthcare or Social Work"},
    {"question": "19. Do you enjoy programming?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Engineering or Technology"},
    {"question": "20. Are you passionate about writing or literature?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Creative Arts or Design"},
    {"question": "21. Do you want to work in investment banking?", "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"], "field": "Finance or Accounting"},
]


def get_field_score(responses):
    scores = {field: 0 for field in set(q["field"] for q in career_questions)}
    for i, response in enumerate(responses):
        if response == "Strongly Agree":
            scores[career_questions[i]["field"]] += 4
        elif response == "Agree":
            scores[career_questions[i]["field"]] += 3
        elif response == "Disagree":
            scores[career_questions[i]["field"]] += 1
        elif response == "Strongly Disagree":
            scores[career_questions[i]["field"]] += 0
    return scores




def get_udemy_courses(field):
    
    mock_courses = {
        "Finance or Accounting": ["Financial Analysis", "Investment Strategies"],
        "Healthcare or Social Work": ["Mental Health Counseling", "Public Health"],
        "Engineering or Technology": ["Data Structures", "Software Engineering"],
        "Creative Arts or Design": ["Graphic Design Basics", "Creative Writing"]
    }
    return mock_courses.get(field, [])


def job_insights():
    return {
        "Finance or Accounting": {
            "insight": "High demand, average salary $70,000. Roles include Financial Analyst, Accountant.",
            "recruitment_rate": "High recruitment rate expected in the next 5 years."
        },
        "Healthcare or Social Work": {
            "insight": "Growing field, average salary $60,000. Roles include Social Worker, Nurse.",
            "recruitment_rate": "Very high recruitment rate expected due to aging population."
        },
        "Engineering or Technology": {
            "insight": "High demand, average salary $85,000. Roles include Software Engineer, Data Scientist.",
            "recruitment_rate": "Extremely high recruitment rate in tech sectors."
        },
        "Creative Arts or Design": {
            "insight": "Competitive field, average salary $50,000. Roles include Graphic Designer, Art Director.",
            "recruitment_rate": "Moderate recruitment rate; opportunities in digital design are increasing."
        }
    }


eligibility_questions = [
    {"question": "1. What is your current GPA?", "options": ["Above 3.5", "3.0 - 3.5", "Below 3.0", "N/A"], "field": None},
    {"question": "2. Have you taken advanced placement (AP) courses?", "options": ["Yes", "No", "Not yet", "N/A"], "field": None},
    {"question": "3. Do you have any extracurricular activities?", "options": ["Yes", "No", "Some", "N/A"], "field": None},
    {"question": "4. What is your intended major?", "options": ["Finance", "Nursing", "Engineering", "Art"], "field": None},
    {"question": "5. Have you taken standardized tests (SAT/ACT)?", "options": ["Yes", "No", "Planning to", "N/A"], "field": None},
    {"question": "6. Do you have any volunteer experience?", "options": ["Yes", "No", "Some", "N/A"], "field": None},
    {"question": "7. Are you considering community college?", "options": ["Yes", "No", "Maybe", "N/A"], "field": None},
    {"question": "8. What type of college are you interested in?", "options": ["Public", "Private", "Community", "Online"], "field": None},
    {"question": "9. What is your preferred location?", "options": ["In-state", "Out-of-state", "International", "N/A"], "field": None},
    {"question": "10. Are you eligible for financial aid?", "options": ["Yes", "No", "Unsure", "N/A"], "field": None},
]


st.title("Career Test")


st.header("Career Interest Questionnaire")
responses = []
for q in career_questions:
    response = st.radio(q["question"], q["options"], key=q["question"])
    responses.append(response)

if st.button("Submit Career Test"):
    scores = get_field_score(responses)
    st.write("Your scores by field:", scores)

    
    top_field = max(scores, key=scores.get)
    

    
    courses = get_udemy_courses(top_field)
    st.write(f"Relevant Udemy courses for {top_field}:", courses)

    
    insights = job_insights()
    st.write(insights[top_field]["insight"])
    st.write(insights[top_field]["recruitment_rate"])


st.header("College Eligibility Quiz")
eligibility_responses = []
for q in eligibility_questions:
    response = st.radio(q["question"], q["options"], key=q["question"] + "_eligibility")
    eligibility_responses.append(response)

if st.button("Check Eligibility"):
    eligibility_score = 0
    for response in eligibility_responses:
        if response == "Yes" or response == "Above 3.5":
            eligibility_score += 1

    if eligibility_score >= 5:
        st.success("You are eligible for many top colleges!")
    else:
        st.warning("You may want to consider improving your profile for better eligibility.")

