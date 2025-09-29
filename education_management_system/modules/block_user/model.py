from sqlalchemy import Column, Integer, String, Boolean
from education_management_system.core.db import Base

class BlockUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_blocked = Column(Boolean, default=False)
