from pydantic import BaseSettings


class Settings(BaseSettings):
    folder:str = None
    info_service_service_host:str = None
    info_host:str = None
    

settings = Settings()