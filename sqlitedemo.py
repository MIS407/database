__author__ = 'Sree'
import sqlite3 

conn = sqlite3.connect('sn.sqlite') 
cursor = conn.cursor() 

# Connect to database sn and set up a cursor

# (C)reate a new blog post 

cursor.execute('insert into Posts (Headline, Body) values (?, ?)', ('This is my Headline', 'This is the body of my blog post.')) 
firstPostId = cursor.lastrowid 

cursor.execute('insert into Posts (Headline, Body) values (?, ?)', ('Jet Fuel XBold Coffee', 'Jet Fuel XBold Dark Roast Coffee will make you code like a madman.')) 

conn.commit() 

# (R)ead our new posts 

cursor.execute('select * from Posts') 
print('Current records: ') 

for row in cursor.fetchall(): 
	print('\t', row) 

# (U)pdate the first post 

cursor.execute('update Posts set Headline=?, Body=? where Id=?', ('This is my NEW Headline', 'This is the NEW body of my blog post.', firstPostId)) 
conn.commit() 

print('Records after update: ') 
cursor.execute('select * from Posts') 

for row in cursor.fetchall(): 
	print('\t', row) 

# (D)elete all the records 

cursor.execute('delete from Posts') 
print('Records after delete: ') 

cursor.execute('select * from Posts') 

for row in cursor.fetchall(): 
	print('\t', row) 

conn.commit() 

cursor.close() 

conn.close() - See more at: http://codecr.am/blog/post/3/#sthash.I1U8Y1Ob.dpuf