"""
Created by Liangraorao on 2019/7/25 21:53
 __author__  : Liangraorao
filename : book.py
"""
import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from flask import jsonify,request, render_template, flash

from app.view_models.book import BookViewModel, BookCollection
from app.web import web
from app.forms.book import SearchForm


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
        # return json.dumps(books, default=lambda o:o.__dict__, ensure_ascii=False)
        # return jsonify(books.books)
    else:
        # return jsonify(form.errors)
        flash("您输入的关键词有误，请重新输入")
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass

@web.route('/my_gifts')
def my_gifts():
    pass

@web.route('/my_wish')
def my_wish():
    pass
@web.route('/pending')
def pending():
    pass

@web.route('/index')
def index():
    pass