from .storage import get_todos, save_todos
from .models import TodoItem

def add_item(title: str):
    items = get_todos()
    new_item = TodoItem(id=(max([item.id for item in items], default=0) + 1), title=title)
    items.append(new_item)
    save_todos(items)

def list_items() -> list[TodoItem]:
    return get_todos()

def complete_item(item_id: int):
    items = get_todos()
    for item in items:
        if item.id == item_id:
            item.completed = True
    save_todos(items)

def delete_item(item_id: int):
    items = [item for item in get_todos() if item.id != item_id]
    save_todos(items)