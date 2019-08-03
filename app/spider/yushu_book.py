"""
Created by Liangraorao on 2019/7/23 23:05
 __author__  : Liangraorao
filename : yushu_book.py
"""
from app.libs.httper import HTTP
from flask import current_app


class YushuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url ='http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        result = HTTP.get(self.isbn_url.format(isbn))
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        result = HTTP.get(self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.caculate_start(page)))
        self.__fill_collection(result)


    def caculate_start(self, page):
        return (page-1)*current_app.config['PER_PAGE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']
