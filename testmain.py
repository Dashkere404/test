from fastapi import FastAPI
from datetime import datetime
import psutil
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
START_TIME = datetime.now()  # Засекаем время старта сервера

@app.get("/health")
async def health_check():
    process = psutil.Process(os.getpid())  # Данные текущего процесса
    
    return {
        "status": "OK",  # Основной статус
        "uptime_seconds": (datetime.now() - START_TIME).total_seconds(),
        "memory_usage_mb": process.memory_info().rss / 1024 / 1024,
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "disk_usage_percent": psutil.disk_usage("/").percent,
        "version": "1.0.0"  # Можно брать из переменных окружения
    }