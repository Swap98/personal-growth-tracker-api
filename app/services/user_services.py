from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.hashing import hash_password

# Create and save a new user in the database
def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Fetch a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()