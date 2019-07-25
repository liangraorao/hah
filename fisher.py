"""
Created by Liangraorao on 2019/7/17 23:31
 __author__  : Liangraorao
filename : fisher.py
"""

from flask import Flask

app = Flask(__name__)
print(str(id(app)) + "每次经过的")
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    print(str(id(app)) + "启动")
    app.run(host='127.0.0.1', debug=app.config['DEBUG'], port=8000)