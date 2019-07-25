"""
Created by Liangraorao on 2019/7/17 23:31
 __author__  : Liangraorao
filename : fisher.py
"""
import json

from flask import Flask,make_response
from helper import is_isbn_or_key
from yushu_book import YushuBook

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/hello')
def hello():
    #和普通函数不一样的地方，返回status code 200 ，301,404
    #content_type http headers
    # content_type = text/html,若为小程序提供数据，content_type=application/json
    # response
    """
    # 第一种返回：
     # return '<html></html>'
     # 返回的cotent-type=text/html  这种在网页上会显示成网页标签，而不会显示此文案
    """
    """
     第二种返回：
      headers = {
        'content-type': 'text/html'
    }
    return make_response('<html></html>', 404, headers)
    """
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('abcd', 404, headers)
    response.headers = headers
    return response

@app.route('/book/search/<q>/<page>')
def search(q, page):
    is_key = is_isbn_or_key(q)
    if is_key=='isbn':
        result = YushuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_keyword(q)
    return json.dumps(result), 200, {'content-type':'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=81)