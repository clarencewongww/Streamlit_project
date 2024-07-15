import streamlit as st 
import pandas as pd 
import numpy as np

st.title('🎓 Testimonial Generator')

# Sidebar
with st.sidebar:
    st.success("Welcome!", icon="🔥")
    model_radio = st.radio(
        "Choose a model",
        ("GPT-3.5 (Cheaper)", "GPT-4o (Better, more expensive)")
    )

st.header("Example of dataframe")
df1 = pd.DataFrame({"name":["Tom", "Bom", "Gom"], "class":["3A", "3G", "4T"]})
#df2 = pd.DataFrame(np.random.randint(100000,10000000, size=(2000,10)), columns=list("ABCDEFGHIJ"))
st.write(df1)
#st.write(df2)

# Attribute section with columns
st.header("Type in the attributes")
# Set columns for input
col1, col2 = st.columns([2,2])
col3, col4 = st.columns([6,2])
# columns 
with col1:
    stu_name = st.text_input('Enter the name of student:', 'Titus')
with col2:
    stu_class = st.text_input('Enter the class of student:', '3E')
with col3:
    stu_cca = st.selectbox("Select CCA of student:", ("Batminton", "Scouts", "NCC", "Basketball", "Drama"), index = None, placeholder="Select CCA...")
with col4:
    stu_age = st.number_input("Enter the age of student:", 12, 19)

# Display the data
st.write(f"""
        The student name is {stu_name}. \n 
        Student class is {stu_class}. \n
        
        Student age is {stu_age}. 
         """)
#Student is from CCA of {stu_cca}.  \n
if stu_cca != None:
    st.write(f"Student is from CCA of {stu_cca}.")