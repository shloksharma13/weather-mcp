import httpx

from shared.config import OllamaConfig


class OllamaClient:

    def __init__(self):

        self.url = f"{OllamaConfig.BASE_URL}/api/chat"

        self.model = OllamaConfig.MODEL

    async def chat(self, messages):

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                self.url,
                json=payload,
            )

            response.raise_for_status()

            return response.json()


ollama = OllamaClient()