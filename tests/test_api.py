import sys
import os
from datetime import datetime

# Добавляем корневую директорию в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from testmain import app  # Импортируем приложение FastAPI

# Создаем клиент для тестирования
client = TestClient(app)


def test_get_server_time():
    """
    Тестирует эндпоинт "/time"
    """
    response = client.get("/time")
    assert response.status_code == 200  # Проверяем статус код
    data = response.json()
    assert "server_time" in data  # Проверяем, что ключ "server_time" есть в ответе

    # Проверяем, что server_time — это строка в формате ISO 8601
    try:
        datetime.fromisoformat(data["server_time"])
    except ValueError:
        assert False, "server_time is not a valid ISO 8601 datetime string"


def test_get_word():
    """
    Тестирует эндпоинт "/get-word"
    """
    response = client.get("/get-word")
    assert response.status_code == 200  # Проверяем статус код
    data = response.json()
    assert "word" in data  # Проверяем, что ключ "word" есть в ответе

    # Проверяем, что слово находится в списке допустимых значений
    valid_words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    assert data["word"] in valid_words, f"Unexpected word: {data['word']}"


def test_get_number():
    """
    Тестирует эндпоинт "/get-number"
    """
    response = client.get("/get-number")
    assert response.status_code == 200  # Проверяем статус код
    data = response.json()
    assert "number" in data  # Проверяем, что ключ "number" есть в ответе

    # Проверяем, что число находится в диапазоне от 1 до 100
    number = data["number"]
    assert isinstance(number, int), f"Expected integer, got {type(number)}"
    assert 1 <= number <= 100, f"Number out of range: {number}"