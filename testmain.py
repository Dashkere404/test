from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from datetime import datetime
import logging
import random
import rollbar

app = FastAPI()

"""# Подключаем статические файлы (если они есть)
app.mount("/static", StaticFiles(directory="frontend"), name="static")"""

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Записываем логи в файл app.log
        logging.StreamHandler()          # Выводим логи в консоль
    ]
)
logger = logging.getLogger(__name__)
# Инициализация Rollbar
rollbar.init(
    '8f5f4d0522a6451c8fc5d832a798d890',  # Замените на ваш токен из Rollbar
    environment='development'  # Или 'production', если вы деплоите
)

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
    logger.info("Эндпоинт /time был вызван")
    raise ValueError("Ошибка в эндпоинте /time")
    return {"server_time": datetime.now().isoformat()}

@app.get("/get-word")
def get_word():
    logger.info("Эндпоинт /get-word был вызван")
    words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    return {"word": random.choice(words)}

@app.get("/get-number")
def get_number():
    logger.info("Эндпоинт /get-number был вызван")
    number = random.randint(1, 100)
    return {"number": number}

# Для простоты оставим корневой маршрут здесь, но в реальном проекте его лучше перенести во фронтенд
@app.get("/", response_class=HTMLResponse)
@app.head("/", response_class=HTMLResponse)
def read_root():
    logger.info("Корневой был вызван")
    with open("frontend/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)
