from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greeting():
    return {"Welcome": "Muhammad Amir"}


@app.get("/board")
def get_board():
    board_data = {
        'tasks': {},
        'columns': {},
        'columnOrder': []
    }
    return {"board": {}}

