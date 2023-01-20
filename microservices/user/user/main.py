from fastapi import FastAPI, Depends
import os
from .config import settings
import requests
import json


app = FastAPI()


async def directory_name():
    return settings.folder

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.post("/create")
async def info(data: str, directory: str = Depends(directory_name)):
    file_path = os.path.join(os.path.join(os.getcwd(), directory), "info.txt")

    print("Writing data to file {}".format(file_path))
    with open(file_path, "w") as f:
        f.write(data)
        print("Wrote data to file")
    return {"Info": data}

@app.get("/read")
async def info():
    data = None
    file_path = os.path.join(os.path.join(os.getcwd(), 'data'), "info.txt")

    print("Reading data from file")

    try:
        with open(file_path, "r") as f:
            data = f.read()
    except (IOError, OSError) as error:
        print("Resource Not Found")
        return "Resource Not Found"

    print("Read data from file")
    return {"Info": data}

@app.get("/ip")
async def ip():
    data = None
    url = "http://" + settings.info_service_service_host + "/read"
    
    print("Reading IP address info from {}".format(url))
    response = requests.get(url=url)

    if response.status_code == 200:
        print("IP Address read")
        return json.loads(response.text)
    else:
        print("Failed to fetch IP address")
        return {"Failed to fetch IP address"}

