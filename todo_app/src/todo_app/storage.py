import json
from pathlib import Path
from todo_app.models import TodoItem

DB_PATH = Path("todo_db.json")

def get_todos() -> list[TodoItem]:
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r") as f:
        todos = json.load(f)
    return [TodoItem(**todo) for todo in todos]

def save_todos(todos: list[TodoItem]):
    with open(DB_PATH, "w") as f:
        json.dump([todo.model_dump() for todo in todos], f, indent=4, default=str)
    
    