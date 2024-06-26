#!/usr/bin/python3
"""accessing and printing a database contents
"""


def main():
    """prints ensuring certain query requirements"""
    # connect to database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # cursor
    cur = db.cursor()

    # execute query
    cur.execute('''SELECT * FROM states
                WHERE name like BINARY "{}" ORDER BY id ASC'''
                .format(sys.argv[4]))

    # obtain results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    import MySQLdb
    import sys

    main()
