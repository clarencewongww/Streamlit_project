import streamlit as st

#from forms.contact import contact_form


#@st.experimental_dialog("Contact Me")
#def show_contact_form():
#    contact_form()

st.title("About Me!")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_img_circle.png", width=300)

with col2:
    st.header("Clarence Wong", anchor=False)
    st.write("""
        Experienced Civil Servant (Ministry of Education Singapore) \n
        Accomplished data-driven professional with strong expertise in quantitative analysis 
        and statistical modelling, gained through extensive experience in educational data 
        management.
        """
    )
#    if st.button("✉️ Contact Me"):
#        show_contact_form()

# --- EDUCATION ---
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - 2024: Master of Education @ Harvard University (4.00/4.00)
    - 2023: Specialist Diploma in AI Solutions Development @ Temasek Polytechnic (4.00/4.00)
    - 2021: Post-graduate Diploma in Education @ NIE (Credit)
    - 2019: Bachelor of Science with Honours in Chemistry @ NUS (Highest Distinction)
    """
)

# --- EXPERIENCE ---
st.write("\n")
st.subheader("Experience", anchor=False)
st.write(
    """
    - \>3 Years of experience leveraging data-driven methods to inform decision making in education
    - Strong hands-on experience and knowledge in Python, R and Excel
    - Strong understanding of statistical modelling (including advanced statistical quasi-methods) and their applications
    - Strong communicator of data with experience in data visualisation 
    - Vicarious learner that always seeks to update myself on new technologies with continuing education
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - Programming: Python (with ML and data science libraries), R, SQL, JavaScript
    - Data Visualization: MS Excel, Visualization libraies (ggplot, matplotlib etc.)
    - Modeling: Logistic regression, linear regression, multi-level models, decision trees and other machine learning algorithms
    - Statistical Methods: Quasi-methods (regression discontinuity, difference in differences, propensity score matching, instrumental variables etc )
    - Databases: MySQL
    """
)