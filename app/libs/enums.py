"""
Created by Liangraorao on 2019/8/24 21:50
 __author__  : Liangraorao
filename : enums.py
"""
from enum import Enum


class PendingStatus(Enum):
    Wating = 1
    Success = 2
    Reject = 3
    Redraw = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Wating : {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'gifter': '你已寄出，交易完成'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.Redraw: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            }
        }
        return key_map[status][key]