"""
Created by Liangraorao on 2019/7/21 18:42
 __author__  : Liangraorao
filename : __init__.py.py
"""
from flask import Flask

def current_app():
     app = Flask(__name__)
     app.config.from_object('config')
     register_blueprint(app)
     return app

def register_blueprint(app):
     from app.web.book import web
     app.register_blueprint(web)