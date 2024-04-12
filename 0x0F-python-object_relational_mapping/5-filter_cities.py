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
            cur.execute('''SELECT cities.name
                         FROM cities
                         JOIN states ON cities.state_id = (
                            SELECT id FROM states WHERE name = %s
                         )
                         ORDER BY cities.id''', (sys.argv[4],))

            # printing results
            sorted_list = []
            for row in cur.fetchall():
                if row[0] not in sorted_list:
                    sorted_list.append(row[0])
            print(*sorted_list)

    except MySQLdb.Error as e:
        pass
