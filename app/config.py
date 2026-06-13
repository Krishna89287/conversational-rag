import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"

    @property
    def llm_ready(self):
        return bool(self.groq_api_key)


settings = Settings()
