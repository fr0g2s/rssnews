내가 관심있는 블로그의 새글을 매번 확인하기 힘듦.

일정 시간마다 rss 파싱해서 새글 올라온거 있으면 띄워줌.




#### Component
```
- rssparser: rss들을 더하고, 수정하고, 삭제하는 행위를 한다.
- rssmanager: db에 저장된 rss를 파싱해서 db를 업데이트한다
- router (flask): 어디로 가야하는가
- DB
```


#### DB 필드
```
- id(pk): 글을 구분하기위한 pk
- author: 누가 이 글을 썻는지
- rss: rss관리 시 
- title: 글 제목
- text: 글 내용 보기
- url: 원본으로 갈 수 있도록 url 저장
- published: 최신 글 날짜(?) ex) Mon, 07 Dec 2020 20:26:11 +0900
```

rss버전마다 다르게 인식하면 pk는 다르지만 내용은 같은게 나오나?
