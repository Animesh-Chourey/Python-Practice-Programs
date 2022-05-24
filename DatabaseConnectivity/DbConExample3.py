#Update Query
import MySQLdb

conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()

snm=input("Enter Student's Name: ")
sid=int(input("Enter Student's Id: "))

#Execute Query
query="update Student set S_id=%d where S_name='%s'"%(sid,snm)
cursor.execute(query)

#Save Data
conn.commit()
print("Data Saved")

#Close Resources
cursor.close()
conn.close()