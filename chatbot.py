import openai
import os     # Provides functions for interacting with the operating system.
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chatbot logic
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(  # API call
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content
