import os
from agentic.llm_clients import GroqLLMClient

class Settings:
    def __init__(self):
        self.groq_api_key   = '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'
        self.groq_model     = "llama-3.1-8b-instant"       
        self.llm_client     = GroqLLMClient(
            api_key=self.groq_api_key,
            model=self.groq_model
        )
        self.mem_db         = None  # Placeholder for vector DB URI
        self.search_api_key = "963fd114fb94363c15fa1f2dfb215932b418bbc8e4d325c0bb8c96c8c751717b"
        self.enable_reflection = False