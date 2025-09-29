import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import text
from education_management_system.core.db import engine

@pytest.mark.asyncio
async def test_db_connection():
    """
    Test that the database connection can be established
    and a simple query executes successfully.
    """
    # Connect to DB
    async with engine.connect() as conn:
        # Execute a simple query
        result = await conn.execute(text("SELECT 1"))
        value = result.scalar()
        
    assert value == 1, "Database connection failed or returned unexpected result"
