from openai import OpenAI
from openai_key import openai_key
class CModel:
    def __init__(self):
        self.client = OpenAI(api_key=openai_key)
    def get_response(self, input_text) -> str:
        response = self.client.responses.create(
            model="gpt-4.1",
            input=input_text
        )
        return response.output_text
