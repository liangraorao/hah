"""
Created by Liangraorao on 2019/8/4 18:23
 __author__  : Liangraorao
filename : gift.py
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.model.base import Base
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    isbn = Column(String(15), nullable=False)