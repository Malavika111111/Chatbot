import openai
import os     # Provides functions for interacting with the operating system.
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Adding the chatbot logic
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(  # API call
        model="gpt-4",  
        messages=messages,
        temperature=0.7
    )
    # Correct way to access the content in the response
    return response['choices'][0]['message']['content']

