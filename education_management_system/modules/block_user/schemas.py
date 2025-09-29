from pydantic import BaseModel, EmailStr

# Input schema for creating user
class BlockUserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Output schema
class BlockUserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_blocked: bool

    class Config:
        orm_mode = True

# Schema for blocking/unblocking
class BlockUserStatus(BaseModel):
    is_blocked: bool
