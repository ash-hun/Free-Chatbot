from openai import AzureOpenAI
from config import get_settings
settings = get_settings()

class ChatModel:
    def __init__(self, model_name: str="gpt-4o-mini"):
        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-15-preview"
        )
        self.model_name = model_name

    def invoke(
            self, 
            user_messages: str, 
            system_prompt: str="You are a helpful assistant.", 
            temperature: float=0.7, 
            max_tokens: int=2048, 
            top_p: float=1, 
            frequency_penalty: float=0, 
            presence_penalty: float=0
        ) -> str:
        ''' chat inference with openai api '''
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_messages}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        return response.choices[0].message.content