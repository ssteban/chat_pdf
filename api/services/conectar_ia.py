import google.generativeai as goai
from dotenv import load_dotenv
import os

load_dotenv()

goai.configure(api_key=os.getenv("GEMINI_API_KEY"))

promptEnviar = """
    basado en la siguiente contexto responde la paregunta:

"""
pregunta = """
    pregunta:

"""
contexto = """"
    contexto:

"""



def generateResponse(prompt):
    try:
        model = goai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(contents=prompt)
        return response 
    except Exception as e:
        print(f"Error al generar la respuesta: {e}")

def generatePrompt(promptEnviar, contexto, pregunta):
    prompt = promptEnviar + contexto + pregunta
    return generateResponse(prompt)


