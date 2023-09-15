#!/usr/bin/python3
""" a script that lists all cities from the database """

import MySQLdb
import sys


if __name__ == '__main__':
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_pass,
                         db=my_db)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON states.id=cities.state_id ORDER BY cities.id ASC')
    cities = cur.fetchall()
    for city in cities:
        print(city)
