from pydantic import BaseModel
from typing import Optional

class HabitCreate(BaseModel):
    title: str
    description: Optional[str] = None
class HabitUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
