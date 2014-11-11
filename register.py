#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()
import Cookie
import os
exist_cookie = os.environ.get('HTTP_COOKIE')
#cookie exists
if exist_cookie:
	coo = Cookie.SimpleCookie(exist_cookie)
	session_ID = coo['session'].value
	c.execute('select * from user where sessionID = ?', (session_ID,))
	all_results = c. fetchall()
	# find the right name
	if len(all_results) > 0:
		name = all_results[0][0]
		print "Content-type: text/html"
		print
		print "<h1>Welcome again "+ name +"</h1>" 
		
# cookie does not exist
else:
	print "Content-type: text/html"
	print
	print "Cookie"
