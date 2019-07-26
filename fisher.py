"""
Created by Liangraorao on 2019/7/17 23:31
 __author__  : Liangraorao
filename : fisher.py
"""
from app import current_app

app = current_app()
print(str(id(app)) + "main")


if __name__ == '__main__':
    print(str(id(app)) + "start")
    app.run(host='127.0.0.1', debug=app.config['DEBUG'], port=8000)