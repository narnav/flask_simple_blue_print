from flask import Blueprint

news = Blueprint('news', __name__,url_prefix='/news')

@news.route('/')
def mainnews():
    return 'news!'

@news.route('/china')
def news_china():
    return 'china news!'