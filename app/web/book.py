"""
Created by Liangraorao on 2019/7/25 21:53
 __author__  : Liangraorao
filename : book.py
"""

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from flask import jsonify,request
from app.web import web
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_key = is_isbn_or_key(q)

        if is_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
        else:
            result = YushuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)