from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.habit_schema import HabitCreate, HabitUpdate
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/habits",
    tags=["habits"]
)

# In-memory placeholder for storing habits
habits_db = []

@router.post("/create")
def create_habit(habit: HabitCreate, current_user: str = Depends(get_current_user)):
    new_habit = {
        "id": len(habits_db) + 1,
        "owner": current_user,
        "title": habit.title,
        "description": habit.description
    }
    habits_db.append(new_habit)
    return {"message": "Habit created successfully", "habit": new_habit}

@router.get("/")
def get_habits(current_user: str = Depends(get_current_user)):
    user_habits = [habit for habit in habits_db if habit["owner"] == current_user]
    return {"habits": user_habits}

@router.delete("/{habit_id}")
def delete_habit(habit_id: int, current_user: str = Depends(get_current_user)):
    habit_to_delete = None
    for habit in habits_db:
        if habit["id"] == habit_id and habit["owner"] == current_user:
            habit_to_delete = habit
            break

    if not habit_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit not found")

    habits_db.remove(habit_to_delete)
    return {"message": f"Habit with id {habit_id} deleted successfully"}

@router.put("/{habit_id}")
def update_habit(habit_id: int, habit_update: HabitUpdate, current_user: str = Depends(get_current_user)):
    habit_to_update = None
    for habit in habits_db:
        if habit["id"] == habit_id and habit["owner"] == current_user:
            habit_to_update = habit
            break

    if not habit_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit not found")

    if habit_update.title is not None:
        habit_to_update["title"] = habit_update.title
    if habit_update.description is not None:
        habit_to_update["description"] = habit_update.description

    return {"message": "Habit updated successfully", "habit": habit_to_update}