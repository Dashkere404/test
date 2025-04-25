from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

"""@app.get("/")
def read_root():
    return {"message": "Hello, World!"}"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Подключаем папку со статическими файлами
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Возвращаем HTML с кнопками
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Кнопки и API</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          text-align: center;
          margin-top: 50px;
        }
        button {
          padding: 10px 20px;
          margin: 10px;
          font-size: 16px;
          cursor: pointer;
        }
        #result {
          margin-top: 20px;
          font-size: 24px;
          color: green;
        }
      </style>
    </head>
    <body>
      <h1>Нажмите на кнопку</h1>

      <!-- Кнопка для получения слова -->
      <button id="wordButton">Получить слово</button>

      <!-- Кнопка для получения цифры -->
      <button id="numberButton">Получить цифру</button>

      <!-- Кнопка для получения времени -->
      <button id="timeButton">Получить время</button>

      <!-- Результат -->
      <div id="result"></div>

      <script>
        // Функция для отправки запроса к API
        async function fetchData(url) {
          try {
            const response = await fetch(url);
            const data = await response.json();
            document.getElementById('result').innerText = JSON.stringify(data);
          } catch (error) {
            document.getElementById('result').innerText = 'Ошибка: ' + error.message;
          }
        }

        // Обработчики кнопок
        document.getElementById('wordButton').addEventListener('click', () => {
          fetchData('/get-word');
        });

        document.getElementById('numberButton').addEventListener('click', () => {
          fetchData('/get-number');
        });

        document.getElementById('timeButton').addEventListener('click', () => {
          fetchData('/time');
        });
      </script>
    </body>
    </html>
    """

@app.get("/time")
def get_server_time():
    from datetime import datetime
    return {"server_time": datetime.now().isoformat()}

@app.get("/get-word")
def get_word():
    import random
    words = ["Привет", "Мир", "Солнце", "Луна", "Земля"]
    return {"word": random.choice(words)}

@app.get("/get-number")
def get_number():
    import random
    number = random.randint(1, 100)
    return {"number": number}
