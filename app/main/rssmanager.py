import rssparser
import sqlite3
import feedparser

class RssManager:
    def __init__(self):
        pass

    def getArticles(self, db):   # 
        cur = db.execute('select author, title, description, url, published from articles order by id desc')
        articles = [dict(
                        author=row[0], 
                        title=row[1], 
                        description=row[2], 
                        url=row[3], 
                        published=row[4]
                        ) for row in cur.fetchall()]
        db.commit()
        return articles

    def delRss(self, db, del_rss):  # delete rss from db
        if not self.__isExist(db, del_rss):
            raise Exception('given RSS is not exist in DB: ', del_rss)

        db.execute('delete from articles where rss = ?', [ del_rss ])
        db.commit()

    def editRss(self, db, old_rss, new_rss):
        if self.__isExist(old_rss):
            raise Exception('old RSS is invalid: ', old_rss)
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid: ', new_rss)
        db.execute('update articles SET rss = ? where rss = ?', [ new_rss, old_rss ])
        db.commit()

    def addRss(self, db, new_rss):
        if self.__isExist(db, new_rss):
            raise Exception('new RSS is already exist in DB: ', new_rss)
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid: ', new_rss)
        
        data = rssparser.RssParser().getParsedRss(new_rss)

        db.execute('insert into articles (rss, author, url, title, description, published) values (?,?,?,?,?,?)', 
                [ new_rss, data['author'], data['url'], data['title'], data['description'], data['published'] ])

    def __isExist(self, db, rss):
        cur = db.execute('select rss from articles where rss = ?', [ rss ])
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

def test_interface_tail(rmgr):
    print(rmgr.getArticles(db))
    print('='*50)

if __name__ == "__main__": # for test
    rmgr = RssManager()
    db = sqlite3.connect('/tmp/rssnews.db')
    print('[*] First ')
    test_interface_tail(rmgr)

    print('[*] Delete RSS ')
    try:
        rmgr.delRss(db, 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.delRss Error: ', e)
    test_interface_tail(rmgr)

    print('[*] Del invalid rss ')
    try:
        rmgr.delRss(db, 'invlid.rss')
    except Exception as e:
        print('[-] RssManager.delRss Error: ', e)
    test_interface_tail(rmgr)
    
    print('[*] Add new RSS ')
    try:
        rmgr.addRss(db, 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.addRss Error: ', e)
    test_interface_tail(rmgr)
    
    print('[*] Add invalid RSS')
    try:
        rmgr.addRss(db, 'rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.addRss Error: ', e)
    test_interface_tail(rmgr)
