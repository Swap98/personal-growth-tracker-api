from pydantic import BaseModel
from typing import Optional

# Schema for creating a habit
class HabitCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for updating a habit (all fields optional)
class HabitUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None