from flask import Flask,render_template
from feedparse import FeedParse

app = Flask(__name__)

@app.route('/')
def index():
    feedParse = FeedParse('https://www.huffpost.com/section/world-news/feed')
    feed = feedParse.get_feed()
    return render_template('index.html',feed=feed)

if __name__ == '__main__':
    app.run(debug=True)
    

    

