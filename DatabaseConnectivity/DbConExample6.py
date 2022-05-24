#Select Query
#fetchone() method

import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()

#Execute Query
query="select * from Student"
cursor.execute(query)

#Fetch Data
data=cursor.fetchone()
print("Data: ",data)

#Close Resorces
cursor.close()
conn.close()