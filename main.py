from fastapi import FastAPI
from app.routes import home, users, habits

app = FastAPI()

app.include_router(home.router)
app.include_router(users.router)
app.include_router(habits.router)