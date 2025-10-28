from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.core.db import Base
from sqlalchemy.orm import relationship
from app.core.timestamp_mixin import timestampMixin

class BlockUserType(Base, timestampMixin):
    __tablename__= "user_types"

    id = Column(Integer, primary_key=True, index=True)
    user_type = Column(String, unique=True, index=True)


class BlockUser(Base, timestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_type = Column(Integer, ForeignKey("user_types.id"), nullable=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_blocked = Column(Boolean, default=False)

    user_type_rel = relationship("BlockUserType")
