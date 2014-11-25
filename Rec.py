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

import urllib

def checkMovie(back_name):
	if(back_name == "Hunger Game.html"):
		# print "Content-type: text/html"
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Hunger Game.html">
		<img src="/Hunger-Game-Mockingjay.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Hobbit.html"):	
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Hobbit.html">
		<img src="/hobbit-battle-five-armies.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if (back_name == "Train Dragons.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Train Dragons.html">
		<img src="/train-dragon.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Transformer.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Transformer.html">
		<img src="/transformer.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Big.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Big.html">
		<img src="/Big-Hero.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "ImitationGame.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/ImitationGame.html">
		<img src="/imiposter.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Gambler.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Gambler.html">
		<img src="/Gambler.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Dumb.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Dumb.html">
		<img src="/Dumb.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Kings.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Kings.html">
		<img src="/King.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Annie.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Annie.html">
		<img src="/Annie.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Night.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Night.html">
		<img src="/Night.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""
	if(back_name == "Ame.html"):
		print
		print """ 
		<html>
		<body>
		<a href="http://jmao6.rochestercs.org/Ame.html">
		<img src="/Am.jpg" width = "150" height = "170">
		</a>
		</body>
		</html>"""

def movieType(back_pre):
	c.execute('select * from movie where type= ?', (back_pre,))
	results3 =c.fetchall()
	print """ 
		<html>
		<body>
		<font size = 5><em>These are the movies that fit your movie type: """ + back_pre + """</em></font><br/>
		</body>
		</html>"""
	if len(results3) > 0:
		count = 0
	 	while(count < len(results3)):
	 		back_name=results3[count][1]
			count = count+1
			checkMovie(back_name)

if exist_cookie:
	coo = Cookie.SimpleCookie(exist_cookie)
	session_ID = coo['session'].value
	c.execute('select * from user where sessionID = ?', (session_ID,))
	all_results = c.fetchall()
	if len(all_results) > 0:
	 	back_email = all_results[0][2]
	 	c.execute('select * from favor where email = ?', (back_email,))
		all_results2=c.fetchall()
	 	if len(all_results2) > 0:
	 		back_pre=all_results2[0][3]
	 		print "Content-type: text/html"
			print
	 		movieType(back_pre)
	 		print """
	 		<html>
	 		<body>
	 		<form method='GET' action='http://jmao6.rochestercs.org/index.html'><input type='submit' id='Home' value='HomePage'></input> </form>
	 		</body>
	 		</html>"""
