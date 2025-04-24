from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/time")
def get_server_time():
    return {"server_time": datetime.now().isoformat()}

