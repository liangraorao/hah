from flask import render_template

from . import web




@web.route('/')
def index():
    pass
    # return render_template('search_result.html')


@web.route('/personal')
def personal_center():
    pass
