#Delete Query

import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()
sid=int(input("Enter Student's Id: "))

#Execute Query
query="delete from Student where S_id=%d"%(sid)
cursor.execute(query)

#Save Data
conn.commit()
print("Table Changed")

#Close Resorces
cursor.close()
conn.close()