import streamlit as st

# Import the chat_with_gpt function from chatbot.py
from chatbot import chat_with_gpt

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 Your Chatbot Assistant")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", 
         "content": "You are a helpful assistant."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input from user
prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = chat_with_gpt(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
