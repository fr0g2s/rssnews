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
- *rss: 어디서 파싱했는지 
- name: 누가 이 글을 썻는지
- text: 글 내용 보기
- published: 최신 글 날짜(?)
```
