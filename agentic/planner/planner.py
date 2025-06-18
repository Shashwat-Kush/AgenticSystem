import json
import os
from groq import Groq
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
        self.llm_client = G;
        self.prompt_template = """"
        Your are an expert AI planner that is tasked with creating a set of steps to achieve that goal. 
        The steps should be specific, actionable, and in a logical order.
        The steps should be written in a JSON array format.
        Goal: {goal}
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
        try:
            plan_items  = json.loads(raw_response)
            steps = [item['description'] for item in plan_items]
        except json.JSONDecodeError:
            steps = []
            for line in raw_response.splitlines():
                if "." in line:
                    _, desc = line.split(".", 1)
                    steps.append(desc.strip())
        return steps
    