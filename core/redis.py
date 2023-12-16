from core.config import get_settings
from upstash_redis import Redis
from functools import lru_cache

settings = get_settings()

redis = Redis(url=settings.UPSTASH_REDIS_REST_URL, token=settings.UPSTASH_REDIS_REST_TOKEN)

@lru_cache
def get_redis():
    return redis