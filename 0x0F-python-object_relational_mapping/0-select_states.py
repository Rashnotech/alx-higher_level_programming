#!/usr/bin/python3
""" a module that list all states from database """
import sys
import MySQLdb


if __name__ == '__main__':
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=my_user, passwd=my_pass,
                         db=my_db)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        print(state)
