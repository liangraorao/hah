"""
Created by Liangraorao on 2019/8/4 18:23
 __author__  : Liangraorao
filename : user.py
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.model.base import Base
from app import login_manager
from app.model.drift import Drift
from app.model.gift import Gift
from app.model.wish import Wish
from app.spider.yushu_book import YushuBook
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from math import floor


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128), nullable=False)
    phone_number = Column(String(50), unique=True, nullable=True)
    email = Column(String(50),unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def set_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != id:
                setattr(self, key, value)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

    def generate_token(self):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=6000)
        temp = s.dumps({'id': self.id}).decode('utf-8')
        return temp

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except Exception as e:
            return False
        uid = data.get('id')
        from app.model.base import db
        with db.auto_to_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    def can_send_drift(self):
        if self.beans <=1:
            return False
        # 成功赠送书籍
        success_gifts_count = Gift.query.filter_by(uid=self.id, launched=False).count()
        # 成功索要到的书籍
        success_receive_count = Drift.query.filter_by(requester_id=self.id, pending=PendingStatus.Success).count()

        return True if floor(success_receive_count/2) <= floor(success_gifts_count) else False

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)
        )
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
