drop table if exists entries;
create table entries (
    rss string primary key null,
    author string not null
);

insert into entries values('https://rss.blog.naver.com/turttle2s.xml', 'fr0g2s');
