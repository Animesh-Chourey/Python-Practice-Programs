from django.shortcuts import render,redirect
from django.http import HttpResponse
import MySQLdb

# Create your views here.

def showIndex(req):
	return render(req,"Index.html")

def showIns(req):
	return render(req,"InsertData.html")

def InsertData(req):
	ename=req.GET['name']
	edesig=req.GET['desig']
	esalary=req.GET['salary']
	esalary=int(esalary)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","python_practice")
	cursor=conn.cursor()
	query="insert into Employee(Emp_name,Emp_desig,Emp_sal) values ('{}','{}',{})".format(ename,edesig,esalary)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()
	return redirect("/showData")

def showData(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","python_practice")
	cursor=conn.cursor()
	query="select * from Employee"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"ViewData.html",{"data":data})

def showUpdate(req):
	eid=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","python_practice")
	cursor=conn.cursor()
	query="select * from Employee where Emp_id={}".format(eid)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"Update.html",{'record':row})

def UpdateData(req):
	eid=req.GET['empid']
	ename=req.GET['name']
	edesig=req.GET['desig']
	esalary=req.GET['salary']
	esalary=int(esalary)
	eid=int(eid)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","python_practice")
	cursor=conn.cursor()
	query="update Employee set Emp_name='{}',Emp_desig='{}',Emp_sal={} where Emp_id={}".format(ename,edesig,esalary,eid)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showData")

def deleteData(req):
	eid=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","python_practice")
	cursor=conn.cursor()
	query="delete from Employee where Emp_id={}".format(eid)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showData")
def jsDemo(req):
	return render(req,"JSdemo.html")