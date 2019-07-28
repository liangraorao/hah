"""
Created by Liangraorao on 2019/7/23 20:09
 __author__  : Liangraorao
filename : httper.py
"""
import requests



class HTTP:
    @staticmethod
    def get(url, return_json =True):
       r =  requests.get(url)
       if r.status_code != 200:
           return {} if return_json else ''
       return r.json() if return_json else r.text
