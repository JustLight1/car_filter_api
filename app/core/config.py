from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения.

    Attributes:
        app_title (str): Название приложения.
        app_description (str): Описание приложения.
        database_url (str): URL базы данных.
        secret (str): Секретный ключ приложения.
        first_superuser_email (EmailStr or None, default = None): Email первого
                                                            суперпользователя.
        first_superuser_password (str or None, default = None): Пароль первого
                                                            суперпользователя.
        model_config (SettingsConfigDict): Конфигурация модели.
    """
    app_title: str = 'Бронирование переговорок'
    database_url: str
    secret: str = 'secret'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
