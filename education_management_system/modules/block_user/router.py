from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from education_management_system.modules.block_user.schemas import BlockUserRead, BlockUserCreate
from education_management_system.modules.block_user.user import create_user, get_users
from education_management_system.core.db import get_db
from typing import List

router = APIRouter(prefix="/block_users", tags=["block_users"])

# Create user
@router.post("/", response_model=BlockUserRead)
async def create_new_user(user: BlockUserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail="User creation failed. Possibly duplicate email or username.")

# List All Users
@router.get('/users', response_model=List[BlockUserRead])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    try:
        return await get_users(db) 
    except Exception as e:
             raise HTTPException(status_code=400, detail=str(e))