#!/usr/bin/python3
"""
accessing and printing a database contents
"""
import MySQLdb
import sys

# connect to database
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

# cursor
cur = db.cursor()

# execute query
cur.execute('SELECT * FROM states ORDER BY id ASC')

# obtain results
rows = cur.fetchall()

for row in rows:
    print(row)
