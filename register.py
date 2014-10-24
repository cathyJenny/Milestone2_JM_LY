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
		print "<html>"
		print "<body>"
		print "<h1>Welcome again "+ name +"</h1>" 
		#Log Out Button
		print "<form action='logout.py'><input type='submit' value='Logout'/></form>"
		print "</body>"
		print "</html>"
# cookie does not exist
else:
	print "Content-type: text/html"
	print
	print """
	<html>
	<head>
	<title> Register </title>
	</head>
	<body>

	<form method="POST" action="reg.py">
	Username: 
	<input name="usrn" type=text size=30 required>
	<br></br>
	Password:
	<input name="pw" type="password" size=30 required>
	<br></br>
	E-mail:
	<input name="email" type=text size=30 required>
	<br></br>
	Zip code:
	<input name="zip" type=text size=30 required>
	<br></br>
	Occuaption:<br/>
	<input  name="occ" type="radio" value="student" required> Student
	<input  name="occ" type="radio" value="other" required> Other <br/>
	<br/>
	Preference:<br/>
	<input  name="preference" type="radio" value="action"> Action <br/>
	<input  name="preference" type="radio" value="advanture"> Advanture <br/>
	<input  name="preference" type="radio" value="comedy"> Comedy <br/>
	<input  name="preference" type="radio" value="docum"> Documentary <br/>
	<input  name="preference" type="radio" value="fantacy"> Fantacy <br/>
	<input  name="preference" type="radio" value="honor"> Horror <br/>
	<input  name="preference" type="radio" value="romance"> Romance <br/>
	<br></br>
	<input type="submit"/><input type="reset"/>
	</form>
	</body>
	</html> """
