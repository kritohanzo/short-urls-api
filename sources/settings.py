from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.environment',
        env_file_encoding='utf-8',
    )

    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'postgres'

    SERVER_SCHEME: str = 'http'
    SERVER_HOST: str = 'localhost'
    SERVER_PORT: int = 8000

    @property
    def postgres_url(self) -> str:
        return (
            'postgresql+asyncpg://'
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    @property
    def server_url(self) -> str:
        return f"{self.SERVER_SCHEME}://{self.SERVER_HOST}:{self.SERVER_PORT}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
