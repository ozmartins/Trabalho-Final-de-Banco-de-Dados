import openai
import json
import os

def ask_gpt(year, round, question):
    openai.api_key = os.getenv('OPEN_AI_KEY')    
    with open(f'./main/datasets/{year}.{round}.json', 'r', encoding='utf-8') as file:
        dataset = json.load(file)
        mensagem = f"Responda a pergunta abaixo considerando apenas os dadios que constan neste JSON: {json.dumps(dataset)}. \n {question}"
        response = openai.ChatCompletion.create(
            model = "gpt-4o-mini",
            messages = [
                { "role": "system", "content": "Você é um assistente de IA útil" },
                { "role": "user", "content": mensagem }
            ]
        )        
        return response['choices'][0]['message']['content']