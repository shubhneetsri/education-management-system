from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from education_management_system.modules.block_user.model import BlockUser
from education_management_system.modules.block_user.schemas import BlockUserCreate

async def create_user(db: AsyncSession, user: BlockUserCreate):
    hashed_password = user.password # get_password_hash(user.password)
    db_user = BlockUser(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(BlockUser))
    return result.scalars().all()