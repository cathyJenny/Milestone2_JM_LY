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

if exist_cookie:
	coo = Cookie.SimpleCookie(exist_cookie)
 	session_ID = coo['session'].value
 	c.execute('select * from user where sessionID = ?', (session_ID,))
 	all_results = c.fetchall()
 	if len(all_results) > 0:
		back_username = all_results[0][0]
		coo['session']['expires']='Tue, 07 Oct 2014 00:00:00 GMT'
		print "Content-type: text/html"
		print coo
		print
		print "<html>"
		print "<body>"
		print "<h1>Logout</h1>"
		print "<form action=/index.html><input type='submit' value='Go Back To Home Page'/></form>"
		print "</body>"
		print "</html>"
 	else:
		pass
else:
	print "Content-type: text/html"
	print
	print "<html>"
	print "<body>"
	print "<h1>You haven't logged in</h1>"
	print "</body>"
	print "</html>"



























