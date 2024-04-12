#!/usr/bin/python3
"""connecting databases and printing output
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    """print records in databases"""
    # connect
    try:
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        # cursor and query execution
        with db.cursor() as cur:
            cur.execute('''SELECT cities.id, cities.name, states.name
                         FROM cities
                         JOIN states ON cities.state_id = states.id
                         ORDER BY cities.id''')

            # printing results
            for row in cur.fetchall():
                print(row)

    except MySQLdb.Error as e:
        pass
