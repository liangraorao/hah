from app.model.gift import Gift
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades
from . import web
from flask_login import login_required, current_user
from flask import current_app, flash, redirect, url_for, render_template
from app.model.base import db


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    # 每个礼物对应的心愿数量
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_Model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_Model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_to_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            ###############################
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash("这本书已经添加到你的赠送清单，或已存放到你的心愿清单，请不熬重复添加")

    return redirect(url_for('web.book_detail', isbn=isbn))



@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



