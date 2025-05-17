import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize client instance using your API key.
client = OpenAI(api_key=api_key)

# Adding the chatbot logic
def chat_with_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content
