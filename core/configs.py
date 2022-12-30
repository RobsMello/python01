from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:13031526@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'kprPjdvZBzblmAif7MnYtLYb0XpoQhTp3yj18v0TtIo'
    '''
      import secrets
                      
      token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
