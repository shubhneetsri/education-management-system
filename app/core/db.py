# app/db.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE URL
DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb"
# DATABASE_URL = "mysql+aiomysql://myuser:mypassword@localhost:3306/mydb"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create session maker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
