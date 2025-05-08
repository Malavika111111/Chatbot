import streamlit as st
from chatbot import chat_with_gpt

# Set page title and icon
st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 Your AI Assistant")

# Initialize chat history in the session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input prompt
prompt = st.chat_input("Say something...")

if prompt:
    # Append user message to the history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get GPT response
    response = chat_with_gpt(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

