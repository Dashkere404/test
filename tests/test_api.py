from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from testmain import app  # Импортируем ваше приложение FastAPI

# Создаем клиент для тестирования
client = TestClient(app)

"""def test_read_root():
    
    Тестирует корневой эндпоинт "/"
    
    response = client.get("/")
    assert response.status_code == 200  # Проверяем статус код
    assert response.json() == {"message": "Hello, World!"}  # Проверяем содержимое ответа

def test_get_server_time():
    
    Тестирует эндпоинт "/time"
    
    response = client.get("/time")
    assert response.status_code == 200  # Проверяем статус код
    data = response.json()
    assert "server_time" in data  # Проверяем, что ключ "server_time" есть в ответе

    # Проверяем, что server_time — это строка в формате ISO 8601
    from datetime import datetime
    try:
        datetime.fromisoformat(data["server_time"])
    except ValueError:
        assert False, "server_time is not a valid ISO 8601 datetime string"""