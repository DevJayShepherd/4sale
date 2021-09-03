import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    # Project meta
    PROJECT_TITLE: str = "4sale"
    PROJECT_VERSION: str = "0.1.1"

    # Database
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    JWT_EXPIRATION: int = os.getenv("JWT_EXPIRATION")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")

    ACCESS_KEY: str = os.getenv("ACCESS_KEY")
    SECRET_AWS_KEY: str = os.getenv("SECRET_AWS_KEY")
    BUCKET_NAME: str = os.getenv("BUCKET_NAME")
    S3_FILE_PATH: str = os.getenv("S3_FILE_PATH")


settings = Settings()
