from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from .environment import Environment


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = "Fuhrer"

    app_version: str = "1.0.0"

    environment: Environment = Environment.DEVELOPMENT

    debug: bool = False

    host: str = "0.0.0.0"

    port: int = 8000

    database_url: str = "sqlite:///./fuhrer.db"

    redis_url: str = "redis://localhost:6379"

    secret_key: str = "change-me-in-development"

    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 60


@lru_cache
def load_settings() -> Settings:
    return Settings()
