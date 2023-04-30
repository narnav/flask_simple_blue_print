from flask import Flask
from BP_news import news
import sport

app = Flask(__name__)

app.register_blueprint(news)
app.register_blueprint(sport.sport)

@app.route('/')
def home():
    return 'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)