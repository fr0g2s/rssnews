drop table if exists rss_entries;
create table rss_entries (
    id integer primary key autoincrement,
    rss string not null,
    author string not null,
    url string not null,
    title string not null,
    description string not null,
    published string not null
);
