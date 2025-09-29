from .base import BaseConfig

class ProdConfig(BaseConfig):
    DEBUG: bool = False
    DB_HOST: str = "prod-db.example.com"
    DB_PORT: int = 5432
    DB_USER: str = "prod_user"
    DB_PASSWORD: str = "prod_pass"
    DB_NAME: str = "education_prod"

config = ProdConfig(_env_file=".env.prod")