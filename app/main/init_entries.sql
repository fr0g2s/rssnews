drop table if exists entries;
create table entries (
    rss string primary key null,
    author string not null,
    published string not null
);
