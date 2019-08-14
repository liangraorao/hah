"""
Created by Liangraorao on 2019/8/10 15:50
 __author__  : Liangraorao
filename : trade.py
"""
class Trade:
    def __init__(self, goods):
        self.total = 1
        self.goods = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_single(good) for good in goods]

    def __map_to_single(self, single):
        if single.create_datetime:
            return dict(
                user_name=single.user.nickname,
                time=single.create_datetime.strftime('%Y-%m-%d'),
                id=single.id
            )
        else:
            return dict(
                username=single.user.nickname,
                time='未知',
                id=single.id
            )

from app.view_models.book import BookViewModel


class MyTrades:
    def __init__(self, trade_of_mine, trade_count_list):
        self.trades = []
        self.trade_of_mine = trade_of_mine
        self.trade_count_list = trade_count_list
        self.trades = self.__parse()


    def __parse(self):
        temp_trades = []
        for trade in self.trade_of_mine:
            my_gift = self.__match(trade)
            if my_gift:
                temp_trades.append(my_gift)
        return temp_trades

    def __match(self, trade):
        for trade_count in self.trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']

                r = {
                    'wishes_count': count,
                    'book': BookViewModel(trade.book),
                    'id': trade.id
                }
                return r

