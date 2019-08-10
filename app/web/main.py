from flask import render_template

from app.model.gift import Gift
from app.view_models.book import BookViewModel
from . import web

@web.route('/')
def index():
    gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    return 'personal'
