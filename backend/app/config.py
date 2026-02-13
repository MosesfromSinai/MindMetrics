from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/mindmetrics"
    allowed_origins: list[str] = ["http://localhost:3000"]
    debug: bool = False

    model_config = {"env_file": ".env"}


settings = Settings()
