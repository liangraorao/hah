"""
Created by Liangraorao on 2019/8/4 18:24
 __author__  : Liangraorao
filename : base.py
"""
from sqlalchemy import Column, SmallInteger, Integer
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager
from datetime import datetime


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_to_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            #文档里写的是db.session.rollback()
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())