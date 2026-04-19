import os
from openai import OpenAI

# Usa variável de ambiente (NÃO expõe sua chave)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Digite sua pergunta (ou 'sair' para encerrar):")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )

    print("ChatGPT:", resposta.choices[0].message.content)
