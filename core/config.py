from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    NEXTAUTH_SECRET: str
    NEXTAUTH_URL: str
    UPSTASH_REDIS_REST_URL: str
    UPSTASH_REDIS_REST_TOKEN: str
    model_config = SettingsConfigDict(env_file="../.env")

@lru_cache
def get_settings() -> Settings:
    return Settings()
