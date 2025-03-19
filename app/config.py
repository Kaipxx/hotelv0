from typing import Literal

# во 2 версии Pydantic модуль BaseSettings
# был вынесен в отдельную библиотеку pydantic-settings
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # Способ ниже оказался чересчур сложным. Обратите внимание на лаконичный способ с @property
    # @root_validator
    # def get_database_url(cls, v):
    #     v["DATABASE_URL"] = f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}"
    #     return v
    class Config:
        env_file = ".env"

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"



#model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
#print(settings.DB_HOST)