#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # connect
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argvs

	cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC
    	""", (sys.argv[4],))

    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    cur.close()
    db.close()
