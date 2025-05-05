from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Указываем директорию, из которой сервер будет отдавать файлы
        super().__init__(*args, directory="logs", **kwargs)

# Запускаем сервер на порту 8000
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()