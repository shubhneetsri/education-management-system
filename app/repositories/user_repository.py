from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.models.user import BlockUser
from app.schemas.user_schemas import BlockUserCreate, LoginRequest
from app.core.auth import get_password_hash

async def create_user(db: AsyncSession, user: BlockUserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = BlockUser(
        user_type=user.user_type,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(BlockUser).options(selectinload(BlockUser.user_type_rel)))
    return result.scalars().all()

async def get_user_details(db: AsyncSession, login_data: LoginRequest):
    result = await db.execute(select(BlockUser).where(BlockUser.username == login_data.username))
    return result.scalars().first()