from .base import BaseConfig

class StageConfig(BaseConfig):
    DEBUG: bool = False
    DB_HOST: str = "stage-db.example.com"
    DB_PORT: int = 5432
    DB_USER: str = "stage_user"
    DB_PASSWORD: str = "stage_pass"
    DB_NAME: str = "education_stage"

config = StageConfig(_env_file=".env.stage")