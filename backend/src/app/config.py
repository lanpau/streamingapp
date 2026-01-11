from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "StreamLive API"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "sqlite+aiosqlite:///./streamlive.db"
    
    model_config = SettingsConfigDict(
        env_prefix="STREAMLIVE_",
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
