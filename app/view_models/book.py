"""
Created by Liangraorao on 2019/8/3 14:22
 __author__  : Liangraorao
filename : book.py
"""

class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price, self.isbn])
        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]



class __BookViewModel:

    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'total':0,
            'books':[],
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books']= [cls.__cut_book_data(data)]
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