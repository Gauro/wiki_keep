from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None


class SaveArticle(BaseModel):
    title: str
    content: str
    tag: str
    user_id: int
