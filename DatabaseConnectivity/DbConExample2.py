#Insert query by taking the data from user
import MySQLdb

#Establish Connection
conn=MySQLdb.connect("localhost","root","animeshroot@123","PythonPractice")

#Create Cursor
cursor=conn.cursor()

sid=int(input("Enter Student's Id: "))
snm=input("Enter Student's Name: ")
sage=int(input("Enter Student's Age: "))
smarks=int(input("Enter Student's Marks: "))
saddr=input("Enter Student's Address: ")

#Execute Query
query="insert into Student values(%d,'%s',%d,%d,'%s')"%(sid,snm,sage,smarks,saddr)
cursor.execute(query)

#Save Data
conn.commit()
print("Data Saved")

#Close Resources
cursor.close()
conn.close()