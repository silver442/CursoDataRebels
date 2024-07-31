from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar la clave API desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear una instancia del cliente OpenAI
client = OpenAI(api_key=api_key)

def main():
    print("Bienvenido al Chat de OpenAI. Escribe 'salir' para terminar.")
    chat_history = []

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                messages=chat_history,
                model="gpt-3.5-turbo",
            )
            ai_response = response.choices[0].message.content.strip()
            print("IA:", ai_response)

            chat_history.append({"role": "system", "content": ai_response})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()