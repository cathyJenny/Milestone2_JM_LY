#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import sqlite3
conn = sqlite3.connect('/home2/jmaosixr/users.db')
c = conn.cursor()

form = cgi.FieldStorage()
nickname = form['NickName'].value
comments = form['comment'].value
cinema = form['theater'].value
city = form['city'].value

string = nickname +" just comments: \""+comments+"\" at "+cinema+" in "+city+"\n"

c.execute('select * from comment where name=? AND comment = ? AND cinema=?', (nickname, comments, cinema))
all_results = c.fetchall()

if len(all_results)==0 :
	try:
		c.execute('insert into comment values(?,?,?);', (nickname, comments,cinema))
		conn.commit()
	except sqlite3.IntegrityError:
		pass

print "Content-type:text/html"
print
print string
	

