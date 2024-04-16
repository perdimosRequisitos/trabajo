from fastapi import FastAPI
import uvicorn

# * Run server
# * uvicorn main:app --reload

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)
