"""
Created by Liangraorao on 2019/8/4 18:23
 __author__  : Liangraorao
filename : gift.py
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey,desc, func
from app.model.base import Base
from sqlalchemy.orm import relationship
from flask import current_app


from app.spider.yushu_book import YushuBook
from app.model.base import db

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

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(cls.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.model.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched==False, Wish.isbn.in_(
                isbn_list), Wish.status==1).group_by(Wish.isbn).all()

        count_list = [{'count': w[0], 'isbn':w[1]} for w in count_list]
        return count_list
