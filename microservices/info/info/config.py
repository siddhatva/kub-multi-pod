from pydantic import BaseSettings


class Settings(BaseSettings):
    folder:str = None
    

settings = Settings()