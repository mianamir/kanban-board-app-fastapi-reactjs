from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greeting():
    return {"Welcome": "Muhammad Amir"}


@app.get("/board")
def get_board():
    board_data = {
        'tasks': {
            'task-1': {'id': 'task-1', 'content': 'create user'},
            'task-2': {'id': 'task-2', 'content': 'update user'},
            'task-3': {'id': 'task-3', 'content': 'view user'},
            'task-4': {'id': 'task-4', 'content': 'delete user'},
        },
        'columns': {
            'column-1': {
                'id': 'column-1', 
                'title': 'TO DO',
                'taskIds': ['task-1', 'task-2']
            },
            'column-2': {
                'id': 'column-2', 
                'title': 'TO DO',
                'taskIds': ['task-2', 'task-3']
            },
        },
        'columnOrder': ['column-1', 'column-2']
    }
    return {"board": board_data}

