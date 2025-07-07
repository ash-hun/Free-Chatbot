from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./environment/.env",
        env_file_encoding="utf-8",
    )
    CONTAINER_NAME: str
    AZURE_OPENAI_API_KEY : str
    AZURE_OPENAI_ENDPOINT : str
    LANGSMITH_TRACING: bool
    LANGSMITH_ENDPOINT: str
    LANGSMITH_PROJECT: str
    LANGSMITH_API_KEY: str

@lru_cache
def get_settings():
    return Settings()