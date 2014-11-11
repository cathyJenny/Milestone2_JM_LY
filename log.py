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

form = cgi.FieldStorage()
my_email = form['email'].value
my_pw = form['password'].value
c.execute('select * from user where email=?',(my_email,))
all_results = c.fetchall()
if len(all_results) > 0:
	real_pw = all_results[0][1]
	# pw is correct
	if real_pw == my_pw:
		exist_name = all_results[0][0]
		import uuid
		session = str(uuid.uuid4())
		c.execute('update user set sessionID = ? where email = ?', (session, my_email))
		conn.commit()
		coo = Cookie.SimpleCookie()
		coo['session'] = session
		print "Content-type: text/html"
		print coo
		print
		print "<h1>Welcome " + exist_name + "</h1>"
		# pw incorrect
	else:
		print "Content-type: text/html"
		print
		print "wrong password. Try again."
		# new user
else:
	print "Content-type: text/html"
	print
	print "you are not registered yet. Do you want to register now?"
