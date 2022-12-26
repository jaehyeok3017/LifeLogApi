from typing import List, Union
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    comment : str
    esg : str
    timestamp : str
    owner_id : int


class Todo(BaseModel):
    id: int
    comment : str
    esg : str
    timestamp : str
    owner_id : int


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id : int
    is_active: bool
    todo_items: List[Todo] = []
    post_items: List[Post] = []

    class Config:
        orm_mode = True