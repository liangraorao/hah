"""
Created by Liangraorao on 2019/7/25 21:53
 __author__  : Liangraorao
filename : book.py
"""

from helper import is_isbn_or_key
from yushu_book import YushuBook

#
# @app.route('/book/search/<q>/<page>')
# def search(q, page):
#     is_key = is_isbn_or_key(q)
#     if is_key == 'isbn':
#         result = YushuBook.search_by_isbn(q)
#     else:
#         result = YushuBook.search_by_keyword(q)
#     return result
    # return json.dumps(result), 200, {'content-type':'application/json'}