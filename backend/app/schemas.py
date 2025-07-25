from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str | None = None
    username: str
    password: str
