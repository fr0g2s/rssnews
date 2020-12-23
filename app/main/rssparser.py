import feedparser
import ssl

class RssParser:
    def __init__(self):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        self.f = ''
        self.recent_feed_entries = {}

    def setFeed(self, rss):
        self.f = feedparser.parse(rss)
        recent_entries = self.f.entries[0]
        self.recent_feed_entries['title'] = recent_entries.title
        self.recent_feed_entries['link'] = recent_entries.link
        self.recent_feed_entries['description'] = recent_entries.description
        self.recent_feed_entries['published'] = recent_entries.published_parsed

    def getFeedTitle(self):
        return self.f.feed.title


if __name__ == "__main__": # for test
    rssparser = RssParser()
    rss_list = []

    with open('./url_list.txt','r') as f:
        for rss in f.read().split('\n'):
            if rss == '':
                continue
            rss_list.append(rss)
    
    for rss in rss_list:
        print('[*] Parse rss: %s' % rss)
        rssparser.setFeed(rss)
        print('[*] Title: %s' % rssparser.getFeedTitle())
        print('[*] Recent Article: %s' % rssparser.recent_feed_entries['title'])
        print('-'*40)
