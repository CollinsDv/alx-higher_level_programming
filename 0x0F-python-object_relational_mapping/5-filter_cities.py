#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # connect
    try:
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        # cursor and query execution
        with db.cursor() as cur:
            cur.execute('''SELECT DISTINCT cities.id, cities.name
                         FROM cities
                         JOIN states ON cities.state_id = states.id
                         WHERE states.name = %s
                         ORDER BY cities.id''', (sys.argv[4],))

            # printing results
            if cur.fetchall():
                print(', '.join([row[1] for row in cur.fetchall()]))

    except MySQLdb.Error as e:
        print(e)
        pass
