import openai
import os
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Inicializa o histórico de mensagens
historico = [
    {"role": "system", "content": "Você é um assistente de IA útil."}
]

def obter_resposta(prompt_usuario):
    # Adiciona a mensagem do usuário ao histórico
    historico.append({"role": "user", "content": prompt_usuario})

    # Chama a API do ChatGPT
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=historico,
        temperature=0.7
    )

    # Extrai a resposta do assistente
    mensagem_assistente = resposta.choices[0].message["content"].strip()

    # Adiciona a resposta do assistente ao histórico
    historico.append({"role": "assistant", "content": mensagem_assistente})

    return mensagem_assistente

def iniciar_chat():
    print("Bem-vindo ao ChatGPT no terminal! Digite 'sair' para encerrar.\n")
    while True:
        entrada_usuario = input("Você: ")
        if entrada_usuario.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat. Até logo!")
            break
        resposta = obter_resposta(entrada_usuario)
        print(f"ChatGPT: {resposta}\n")

if __name__ == "__main__":
    iniciar_chat()
