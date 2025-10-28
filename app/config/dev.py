from .base import BaseConfig

class DevConfig(BaseConfig):
    DEBUG: bool = True
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "dev_user"
    DB_PASSWORD: str = "dev_pass"
    DB_NAME: str = "education_dev"

config = DevConfig(_env_file=".env.dev")