from pydantic import BaseSettings


class Settings(BaseSettings):
    username: str
    password: str
    host: str
    port: str
    db_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


config = Settings()
