from pydantic import BaseSettings


class Settings(BaseSettings):
    folder:str = "/data"
    connection_way: str = "dns"
    local: str = "localhost"
    ip_address: str = "0.0.0.0"
    info_service_service_host:str = ""
    dns:str = "info-main"
    

settings = Settings()