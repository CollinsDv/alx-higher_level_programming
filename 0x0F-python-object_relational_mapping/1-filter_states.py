#!/usr/bin/python3
"""accessing and printing a database contents
"""


def main():
    """prints ensuring certain query requirements"""
    try:
        # connect to database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])


        cur = db.cursor()

        # execute query
        cur.execute('SELECT * FROM states WHERE name like "N%" ORDER BY id ASC')

        # obtain results
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        
        # clean up
        cur.close()
        db.close()

    except MySQLdb.Error, e:
        pass
    finally:
        if 'db' in locals():
            db.close()


if __name__ == '__main__':
    import MySQLdb
    import sys

    main()
