from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения.

    Attributes:
        app_title (str): Название приложения.
        database_url (str): URL базы данных.
        secret (str): Секретный ключ приложения.
        model_config (SettingsConfigDict): Конфигурация модели.
    """
    app_title: str = 'Бронирование переговорок'
    database_url: str
    secret: str = 'secret'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
