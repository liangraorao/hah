"""
Created by Liangraorao on 2019/8/4 18:23
 __author__  : Liangraorao
filename : gift.py
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey,desc
from app.model.base import Base
from sqlalchemy.orm import relationship
from flask import current_app

from app.spider.yushu_book import YushuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    isbn = Column(String(15), nullable=False)

    @classmethod
    def recent(cls):
        recent_gifts = Gift.query.filter_by(launched=False).group_by(
            cls.isbn).order_by(
            desc(cls.create_time)).distinct().limit(
            current_app.config['RECENT_UPLOAD']).all()
        return recent_gifts

    @property
    def book(self):
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
