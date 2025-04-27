from fastapi import APIRouter
from app.schemas.user_schema import UserRegister
from app.utils.hashing import hash_password
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token_schema import Token
from app.utils.token import create_access_token
from app.utils.hashing import pwd_context
from app.utils.hashing import hash_password


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Temporary list to save users in memory
users_db = []
users_db = [
    {
        "username": "swapnil",
        "email": "swapnil@example.com",
        "password": "$2b$12$d1eipbEe9LhqcQoW8g2sP.934QRiALiWix4I9W.ATFbwUeVmy/7Ju"  # hashed "mysecretpassword"
    }
]
print("Current users in database:", users_db)
print(hash_password("mysecretpassword"))


@router.post("/register")
def register_user(user: UserRegister):
    hashed_pw = hash_password(user.password)

    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_pw
    }
    
    users_db.append(new_user)

    return {
        "username": new_user["username"],
        "email": new_user["email"],
        "message": "User registered successfully!"
    }

@router.post("/login", response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = None
    for u in users_db:
        if u["username"] == user_credentials.username:
            user = u
            break

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    if not pwd_context.verify(user_credentials.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    access_token = create_access_token(data={"sub": user["username"]})

    return {"access_token": access_token, "token_type": "bearer"}

