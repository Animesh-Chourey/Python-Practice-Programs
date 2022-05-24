#insert query
import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")
print("Connection Established")

#Create Cursor
cursor=conn.cursor()
print("Cursor Created")

#Execute Query
query="insert into Student values(20,'Rishabh',21,90,'Chitrakoot')"
row=cursor.execute(query)

#Save Data
conn.commit()
print("Data Inserted in ",row)

#Close Resources
cursor.close()
conn.close()