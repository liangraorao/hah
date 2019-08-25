"""
Created by Liangraorao on 2019/8/10 14:39
 __author__  : Liangraorao
filename : manage.py
"""

from app.model.base import db

from app import current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.model.base import Base
from app.model.book import Book
from app.model.gift import Gift
from app.model.wish import Wish
from app.model.user import User
from app.model.drift import Drift


app = current_app()
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
