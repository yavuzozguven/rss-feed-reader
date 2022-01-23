import feedparser
from rssitem import RssItem
import random

class FeedParse:
    def __init__(self,url):
        self.url = url

    def get_channelInfo(self):
        feed = {}
        response = self.get_response()
        feed['title'] = self.get_title(response)
        feed['description'] = self.get_description(response)
        feed['link'] = self.get_link(response)
        feed['pubDate'] = self.get_pubDate(response)
        feed['imageUrl'] = self.get_imageUrl(response)
        return feed

    def get_feed(self):
        response = self.get_response()
        feed = []
        for item in self.get_items(response):
            random_number = random.randint(0,150000)
            RssItem = {}
            RssItem['title'] = self.get_item_title(item)
            RssItem['description'] = self.get_item_description(item)
            RssItem['link'] = self.get_item_link(item)
            RssItem['pubDate'] = self.get_item_pubDate(item)
            RssItem['imageUrl'] = self.get_item_imageUrl(item) if self.get_item_imageUrl(item) is not None else "https://source.unsplash.com/random/200x200?sig={random_number}".format(random_number=random_number)
            RssItem['guid'] = self.get_item_guid(item)
            RssItem['author'] = self.get_item_author(item)
            RssItem['category'] = self.get_item_category(item)
            RssItem['comments'] = self.get_item_comments(item)
            feed.append(RssItem)
        return feed        

    def get_response(self):
        return feedparser.parse(self.url)

    def get_title(self,response):
        try:
            return response.feed.title
        except:
            return None

    def get_description(self,response):
        try:
            return response.feed.description
        except:
            return None

    def get_link(self,response):
        try:
            return response.feed.link
        except:
            return None

    def get_pubDate(self,response):
        try:
            return response.feed.published
        except:
            return None
    
    def get_imageUrl(self,response):
        try:
            return response.feed.image.href
        except:
            return None

    def get_items(self,response):
        try:
            return response.entries
        except:
            return None
    
    def get_item_title(self,item):
        try:
            return item.title
        except:
            return None

    def get_item_description(self,item):
        try:
            return item.description
        except:
            return None

    def get_item_link(self,item):
        try:
            return item.link
        except:
            return None

    def get_item_pubDate(self,item):
        try:
            return item.published
        except:
            return None

    def get_item_imageUrl(self,item):
        try:
            return item.image.href
        except:
            return None

    def get_item_guid(self,item):
        try:
            return item.guid
        except:
            return None

    def get_item_author(self,item):
        try:
            return item.author
        except:
            return None

    def get_item_category(self,item):
        try:
            return item.category
        except:
            return None

    def get_item_comments(self,item):
        try:
            return item.comments
        except:
            return None
