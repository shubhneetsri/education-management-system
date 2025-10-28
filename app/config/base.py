from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    APP_NAME: str = "Education Management System"
    DEBUG: bool = False

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        env_file = ".env"  # default, can be overridden
        env_file_encoding = "utf-8"
