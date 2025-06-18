import os
from groq import Groq

class GroqLLMClient:
    def __init__(self, api_key: str = None, model: str = "llama3-8b-8192"):
        """
        A thin wrapper around the Groq SDK that exposes a `.generate(prompt)` method.
        """
        self.client = Groq(api_key=api_key)
        self.model  = model

    def generate(self, prompt: str) -> str:
        """
        Send a single-prompt chat completion and return the assistant’s reply.
        """
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content