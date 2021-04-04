import rssmanager
import sqlite3

rmgr = rssmanager.RssManager()
db = sqlite3.connect('/tmp/rssnews.db')

def test_interface_tail(rmgr, db):
    for data in rmgr.getEntries(db):
        for k, v in data.items():
            print('%s |' % v, end='')
    print('\n'+'='*100+'\n')

def add_test():
    print('[1] Add new RSS ')
    try:
        rmgr.addRss(db, 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.addRss Error: ', e)
    test_interface_tail(rmgr, db)
   
    print('[1-1] Add invalid RSS')
    try:
        rmgr.addRss(db, 'rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.addRss Error: ', e)
    test_interface_tail(rmgr, db)

def del_test():
    print('[2] Delete RSS ')
    try:
        rmgr.delRss(db, 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.delRss Error: ', e)
    test_interface_tail(rmgr, db)

    print('[2-1] Del invalid rss ')
    try:
        rmgr.delRss(db, 'invlid.rss')
    except Exception as e:
        print('[-] RssManager.delRss Error: ', e)
    test_interface_tail(rmgr, db)

def edit_test():
    print('[3] Edit RSS')
    try:
        rmgr.editRss(db, 'https://rss.blog.naver.com/turttle2s.xml', 'https://rss.blog.naver.com/r00tdr4g0n.xml')
    except Exception as e:
        print('[-] RssManager.editRss Error: ', e)
    test_interface_tail(rmgr, db)

    print('[3-1] Edit RSS (wrong src RSS)')
    try:
        rmgr.editRss(db, 'wrong.rss', 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] RssManager.editRss Error: ', e)
    test_interface_tail(rmgr, db)

    print('[3-2] Edit RSS (wrong dst RSS)')
    try:
        rmgr.editRss(db, 'https://rss.blog.naver.com/r00tdr4g0n.xml', 'https://rss.blog.naver.com/turttle2s.xml')
    except Exception as e:
        print('[-] Rssmanager.editRss Error: ', e)
    test_interface_tail(rmgr, db)
 

if __name__ == "__main__": # for test
	add_test()
	del_test()
	add_test()
	edit_test()
   
