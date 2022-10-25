# TODO: Для docker удалить load_dotenv
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, Field

load_dotenv()


class Settings(BaseSettings):
    elastic: AnyHttpUrl = Field(default="http://localhost:9200", env="ELASTICSEARCH_DSN")
