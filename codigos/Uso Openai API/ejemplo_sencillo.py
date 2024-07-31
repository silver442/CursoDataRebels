from openai import OpenAI
import os
from dotenv import load_dotenv

#Para crear un entorno virtual:
#python -m venv .venv

#Para activar mi entorno virtual
#.\.venv\Scripts\activate

#hay que instalar openai y dotenv
#pip install openai python-dotenv

# Cargar la clave API desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear una instancia del cliente OpenAI
client = OpenAI(api_key=api_key)

def main():
    print("Bienvenido al Chat de OpenAI. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            break

        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="gpt-3.5-turbo",
            )
            print("IA:", response.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()