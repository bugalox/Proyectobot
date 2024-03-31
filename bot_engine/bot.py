# bot_engine/bot.py
import openai
from django.shortcuts import redirect

openai.api_key = "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"

def process_request(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )
    answer = response["choices"][0]["message"]["content"]

    # Define la URL base de tu sitio
    base_url = "http://52.6.91.3:8000"

    # Analiza la respuesta para determinar una posible redirección
    redirect_url = None
    if "info personal" in answer.lower():
        redirect_url = base_url + '/personal/'
        answer += f" Puedes encontrar más información sobre información personal aquí: {redirect_url}"
    elif "nóminas" in answer.lower() or "beneficios" in answer.lower():
        redirect_url = base_url + '/nominasbeneficios/'
        answer += f" Puedes encontrar más información sobre nóminas y beneficios aquí: {redirect_url}"
    elif "vacaciones" in answer.lower() or "permisos" in answer.lower():
        redirect_url = base_url + '/vacaciones/'
        answer += f" Puedes encontrar más información sobre vacaciones y permisos aquí: {redirect_url}"
    elif "políticas" in answer.lower():
        redirect_url = base_url + '/politicas/'
        answer += f" Puedes encontrar más información sobre políticas internas aquí: {redirect_url}"
    elif "información general" in answer.lower():
        redirect_url = base_url + '/company_info/'
        answer += f" Puedes encontrar más información general sobre la empresa aquí: {redirect_url}"
    elif "preguntas frecuentes" in answer.lower():
        redirect_url = base_url + '/faq/'
        answer += f" Puedes encontrar más información general sobre la empresa aquí: {redirect_url}"    

    return {'answer': answer, 'redirect_url': redirect_url}
