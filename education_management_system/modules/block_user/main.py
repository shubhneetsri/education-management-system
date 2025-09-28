from fastapi import FastAPI
from block_user.router import router as block_user_router
from education_management_system.core.db import engine, Base
import asyncio

# Create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())

app = FastAPI(title="Block User Module Example")

# Include block_user routes
app.include_router(block_user_router)
