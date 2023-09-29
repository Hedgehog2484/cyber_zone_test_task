from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: SecretStr

    class Config:
        env_file = "app/.env"
        env_file_encoding = "utf-8"


config = Settings()
