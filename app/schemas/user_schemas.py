from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Input schema for creating user
class BlockUserCreate(BaseModel):
    username: str
    user_type: int
    email: EmailStr
    password: str

class BlockUserTypeCreate(BaseModel):
    user_type: str

# Output schema
class BlockUserTypeRead(BaseModel):
    id: int
    user_type: str

    class Config:
        from_attributes = True

class BlockUserRead(BaseModel):
    id: int
    user_type: Optional[BlockUserTypeRead] = Field(..., alias="user_type_rel")
    username: str
    email: EmailStr
    is_blocked: bool

    class Config:
        from_attributes = True

# Schema for blocking/unblocking
class BlockUserStatus(BaseModel):
    is_blocked: bool

class LoginRequest(BaseModel):
    username: str
    password: str
