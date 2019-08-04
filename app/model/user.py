"""
Created by Liangraorao on 2019/8/4 18:23
 __author__  : Liangraorao
filename : user.py
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from app.model.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(50), unique=True, nullable=False)
    email = Column(String(50),unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))