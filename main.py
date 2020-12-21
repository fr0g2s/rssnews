import rssparser
from flask import Flask

# 웹에서 rss 주소 입력받음
# rss주소는 rssfeed_list.txt에 저장
# rssfeed_list.txt에서 rssfeed 들고옴
# rssfeed 파싱해서 제목만 파싱해서 보여줌
# 등록한 rssfeed 리스트도 보여줌
# 등록했던 rssfeed 리스트 삭제 가능


