#!/usr/bin/python3
""" a script that takes an argument and display all values """

import sys
import MySQLdb


if __name__ == '__main__':
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_pass,
                         db=my_db)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        if state[1] == search:
            print(state)
