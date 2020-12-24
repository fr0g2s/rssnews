import rssparser

class RssManager:
    def __init__(self):
        self.url_list = []

    def getRssList(self):
        return self.url_list

    def delRss(self, del_rss):
        if not self.__isExist(del_rss):
            raise Exception('no RSS to delete')
        self.__updateRssStore('del', del_rss)

    def editRss(self, old_rss, new_rss):
        if not self.__isExist(old_rss):
            raise Exception('no RSS to edit')
        elif self.__isExist(new_rss):
            raise Exception('new RSS is already exist')
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid')
        self.__updateRssStore('edit', old_rss, new_rss)

    def addRss(self, new_rss):
        if self.__isExist(new_rss):
            raise Exception('can not add exist RSS') 
        if not self.__isValidRss(new_rss):
            raise Exception('new RSS is invalid')
        self.__updateRssStore('add', new_rss)

    def __updateRssStore(self, cmd, *rss):
        if cmd == 'del':
            self.url_list.remove(rss[0])
        elif cmd == 'edit':
            rss_idx = self.url_list.index(rss[0])
            self.url_list[rss_idx] = rss[1]
        elif cmd == 'add':
            self.url_list.append(rss[0])
        
        with open('./url_list.txt','w') as f:
            for url in self.url_list:
                if url == '':
                    continue
                f.write(url+'\n')

    def __isExist(self, rss):
        if rss in self.url_list:
            return True
        return False

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
