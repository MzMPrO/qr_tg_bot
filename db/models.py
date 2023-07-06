import datetime

from sqlalchemy import create_engine, Integer, Column, String, Text, ForeignKey, TIMESTAMP, DateTime, BIGINT, TEXT, \
    Boolean, Date
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(BIGINT, unique=True)
    fullname = Column(String(255))
    phone = Column(String(20))

class Qr_code(Base):
    __tablename__ = "qr_code"
    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True)