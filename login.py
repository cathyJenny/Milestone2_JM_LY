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

# check if cookie exists
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

# ///////////////////////////////////////////////
# ///// 	# print "<form action=/logout.py><input type='submit' value='logout'/></form>"
# //////////////////////////////////////////////
		
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
#cookie does not exist
else:
	form = cgi.FieldStorage()
	my_email = form['email'].value
	my_pw = form['pw'].value
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
			print "<html>"
			print "<body>"
			print "<h1>Welcome " + exist_name + "</h1>"

# ///////////////////////////////////////////////
# /////		# print "<form action=/logout.py><input type='submit' value='logout'/></form>"
# ///////////////////////////////////////////////

			print "</body>"
			print "</html>"
		# pw incorrect
		else:
			print "Content-type: text/html"
			print
			print "<html>"
			print "<body>"
			print "wrong password. Try again."
			print "<form action=/login.html><input type='submit' value='login again'/></form>"
			print "</body>"
			print "</html>"

	# new user
	else:
		print "Content-type: text/html"
		print
		print "<html>"
		print "<body>"
		print "<h1>you are not registered yet. Do you want to register now?</h1>"
		print "<form action=/register.html><input type='submit' value='register'/></form>"
		print "</body>"
		print "</html>"
