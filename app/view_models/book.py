"""
Created by Liangraorao on 2019/8/3 14:22
 __author__  : Liangraorao
filename : book.py
"""

class BookViewModel:

    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'total':0,
            'books':[],
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books']=[cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'total': 0,
            'books': [],
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        books = {
            'title': data['title'],
            'publisher':data['publisher'],
            'pages': data['pages'] or '',
            'author':'、'.join(data['author']),
            'price': data['price'],
            'summary':data['summary'] or '',
            'image': data['image'],
            'isbn': data['isbn']
        }
        return books