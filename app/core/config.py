from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Aplicación
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # Base de datos
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Telegram
    BOT_TOKEN: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()