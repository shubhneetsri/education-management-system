from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from education_management_system.modules.block_user.schemas import BlockUserRead, BlockUserCreate
from education_management_system.core.db import get_db

router = APIRouter(prefix="/block_users", tags=["block_users"])

# Create user
@router.post("/", response_model=BlockUserRead)
async def create_new_user(user: BlockUserCreate, db: AsyncSession = Depends(get_db)):
    return await user.create_user(db, user)
