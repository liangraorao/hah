"""
Created by Liangraorao on 2019/8/7 21:26
 __author__  : Liangraorao
filename : wish.py
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc, func
from app.model.base import Base
from sqlalchemy.orm import relationship


from app.spider.yushu_book import YushuBook
from app.model.base import db

class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    isbn = Column(String(15), nullable=False)

    @property
    def book(self):
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(cls.create_time)).all()
        return gifts

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from app.model.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched==False, Gift.isbn.in_(
                isbn_list), Gift.status==1).group_by(Gift.isbn).all()

        count_list = [{'count': w[0], 'isbn':w[1]} for w in count_list]
        return count_list
