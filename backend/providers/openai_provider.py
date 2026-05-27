import os

from dotenv import load_dotenv
from openai import OpenAI

from providers.base_provider import BaseProvider

load_dotenv()


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def send_prompt(
        self,
        system_prompt,
        user_prompt
    ):

        response = (
            self.client.chat.completions.create(
                model="gpt-4o-mini",
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
        )

        return (
            response
            .choices[0]
            .message.content
        )