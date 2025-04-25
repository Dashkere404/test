from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from datetime import datetime
import random

app = FastAPI()

# Подключаем статические файлы (если нужно)
app.mount("/static", StaticFiles(directory="static"), name="static")

# API endpoints
@app.get("/time")
def get_server_time():
    return {"server_time": datetime.now().isoformat()}

@app.get("/get-word")
def get_word():
    words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    return {"word": random.choice(words)}

@app.get("/get-number")
def get_number():
    number = random.randint(1, 100)
    return {"number": number}

# Для простоты оставим корневой маршрут здесь, но в реальном проекте его лучше перенести во фронтенд
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)
