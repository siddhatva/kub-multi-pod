from fastapi import FastAPI, Depends
import os
from .config import settings
import requests
import json
import logging


app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

async def directory_name():
    return settings.folder

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.post("/create")
async def info(data: str, directory: str = Depends(directory_name)):
    file_path = os.path.join(os.path.join(os.getcwd(), directory), "info.txt")

    logging.info("Writing data to file {}".format(file_path))
    with open(file_path, "w") as f:
        f.write(data)
        logging.info("Wrote data to file")
    return {"Info": data}

@app.get("/read")
async def info():
    data = None
    file_path = os.path.join(os.path.join(os.getcwd(), 'data'), "info.txt")

    logging.info("Reading data from file")

    try:
        with open(file_path, "r") as f:
            data = f.read()
    except (IOError, OSError) as error:
        logging.info("Resource Not Found")
        return "Resource Not Found"

    logging.info("Read data from file")
    return {"Info": data}

@app.get("/ip")
async def ip():
    host = None

    logging.info("Checking host type...")

    if settings.connection_way == "local":
        host = settings.local
        logging.info("Host type is local '{}'.".format(host))
    elif settings.connection_way == "ip":
        host = settings.ip_address
        logging.info("Host type is host '{}'.".format(host))
    elif settings.connection_way == "host_name":
        host = settings.info_service_service_host
        logging.info("Host type is service host '{}'.".format(host))
    elif settings.connection_way == "dns":
        host = settings.dns
        logging.info("Host type is dns '{}'.".format(host))
    else:
        host = "localhost"
        logging.info("Host type is localhost '{}'.".format(host))

    url = "http://" + host + ":5002" + "/read"
    
    print("Reading IP address from '{}'.".format(url))
    logging.info("Reading IP address from '{}'.".format(url))
    response = requests.get(url=url)

    if response.status_code == 200:
        logging.info("IP Address read")
        return json.loads(response.text)
    else:
        logging.info("Failed to fetch IP address")
        return {"Failed to fetch IP address"}

