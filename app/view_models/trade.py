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