import anthropic
import random
import time
import streamlit as st
import config
import hmac

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
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
# Define parameters
MODEL = "claude-3-haiku-20240307"
API_KEY = st.secrets["ANTHROPIC_API_KEY"]

# Anthropic Client
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=API_KEY,
)

st.title("Chatbot")

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

        # Generate message and display stream responses
        with client.messages.stream(
            model=MODEL,
            max_tokens=4096,
            temperature=0,
            system="You are a professor of statistics in a top university, any question on stats will be given with examples and equations to explain the concept clearly.",
            messages=st.session_state.messages
        ) as stream:
            for text in stream.text_stream:
                full_text += text
                response_container.markdown(full_text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_text})

