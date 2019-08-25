"""
Created by Liangraorao on 2019/7/25 21:53
 __author__  : Liangraorao
filename : book.py
"""
from app.libs.helper import is_isbn_or_key
from app.model.gift import Gift
from app.model.wish import Wish
from app.spider.yushu_book import YushuBook
from flask import jsonify,request, render_template, flash

from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import Trade
from app.web import web
from app.forms.book import SearchForm
from flask_login import current_user


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_key = is_isbn_or_key(q)

        yushu_book = YushuBook()
        if is_key == 'isbn':
            yushu_book.search_by_isbn(q)

        else:
            yushu_book.search_by_keyword(q)
        books.fill(yushu_book,q)
    else:
        flash("您输入的关键词有误，请重新输入")
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    #默认情况下
    has_in_giftes = False
    has_in_wishes = False


    # 书籍详情信息
    yushu_book = YushuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])

    # 用户登录情况
    if current_user.is_authenticated:
        if Gift.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = Trade(trade_gifts)
    trade_wishes_model = Trade(trade_wishes)

    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)





