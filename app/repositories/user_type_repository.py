from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import BlockUserType
from app.schemas.user_schemas import BlockUserTypeCreate

async def create_user_type(db: AsyncSession, user: BlockUserTypeCreate):
    db_user_type = BlockUserType(
        user_type = user.user_type
    )
    db.add(db_user_type)
    await db.commit()
    await db.refresh(db_user_type)
    return db_user_type

async def get_user_types(db: AsyncSession):
    result = await db.execute(select(BlockUserType))
    return result.scalars().all()
