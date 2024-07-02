import aiohttp
import json
import os

class OllamaClient:
    def __init__(self, base_url=os.getenv('OLLAMA_URL', 'http://localhost:11434')):
        self.base_url = base_url

    async def generate(self, prompt, model=os.getenv('OLLAMA_MODEL', 'llama2')):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt}
            ) as response:
                if response.status == 200:
                    full_response = await response.text()
                    return self.parse_response(full_response)
                else:
                    return f"Error: {response.status}"

    def parse_response(self, response_text):
        lines = response_text.strip().split('\n')
        parsed_response = ""
        for line in lines:
            try:
                data = json.loads(line)
                if 'response' in data:
                    parsed_response += data['response']
            except json.JSONDecodeError:
                continue
        return parsed_response.strip()