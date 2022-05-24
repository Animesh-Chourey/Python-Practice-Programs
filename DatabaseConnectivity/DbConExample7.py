#Select Query
#fetchone() & fetchall() method used together at different scenarios

import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()

#Execute Query
query="select * from Student"
cursor.execute(query)

#Fetch Data
'''
print("fetchone() used before fetchall()") 
data=cursor.fetchone()
print("Data: ",data)
data=cursor.fetchall()
print("Data: ",data)
'''
print("fetchone() used after fetchall()") 
data=cursor.fetchall()
print("Data: ",data)
data=cursor.fetchone()
print("Data: ",data)

#Close Resorces
cursor.close()
conn.close()