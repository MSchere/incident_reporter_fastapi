from fastapi_nextauth_jwt import NextAuthJWT
import config

def get_jwt() -> str:
    settings = config.Settings()
    JWT = NextAuthJWT(settings.nextauth_secret)
    return JWT