from app.forms.book import DriftForm
from app.libs.enums import PendingStatus
from app.libs.mail import send_mail
from app.model.drift import Drift
from app.model.gift import Gift
from app.model.wish import Wish
from app.view_models.book import BookViewModel
from app.view_models.drift import DriftsCollection
from . import web
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_
from app.model.user import User
from app.model.base import db


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的，不能向自己索要书籍')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))

    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(form, current_gift)
        send_mail(current_gift.user.email, '有人想要一本书', 'email/get_gift.html', wisher=current_user,gift=current_gift)
        return redirect(url_for('web.pending'))
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=form)


@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id, Drift.gifter_id == current_user.id)).order_by(
        desc(Drift.create_time)).all()
    views = DriftsCollection(drifts, current_user.id)
    return render_template('pending.html', drifts=views.data)


@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    with db.auto_to_commit():
        drift = Drift.query.filter(Drift.id == did, Drift.gifter_id == current_user.id).first_or_404()
        drift.pending = PendingStatus.Reject
        requester = User.query.get_or_404(drift.requester_id)
        requester.beans += 1
        return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    with db.auto_to_commit():
        drift = Drift.query.filter_by(requester_id=current_user.id, id=did).first_or_404()
        drift.pending = PendingStatus.Redraw
        current_user.beans += 1
    return redirect(url_for('web.pending'))

@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    with db.auto_to_commit():
        drift = Drift.query.filter_by(id=did, gifter_id=current_user.id).first_or_404()
        drift.pending = PendingStatus.Success
        current_user.beans += 1
        gift = Gift.query.filter_by(uid=drift.gifter_id).first_or_404()
        gift.launched = True
        Wish.query.filter_by(
            uid=drift.requester_id, isbn=drift.isbn, launched=False).update({Wish.launched:True})
        return redirect(url_for('web.pending'))

def save_drift(drift_form, current_gift):
    from app.model.base import db
    with db.auto_to_commit():
        drift = Drift()
        drift_form.populate_obj(drift)

        drift.id = current_user.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_id = current_gift.user.id
        drift.gifter_nickname = current_gift.user.nickname

        book = BookViewModel(current_gift.book)
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_image = book.image
        drift.isbn = book.isbn
        current_user.beans -= 1
        db.session.add(drift)



