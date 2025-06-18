import json
import os
from groq import Groq
import re

def extract_first_json_array(text:str)->str:
    pattern = r"\[\s*(?:\{.*?\}\s*,?\s*)+\]"
    match = re.search(pattern, text,re.DOTALL)
    return match.group(0) if match else None


class GroqClient:
    def __init__(self, api_key:str, model:str):
        self.client = Groq(api_key = api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content

class Planner:
    def __init__(self, llm_client):
        self.llm_client = llm_client;
        self.prompt_template = """"
        Your are an expert AI planner that is tasked with creating a set of steps to achieve that goal. 
        The steps should be specific, actionable, and in a logical order.
        The steps should be written in a JSON array format.
        **Only output a single JSON array of steps. No headings or extra text.**
        Goal: {user_goal}
        Output format:
        [
            {{ "step": 1, "description": "…" }},
            {{ "step": 2, "description": "…" }},
            …
        ]
        """

    def generate_plan(self,user_goal) -> str:
        prompt = self.prompt_template.format(user_goal = user_goal)
        raw_response = self.llm_client.generate(prompt)
        # print(f"Raw response from LLM:\n{raw_response}\n")
        json_block = extract_first_json_array(raw_response)
        if json_block:
            try:
                objs = json.loads(json_block)
                return [item['description'] for item in objs]
            except json.JSONDecodeError:
                pass
        steps = []
        for line in raw_response.splitlines():
            if "." in line:
                _, desc = line.split(".", 1)
                steps.append(desc.strip())
        return steps
    