from flask import Blueprint

sport = Blueprint('sport', __name__,url_prefix='/sport')

@sport.route('/')
def sp():
    return 'sport!'

@sport.route('/world')
def wd():
    return ' World!'