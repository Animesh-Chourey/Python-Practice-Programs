#Select Query 
#Printing data one bye one

import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()

#Execute Query
query="select * from Student"
cursor.execute(query)

#Fetch Data
data=cursor.fetchall()
for row in data:
	#for col in row:
		print(row,end="\t")

#Close Resorces
cursor.close()
conn.close()