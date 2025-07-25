from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255))     # 평문 (취약)
