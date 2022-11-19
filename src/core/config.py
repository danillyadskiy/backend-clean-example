from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class Settings(BaseSettings):
    hostname: str
    port: int
    elastic_host: str = Field(env="ELASTICSEARCH_HOST")


SETTINGS = Settings()

ROOT_DIR = Path(__file__).parent.parent
