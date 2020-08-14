from pydantic import BaseSettings


class Settings(BaseSettings):
    nfl_api_key: str

    class Config:
        env_file = ".env"
