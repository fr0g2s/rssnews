import rssparser

def test_interface_tail(data):
	print(data)
	print('='*50)

if __name__ == '__main__':
    rpsr = rssparser.RssParser()
    print('[*] test for parsing rss')
    data = rpsr.getParsedRss('https://rss.blog.naver.com/turttle2s.xml')
    test_interface_tail(data)
    print('[*] test for wrong rss')
    data = rpsr.getParsedRss('rss.blog.naver.com/turttle2s.xml')
    test_interface_tail(data)
