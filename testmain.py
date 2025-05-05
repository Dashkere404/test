from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from datetime import datetime
import logging
import random
import requests
import rollbar

app = FastAPI()

"""# Подключаем статические файлы (если они есть)
app.mount("/static", StaticFiles(directory="frontend"), name="static")"""

import logging
import json

import logging
import json

import os
server_name = "gavno"

import rollbar

rollbar.init(
    access_token='8f5f4d0522a6451c8fc5d832a798d890',
    environment='testenv',
    code_version='1.0'
)

rollbar.report_message('Rollbar is configured correctly', 'info')

class JsonFormatter(logging.Formatter):
    def __init__(self, server_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server_name = server_name

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "lineno": record.lineno,
            "server_name": self.server_name,  # Добавляем имя сервера
        }
        if hasattr(record, "__dict__"):
            extra_data = {k: v for k, v in record.__dict__.items() if k in ["endpoint", "status"]}
            log_record.update(extra_data)
        
        # Отладочный вывод для проверки
        print(f"Log record: {log_record}")
        
        return json.dumps(log_record, ensure_ascii=False)



# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Файл логов
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(JsonFormatter(server_name))

# Консоль
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(JsonFormatter(server_name))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# Настройка логгера
"""logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Записываем логи в файл app.log
        logging.StreamHandler()          # Выводим логи в консоль
    ]
)
logger = logging.getLogger(__name__)"""
# Инициализация Rollbar


@app.middleware("http")
async def rollbar_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Логируем ошибку в Rollbar
        rollbar.report_exc_info()
        raise e
# API endpoints
@app.get("/time")
def get_server_time():
    logger.info(
        "Эндпоинт вызван",
        extra={
            "endpoint": "/time",
            "status": "success"
        }
    )
    """logger.info("Эндпоинт /time был вызван")"""
    return {"server_time": datetime.now().isoformat()}

@app.get("/get-word")
def get_word():
    logger.info("Эндпоинт вызван", extra={"endpoint": "/get-word", "status": "success"})
    words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    return {"word": random.choice(words)}

@app.get("/get-number")
def get_number():
    logger.info("Эндпоинт вызван", extra={"endpoint": "/get-number", "status": "success"})
    number = random.randint(1, 100)
    return {"number": number}

# Для простоты оставим корневой маршрут здесь, но в реальном проекте его лучше перенести во фронтенд
@app.get("/", response_class=HTMLResponse)
@app.head("/", response_class=HTMLResponse)
def read_root():
    logger.info("Корневой эндпоинт вызван", extra={"endpoint": "/root", "status": "success"})
    with open("frontend/index.html", "r") as f:
        html_content = f.read()
    
    # Добавляем уникальный идентификатор сервера в HTML
    html_content_with_server_name = html_content.replace(
        "<body>", 
        f"<body><p>Server: {server_name}</p>"
    )
    
    return HTMLResponse(content=html_content_with_server_name, status_code=200)
