from fastapi import FastAPI
from .config import settings
import requests
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Info"}

@app.get("/read")
async def my_ip():
    data = None
    url = "https://api.ipify.org?format=json"
    
    print("Reading IP address info")
    response = requests.get(url=url)

    if response.status_code == 200:
        print("IP Address read")
        return json.loads(response.text)
    else:
        print("Failed to fetch IP address")
        return {"Failed to fetch IP address"}


