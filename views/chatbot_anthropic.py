import anthropic
import random
import time
import streamlit as st
import config


# Define parameters
MODEL = "claude-3-haiku-20240307"
API_KEY = config.ANTHROPIC_API_KEY

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

