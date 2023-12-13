from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    nextauth_secret: str
    model_config = SettingsConfigDict(env_file="../.env")