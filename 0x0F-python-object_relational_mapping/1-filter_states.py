#!/usr/bin/python3
"""accessing and printing a database contents
"""
import MySQLdb
import sys


def main():
    """prints ensuring certain query requirements"""
    try:
        # connect to database
        db = MySQLdb.connect(port=3306, host='localhost',
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cur = db.cursor()

        # execute query
        cur.execute('''SELECT * FROM states
                    WHERE name like BINARY 'N%' ORDER BY id ASC''')

        # obtain results
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)

        cur.close()

    except MySQLdb.Error as e:
        pass
    finally:
        if 'db' in locals():
            db.close()


if __name__ == '__main__':

    main()
