"""
Created by Liangraorao on 2019/8/7 21:26
 __author__  : Liangraorao
filename : wish.py
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.model.base import Base
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    isbn = Column(String(15), nullable=False)