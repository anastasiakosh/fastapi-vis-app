from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str
    log_level: str = "info"

    class Config:
        env_file = ".env"

settings = Settings()

