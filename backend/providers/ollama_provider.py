import os

from ollama import Client
from dotenv import load_dotenv

from providers.base_provider import BaseProvider

load_dotenv()

client = Client(
    host=os.getenv("OLLAMA_HOST")
)


class OllamaProvider(BaseProvider):

    def send_prompt(
        self,
        system_prompt,
        user_prompt
    ):

        response = client.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response["message"]["content"]