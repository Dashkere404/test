from http.server import BaseHTTPRequestHandler, HTTPServer

LOG_FILE = "logs/app.log"

class LogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/logs":
            # Отправляем логи как текст
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f:
                    logs = f.read()
                self.wfile.write(logs.encode())
            else:
                self.wfile.write(b"No logs available")
        else:
            # Возвращаем HTML-страницу
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Logs Viewer</title>
                <script>
                    async function fetchLogs() {
                        const response = await fetch('/logs');
                        const logs = await response.text();
                        document.getElementById('logs').innerText = logs;
                    }
                    setInterval(fetchLogs, 5000); // Обновляем логи каждые 5 секунд
                </script>
            </head>
            <body>
                <h1>Logs Viewer</h1>
                <pre id="logs">Loading logs...</pre>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

# Запуск сервера
HTTPServer(("0.0.0.0", 8000), LogHandler).serve_forever()