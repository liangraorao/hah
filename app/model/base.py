"""
Created by Liangraorao on 2019/8/4 18:24
 __author__  : Liangraorao
filename : base.py
"""
from sqlalchemy import Column, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)