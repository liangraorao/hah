"""
Created by Liangraorao on 2019/7/17 23:31
 __author__  : Liangraorao
filename : fisher.py
"""
from app import current_app
from helper import is_isbn_or_key
from yushu_book import YushuBook
import json

app = current_app()

@app.route('/book/search/<q>/<page>')
def search(q, page):
    is_key = is_isbn_or_key(q)
    if is_key == 'isbn':
        result = YushuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_keyword(q)
    return json.dumps(result), 200, {'content-type':'application/json'}
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=app.config['DEBUG'], port=8000)