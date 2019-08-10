from app.model.wish import Wish
from . import web
from flask_login import current_user, login_required
from app.model.base import db
from flask import flash, redirect, url_for


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_to_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            ###############################
            db.session.add(wish)
    else:
        flash("这本书已经添加到你的赠送清单，或已存放到你的心愿清单，请不熬重复添加")

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
