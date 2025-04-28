from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user
from app.routes import home, users, habits

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

app.include_router(home.router)
app.include_router(users.router)
app.include_router(habits.router)