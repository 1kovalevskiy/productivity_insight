from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Сервис пользовательских рецептов'
    description: str = 'Сервис пользовательских рецептов'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'test@test.ru'
    first_superuser_password: Optional[str] = 'password'
    first_superuser_nickname: Optional[str] = 'developer'

    class Config:
        env_file = '.env'


settings = Settings()
