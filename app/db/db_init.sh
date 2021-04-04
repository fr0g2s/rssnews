#!/usr/bin/bash
sqlite3 /tmp/rssnews.db < articles_init.sql
sqlite3 /tmp/rssnews.db < entries_init.sql
