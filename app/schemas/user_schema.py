from pydantic import BaseModel, EmailStr

# Incoming request schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Response schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
