#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()

form = cgi.FieldStorage()
cinema = form['name'].value

c.execute('select * from comment where cinema=?', (cinema,)) 
all_results = c. fetchall()

if len(all_results) > 0:
	count = 0
	while(count < len(all_results)):
		all_n=all_results[count][0]
		all_c=all_results[count][1]
		count = count+1
		if(count == 1):
			print "Content-type:text/html"
			print
			print '<li>'+all_n+" says: "+all_c+'</li>'
		else:
			print '<li>'+all_n+" says: "+all_c+'</li>'
else:
	print "Content-type:text/html"
	print
	print '<li>'+"No comments yet."+'</li>'
