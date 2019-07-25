"""
Created by Liangraorao on 2019/7/23 23:05
 __author__  : Liangraorao
filename : yushu_book.py
"""
from httper import HTTP

class YushuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url ='http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        result = HTTP.get(cls.isbn_url.format(isbn))
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count =15, start =0):
        result = HTTP.get(cls.keyword_url.format(keyword, count, start))
        return result
