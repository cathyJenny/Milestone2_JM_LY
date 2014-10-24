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
		print "Content-type: text/html"
		print
		print "<html>"
		print "<body>"
		print "<h1>Welcome again, " + back_username + "</h1>"
		print "<form action='logout.py'><input type='submit' value='logout'/></form>"
		print "</body>"
		print "</html>"
		
	else:
		print "Content-type: text/html"
		print
		print "<html>"
		print "<body>"
		print "<h1>you already logged out.</h1>"
		print "</body>"
		print "</html>"
else:
	form = cgi.FieldStorage()
	my_email = form['email'].value
	my_usern = form['usrn'].value
	my_pw = form['pw'].value
	my_zc = form['zip'].value
	my_occu = form['occ'].value
	my_pref = form['preference'].value

	import uuid
	session = str(uuid.uuid4())
	# to check if the username is already in the database
	c.execute('select * from user where email = ?', (my_email,))
	all_results = c.fetchall()
	if len(all_results) > 0:
		c.execute('update user set sessionID = ? where email = ?',(session, my_email))
		conn.commit()
		coo = Cookie.SimpleCookie()
		coo['session'] = session
		print "Content-type: text/html"
		print coo
		print
		print "<html>"
		print "<body>"
		print "<h1>"+ my_usern + ", you already registered.</h1>"
		#Log in Button
		print "<form action='login.py'><input type='submit' value='Login'/></form>"
		print "</body>"
		print "</html>"
	else:
		#insert value to two tables
		try:		
			c.execute('insert into favor values (?, ?, ?, ?);',(my_email, my_zc, my_occu, my_pref))
			c.execute('insert into user values (?, ?, ?, ?);', (my_usern, my_pw, my_email, session))		
			conn.commit()

		except sqlite3.IntegrityError:
			pass
		
		coo = Cookie.SimpleCookie()
		coo['session'] = session

		print "Content-type: text/html"
		print coo
		print
		print "<html>"
		print "<body>"
		print "<h1>Welcome "+ my_usern+"</h1>" 
		#Log Out Button
		print "<form action='logout.py'><input type='submit' value='Logout'/></form>"
		print "</body>"
		print "</html>"
