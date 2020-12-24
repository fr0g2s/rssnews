내가 관심있는 블로그의 새글을 매번 확인하기 힘듦.
일정 시간마다 rss 파싱해서 새글 올라온거 있으면 띄워줌.

rssmanager는 rss들을 더하고, 수정하고, 삭제하는 등의 행위를 한다.
지금은 file io를 사용하고있는데 DB로 바꿔야겠다.

<h3>DB</h3>
```
- *rss: 어디서 파싱했는지 
- name: 누가 이 글을 썻는지
- text: 글 내용 보기
- published: 최신 글 날짜(?)
```

<h3>architecture</h3>
- rssparser
- rssmanager
- router (flask)
- DB

