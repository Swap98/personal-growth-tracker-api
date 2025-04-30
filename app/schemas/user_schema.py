from pydantic import BaseModel, EmailStr

# Schema for incoming user registration requests
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for outgoing user responses
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True