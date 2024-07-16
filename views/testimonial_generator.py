import streamlit as st
import anthropic
import hmac

# Check password
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["simple_pass"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.success("This tool helps to generate testimonal based on your input.")
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect.")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
# Define parameters
MODEL = "claude-3-haiku-20240307"
API_KEY = st.secrets["ANTHROPIC_API_KEY"]
SYSTEM = """
You are a teacher/educator that is writing testimonial for students that are leaving the school at secondary 4 or 5 in Singapore. Make use of the inputs given to write a 5 paragraph testimonial for the student. 
Emphasize on the acheivements and examples but never make up examples that are not stated. If needed, you can give generic statements.
        """

# Anthropic Client
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=API_KEY,
)

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
