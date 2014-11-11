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
		useremail=all_results[0][2]
		c.execute('delete from user where email = ?',(useremail,))
		c.execute('delete from favor where email = ?',(useremail,))
		conn.commit()
		coo['session']['expires']='Tue, 07 Oct 2014 00:00:00 GMT'
		print "Content-type: text/html"
		print coo
		print
		print "<h1>You already delete your account.</h1>"
		
else:
	print "Content-type: text/html"
	print
	print "<h1>You already logout. Can not delete account when you logout</h1>"
	
