drop table if exists rss_entries;
create table rss_entries (
    rss string primary key not null,
    name string not null,
    text string not null,
    url string not null,
    published string not null
);
