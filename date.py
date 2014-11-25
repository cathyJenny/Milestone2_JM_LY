#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()

import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()

form = cgi.FieldStorage()
my_name = form['name'].value
my_date = form['date'].value
c.execute('select * from date where name=? AND date=?', (my_name,my_date),) 
all_results = c. fetchall()

if len(all_results) > 0:
	all_r=all_results[0][3]
	all_c=all_r.split(',')
	count=len(all_c)
	i=0
	while count>0 :
		al_c=all_c[i]
		if i==0 :
			i=i+1
			count=count-1
			print "Content-type: text/html"
			print 
			print "<h1>Time Slot for "+my_date+"</h1>"
			print "<h2><li> "+al_c+"</li></h2>"
		else :
			i=i+1
			count=count-1
			print "<h2><li>"+al_c+"</li></h2>"
