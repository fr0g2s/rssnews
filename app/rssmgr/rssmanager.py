from . import rssparser
import sqlite3
import feedparser

class RssManager:
    def __init__(self):
        pass

    def getArticles(self, db):    
        cur = db.execute('select author, title, description, url, published from articles order by id desc')
        articles = [dict(
                        author=row[0], 
                        title=row[1], 
                        description=row[2], 
                        url=row[3], 
                        published=row[4]
                        ) for row in cur.fetchall()]
        return articles

    def getEntries(self, db):
        cur = db.execute('select rss, author from entries')
        entries = [dict(rss=row[0], author=row[1]) for row in cur.fetchall()]
        return entries

    def updateRss(self, db):    # update published in entries
        cur = db.execute('select rss from entries')
        rssentries = [dict(row[0]) for row in cur.fetchall()]
        

    def delRss(self, db, del_rss):  # delete rss from entries db
        if not self.__isExist(db, del_rss):
            raise Exception('given RSS is not exist in DB: ', del_rss)
        db.execute('delete from entries where rss = ?', [ del_rss ])
        db.commit()

    def editRss(self, db, old_rss, new_rss): # edit rss in entries db
        if not self.__isExist(db, old_rss):
            raise Exception('old RSS is invalid: ', old_rss)
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid: ', new_rss)
        parsed = rssparser.RssParser().getParsedRss(new_rss)
        db.execute('update entries set rss = ?, author = ?, published = ? where rss = ?', 
                    [ new_rss, parsed['author'], parsed['published'], old_rss ])
        db.commit()

    def addRss(self, db, new_rss):  # add rss to entries db
        if self.__isExist(db, new_rss):
            raise Exception('new RSS is already exist in DB(entries): ', new_rss)
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid: ', new_rss)
        
        try:
            rssparser.RssParser().getParsedRss(new_rss)
        except Exception as e:
            raise 

        if data != False:
            db.execute('insert into entries (rss, author, published) values (?,?,?)', [ new_rss, data['author'], data['published'] ])
            return True
        else:   # wrong RSS
            return False
    
    def __isExist(self, db, rss):
        cur = db.execute('select rss from entries where rss = ?', [ rss ])
        if cur.fetchone():
            return True
        return False

    def __isValidRss(self, rss):
        try:
            f = feedparser.parse(rss)
        except Exception as e:
            print('[-] RssManager: __isValidRss Error:', e)
            return False
        return True

