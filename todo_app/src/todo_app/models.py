from datetime import datetime
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False
    created_at: datetime = datetime.now()

    