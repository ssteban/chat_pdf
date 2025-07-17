import google.generativeai as goai
from dotenv import load_dotenv
import os

load_dotenv()

goai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt):
    model = goai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(contents=prompt)
    return response 

pregunta = "explica que es la inteligencia artificial y sus aplicaciones en la vida cotidiana y si cres que es necesario que la gente aprenda a programar para poder usarla de manera efectiva"
response = generate_response(pregunta)

print(response.text)

