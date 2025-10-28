from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schemas import LoginRequest, BlockUserRead, BlockUserCreate, BlockUserTypeRead, BlockUserTypeCreate
from app.repositories.user_repository import create_user, get_users, get_user_details
from app.repositories.user_type_repository import create_user_type, get_user_types
from app.core.db import get_db
from app.core.auth import verify_password, create_access_token, get_current_user
from typing import List

router = APIRouter(prefix="/block_users", tags=["block_users"])

@router.post("/login")
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await get_user_details(login_data)

    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/user_type", response_model=BlockUserTypeRead)
async def create_new_user_type(user: BlockUserTypeCreate, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
     try:
          return await create_user_type(db,user)
     except Exception as e:
          raise HTTPException(status_code=400, detail="User Type Create Failed!")

@router.get('/user_types', response_model=List[BlockUserTypeRead])
async def get_all_user_types(db: AsyncSession = Depends(get_db)):
    try:
        return await get_user_types(db) 
    except Exception as e:
             raise HTTPException(status_code=400, detail=str(e))

# Create user
@router.post("/", response_model=BlockUserRead)
async def create_new_user(user: BlockUserCreate, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return await create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail="User creation failed. Possibly duplicate email or username.")

# List All Users
@router.get('/users', response_model=List[BlockUserRead])
async def get_all_users(db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return await get_users(db) 
    except Exception as e:
             raise HTTPException(status_code=400, detail=str(e))