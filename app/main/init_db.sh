#!/usr/bin/bash
sqlite3 /tmp/rssnews.db < init_articles.sql
sqlite3 /tmp/rssnews.db < init_entries.sql
