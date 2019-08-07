from app.model.gift import Gift
from . import web
from flask_login import login_required, current_user
from flask import current_app, flash
from app.model.base import db

@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gift'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            ###############################
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash("这本书已经添加到你的赠送清单，或已存放到你的心愿清单，请不熬重复添加")



@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



