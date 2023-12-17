from fastapi_nextauth_jwt import NextAuthJWT
from functools import lru_cache
from dotenv import load_dotenv
load_dotenv()

JWT = NextAuthJWT()

@lru_cache
def get_jwt() -> NextAuthJWT or None:
    return JWT
