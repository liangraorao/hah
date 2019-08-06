"""
Created by Liangraorao on 2019/7/21 18:42
 __author__  : Liangraorao
filename : __init__.py.py
"""
from flask import Flask
from app.model.base import db
from flask_login import LoginManager

login_manager = LoginManager()
def current_app():
     app = Flask(__name__)
     app.config.from_object('app.config')
     app.config.from_object('app.secure')
     register_blueprint(app)
     db.init_app(app)
     db.create_all(app=app)
     login_manager.init_app(app=app)
     login_manager.login_view = 'web.login'
     login_manager.login_message = '请先登录或注册'
     return app

def register_blueprint(app):
     from app.web.book import web
     app.register_blueprint(web)