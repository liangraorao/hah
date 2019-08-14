from app.model.wish import Wish
from app.view_models.trade import MyTrades
from . import web
from flask_login import current_user, login_required
from app.model.base import db
from flask import flash, redirect, url_for, render_template


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [gift.isbn for gift in wishes_of_mine]
    # 每个礼物对应的心愿数量
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_Model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_Model.trades)


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
