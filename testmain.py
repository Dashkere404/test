from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/time")
def get_server_time():
    return {"server_time": datetime.now().isoformat()}

from pydantic import BaseModel
import random

# Эндпоинт для получения слова
@app.get("/get-word")
def get_word():
    words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    return {"word": random.choice(words)}

# Эндпоинт для получения цифры
@app.get("/get-number")
def get_number():
    number = random.randint(1, 100)
    return {"number": number}
