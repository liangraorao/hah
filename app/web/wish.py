from app.libs.mail import send_mail
from app.model.gift import Gift
from app.model.wish import Wish
from app.view_models.trade import MyTrades
from . import web
from flask_login import current_user, login_required
from app.model.base import db
from flask import flash, redirect, url_for, render_template


@web.route('/my/wish')
@login_required
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
@login_required
def satisfy_wish(wid):
    wish = Wish.query.filter_by(id=wid, launched=False).first_or_404()
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书，请点击赠送清单添加此书，添加前，请确保自己可以赠送此书')
    else:
        send_mail(wish.user.email, '有人想要送你一本书', 'email/satisify_wish.html', wish=wish, gift=gift)
        flash('已向他/她发送了一封邮件，如果她/他愿意接受你的赠送，你将收到一个鱼漂')
        return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_to_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))
