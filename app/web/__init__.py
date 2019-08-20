from flask import Blueprint, render_template

web = Blueprint('web', __name__)

@web.errorhandler(404)
def not_found(e):
    return render_template('404.html')

from app.web import auth
from app.web import book
from app.web import gift
from app.web import wish
from app.web import main