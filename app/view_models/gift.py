"""
Created by Liangraorao on 2019/8/13 23:03
 __author__  : Liangraorao
filename : gift.py
"""
from app.view_models.book import BookViewModel


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.gifts_of_mine = gifts_of_mine
        self.wish_count_list = wish_count_list
        self.gifts = self.__parse()


    def __parse(self):
        temp_gifts = []
        for gift in self.gifts_of_mine:
            my_gift = self.__match(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __match(self, gift):
        for wish_count in self.wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']

                r = {
                    'wishes_count': count,
                    'book': BookViewModel(gift.book),
                    'id': gift.id
                }
                return r

