#!/usr/bin/python

import cgi
# to facilitate debugging
import cgitb
cgitb.enable()

#connect database
import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()

#Cookie
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
		print "Content-type: text/html"
		# don't forget the extra newline!
		print
		print "<h1>Welcome again!!! "+back_username+"</h1>"
	else:
		print "Content-type: text/html"
		print
		print "<html>"
		print "<body>"
		print "<h1>you already logged out.</h1>"
		print "</body>"
		print "</html>"
else :	
	print "Content-type: text/html"
	# don't forget the extra newline!
	print
	print "Cookie"
