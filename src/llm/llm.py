from openai import OpenAI


class LLM:
    def __init__(self, key: str, model: str, role: str):
        self.key = key
        self.model = model
        self.role = role
        self.client = OpenAI(api_key=self.key)

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model, messages=[{"role": self.role, "content": prompt}]
        )
        return response
