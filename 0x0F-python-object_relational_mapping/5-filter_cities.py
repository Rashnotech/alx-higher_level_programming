#!/usr/bin/python3
""" a script that lists all cities from the database """

import MySQLdb
import sys


if __name__ == '__main__':
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_pass,
                         db=my_db)
    cur = db.cursor()
    cur.execute('SELECT name FROM cities\
            WHERE state_id = (SELECT id FROM states\
            WHERE name = %s) ORDER BY id ASC', (search,))
    cities = cur.fetchall()
    for city, in cities:
        print(city, end=", ")
    print()
