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
	form = cgi.FieldStorage()
	my_usern = form['usrn'].value
	my_pw = form['pw'].value
	my_zc = form['zip'].value
	my_occu = form['occ'].value
	my_pref = form['preference'].value
	coo = Cookie.SimpleCookie(exist_cookie)
	session_ID = coo['session'].value
	c.execute('select * from user where sessionID = ?', (session_ID,))
	all_results = c. fetchall()
	# find the right name
	if len(all_results) > 0:
		back_email = all_results[0][2]

		#info from table user
		c.execute('select * from user where email = ?', (back_email,))
		all_content=c.fetchall()
		back_Name=all_content[0][0]
		back_pw=all_content[0][1]

		#info from favor table
		c.execute('select * from favor where email = ?', (back_email,))
		all_contentF=c.fetchall()
		back_zip=all_contentF[0][1]
		back_occ=all_contentF[0][2]
		back_pre=all_contentF[0][3]
		
		if back_Name !=my_usern :
			c.execute('update user set name= ? where email = ?',(my_usern, back_email))
			conn.commit()
			print "Content-type: text/html"
			print
			print "<h1>Your username information has been updated to \""+my_usern+"\"</h1>"
	 	if back_pw !=my_pw :
	 		c.execute('update user set password= ? where email = ?',(my_pw, back_email))
	 		conn.commit()		
			print
			print "<h1>Your password information has been updated!</h1>"
		if back_occ !=my_occu :
		 	c.execute('update favor set occupation= ? where email = ?',(my_occu, back_email))
		 	conn.commit()
			print
			print "<h1>Your occupation information has been updated to \""+my_occu+"\"</h1>"
		if back_pre !=my_pref :
			c.execute('update favor set preference= ? where email = ?',(my_pref, back_email))
			conn.commit()
			print
			print "<h1>Your preference information has been updated to \""+my_pref+"\"</h1>"
		if back_zip !=my_zc :
		 	c.execute('update favor set zc= ? where email = ?',(my_zc, back_email))
		 	conn.commit()
			print
			print "<h1>Your zipCode information has been updated to \""+my_zc+"\"</h1>"		
	# cookie does not exist
	else:
		print "Content-type: text/html"
		print
		print "You haven't Logged in"
