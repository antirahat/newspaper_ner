from google import genai
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path=".env.local")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="what is the capital of France?"
)
print(response.text)