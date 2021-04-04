drop table if exists articles;
create table articles (
    id integer primary key autoincrement,
    rss string not null,
    author string not null,
    url string not null,
    title string not null,
    description string not null,
    published string not null
);

-- insert into articles () values ();
