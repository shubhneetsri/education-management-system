from fastapi import FastAPI
import os
import sys

print(">>> CWD:", os.getcwd())
print(">>> sys.path:", sys.path)
from education_management_system.modules.block_user.router import router as block_user_router

app = FastAPI(title='Education Management System')

@app.get('/test')
def for_test():
    return {'status': 'I am Live.'}

app.include_router(block_user_router)