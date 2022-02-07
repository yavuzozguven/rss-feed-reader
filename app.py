from flask import Flask,render_template,session,request
from feedparse import FeedParse

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def add_url():
    url = request.form['url']
    feedParse = FeedParse(url)
    channelInfo = feedParse.get_channelInfo()
    feeds = feedParse.get_feed()
    print(feedParse.get_item_imageUrl(feeds[0]))
    return render_template('index.html',feeds=feeds,channelInfo=channelInfo)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    

    

