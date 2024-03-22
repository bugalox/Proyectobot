import openai

openai.api_key = "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"

def process_request(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )
    return response["choices"][0]["message"]["content"]


