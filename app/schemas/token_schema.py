from pydantic import BaseModel

# Schema for access token response
class Token(BaseModel):
    access_token: str
    token_type: str