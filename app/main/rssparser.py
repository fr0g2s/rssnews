import feedparser
import ssl
import sqlite3
import sys

class RssParser:
    def __init__(self):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

    def __getRecentEntries(self, f):
        return f.entries[0]
    def __getAuthor(self, f):
        return f.author
    def __getUrl(self, f):
        return f.link
    def __getTitle(self, f):
        return f.title
    def __getDescription(self, f):
        return f.description
    def __getPublished(self, f):
        return f.published

    def getParsedRss(self, rss):  # return parsed data with dict format
        f = feedparser.parse(rss)
        try:
            recent_f = self.__getRecentEntries(f)
        except Exception as e:
            print('wrong rss or no recent article')
            print('your rss: %s' % rss)
            sys.exit(0)

        data = {}
        data['author'] = self.__getAuthor(recent_f)
        data['title'] = self.__getTitle(recent_f)
        data['url'] = self.__getUrl(recent_f)
        data['title'] = self.__getTitle(recent_f)
        data['description'] = self.__getDescription(recent_f)
        data['published'] = self.__getPublished(recent_f)

        return data

if __name__ == '__main__':
    rpsr = RssParser()
    print('[*] test for parsing rss')
    data = rpsr.getParsedRss('https://rss.blog.naver.com/turttle2s.xml')
    print(data)
    print('='*50)

    print('[*] test for wrong rss')
    data = rpsr.getParsedRss('rss.blog.naver.com/turttle2s.xml')
    print(data)
    print('='*50)
