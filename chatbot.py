import openai
import os    
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Adding the chatbot logic
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(  
        model="gpt-4", 
        messages=messages,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
