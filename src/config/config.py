from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Authas"
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    PROJECT_DESCRIPTION: str = "Authentication as a service"
    PROJECT_VERSION: str = "v1.0.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    FRONTEND_ORIGIN: str = "http://localhost:3000"

    # class Config:
    #     env_file = ".env"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
