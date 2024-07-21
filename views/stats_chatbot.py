import anthropic
import random
import time
import streamlit as st
import hmac
from openai import OpenAI


# Check password
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.success("This chatbot is trained to give insights into statistics concepts. It can even write code too! Enter the password given to continue.")
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect.")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.
    

# Setup model selection 
with st.sidebar: 
    st.divider() 
    st.info("You can select and switch the LLM used at anytime!")
    model_selected = st.radio(
    "Select the LLM to use",
    ["Anthropic Haiku", "OpenAI GPT-4o mini"],
    captions = ["Less powerful but more concise model", "More powerful but more verbose"])

# Main Streamlit app starts here
# Define parameters
ANTHRO_MODEL = "claude-3-haiku-20240307"
OPENAI_MODEL = "gpt-4o-mini"
ANTHRO_API_KEY = st.secrets["ANTHROPIC_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
SYSTEM = "You are an expert in statistics. You are well versed in explaining stats concepts and also in analysis of data. You have read all the textbooks on statistics and can quote from there. "

# Anthropic Client
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=ANTHRO_API_KEY,
)

# OpenAI Client 
openai_client = OpenAI(api_key=OPENAI_API_KEY)

st.title("Stats Chatbot 🧮")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Create a placeholder for the assistant's response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_text = ""
        
        if model_selected == "Anthropic Haiku": 
            # Generate message and display stream responses
            with client.messages.stream(
                model=ANTHRO_MODEL,
                max_tokens=4096,
                temperature=0,
                system=SYSTEM,
                messages=st.session_state.messages
            ) as stream:
                for text in stream.text_stream:
                    full_text += text
                    response_container.markdown(full_text)
        else: 
            response = openai_client.chat.completions.create(
                        model=OPENAI_MODEL,
                        messages=st.session_state.messages,
                        stream=True
                        ) 
        
            for chunk in response:
                delta = chunk.choices[0].delta
                chunk_text = getattr(delta, 'content', '')
                if chunk_text:
                    full_text += chunk_text
                response_container.markdown(full_text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_text})

