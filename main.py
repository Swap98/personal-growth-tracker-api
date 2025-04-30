from app.core.database import Base, engine
from app.models import user
from app.routes import home, users, habits
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables
Base.metadata.create_all(bind=engine)

app.include_router(home.router)
app.include_router(users.router)
app.include_router(habits.router)