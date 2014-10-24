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
#cookie does not exist
else:
	 print "Content-type: text/html"
	 print
	 print """ 
	 <html> 
	 <head>
	 <title> Login </title>
	 </head>
	 <body> 

	 <form method="POST" action="log.py"> 
	 <h1> Enter your info to log in:</h1>
	 Email: <input name="email" type=text size=30/><br></br>
	 Password:<input name="pw" type="password" size=30/><br></br>
	 <input type="submit"/><input type="reset"/>
	 </form>
	 </body>
	 </html> """
