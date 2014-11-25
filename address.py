#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()

import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()
form = cgi.FieldStorage()
my_name=form['name'].value

c.execute('select * from address where name = ?', (my_name,))
all_results = c.fetchall()

if len(all_results) > 0:
	print "Content-type: text/html"
	print
	print all_results[0][1]	

