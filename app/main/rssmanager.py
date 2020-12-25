import rssparser
import sqlite3

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
        db.execute('delete from articles where rss = ?', (del_rss))
        db.commit()

    def editRss(self, db, old_rss, new_rss):
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid')
        db.execute('update articles SET rss = ? where rss = ?', (new_rss, old_rss))
        db.commit()

    def addRss(self, db, new_rss):
        if self.__isExist(new_rss):
            raise Exception('can not add exist RSS') 
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid')
        
        data = rssparser.getParsedRss(new_rss)

        db.execute('insert into articles (rss, author, url, title, description, published) values (?, ?, ?)', 
                new_rss, data['author'], data['url'], data['title'], data['description'], data['published'])


    def __isValidRss(self, rss):
        try:
            f = feedparser.parse(rss)
        except Exception as e:
            return False
        return True

if __name__ == "__main__": # for test
    if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
    rmgr = RssManager()
    
    print('[*] Test Start [*]')
    print('[+] Init RSS list: ', rmgr.getRssList())

    try:
        rmgr.delRss('https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print(e)
    print('[+] after delete RSS: ', rmgr.getRssList())
    print('-'*100)

    try:
        rmgr.addRss('https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print(e)
    print('[+] after add RSS: ', rmgr.getRssList())
    print('-'*100)

    try:
        rmgr.editRss('https://rss.blog.naver.com/turttle2s.xml', 'test')
    except Exception as e:
        print(e)
    print('[+] after edit RSS: ', rmgr.getRssList())
    print('-'*100)
