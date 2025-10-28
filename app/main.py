from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
import os
import sys
from sqlalchemy.future import select
from app.models.user import BlockUser
from app.core.db import get_db
from app.core.auth import verify_password, create_access_token
from pydantic import BaseModel

# print(">>> CWD:", os.getcwd())
# print(">>> sys.path:", sys.path)
from app.api.v1.user_router import router as block_user_router

app = FastAPI(title='Education Management System')


@app.get('/test')
def for_test():
    return {'status': 'I am Live.'}


app.include_router(block_user_router)