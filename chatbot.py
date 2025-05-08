import os     # Provides functions for interacting with the operating system.
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Adding the chatbot logic
def chat_with_gpt(messages):
    response = client.chat.completions.create(  # ✅ Fixed API call
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content  # ✅ Correct way to access content
