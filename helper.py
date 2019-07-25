"""
Created by Liangraorao on 2019/7/23 19:23
 __author__  : Liangraorao
filename : helper.py
"""

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('_', '')
    if '_' in word and len(short_word)==10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return  isbn_or_key

if __name__ == '__main__':
    r = is_isbn_or_key('12345ju67890123')
    print(r)