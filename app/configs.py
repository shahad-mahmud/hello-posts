import dataclasses

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_METHODS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]

    BASE_URL: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///./app.db"


@dataclasses.dataclass
class AppConfigs:
    title: str = "Hello Posts"

    version: str = "0.0.1"


settings = Config()
app_configs = dataclasses.asdict(AppConfigs())
