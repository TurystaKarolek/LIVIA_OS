from providers.base_provider import BaseProvider


class MockProvider(BaseProvider):
    def __init__(self):
        super().__init__("MockProvider")

    def generate(self, prompt):
        return f"[MOCK AI RESPONSE] Received prompt: {prompt}"
