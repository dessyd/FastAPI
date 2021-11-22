from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from sqlalchemy.log import class_logger

#
# posts
#


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

#
# users
#

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase): # Need password for user creation
    password: str

class UserOut(UserBase):    # Remove password field from response
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

#
# auth
#

class UserLogin(UserCreate):    # email + password
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str]
