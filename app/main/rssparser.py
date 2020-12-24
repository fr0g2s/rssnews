import feedparser
import ssl
import sqlite3

class RssParser:
    def __init__(self):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

    def setFeed(self, db, rss): # save to db
        self.f = feedparser.parse(rss)
        recent_entries = self.f.entries[0]
        self.recent_feed_entries['title'] = recent_entries.title
        self.recent_feed_entries['link'] = recent_entries.link
        self.recent_feed_entries['description'] = recent_entries.description
        self.recent_feed_entries['published'] = recent_entries.published_parsed

    def getFeedTitle(self, db):
        pass

