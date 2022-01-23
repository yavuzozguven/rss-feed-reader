class RssItem:
    def __init__(self,title,description,link,pubDate,imageUrl,guid,author,category,comments):
        self.title = title
        self.description = description
        self.link = link
        self.pubDate = pubDate
        self.imageUrl = imageUrl
        self.guid = guid
        self.author = author
        self.category = category
        self.comments = comments