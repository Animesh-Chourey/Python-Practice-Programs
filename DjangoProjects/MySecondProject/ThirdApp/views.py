from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime

# Create your views here.
def tempDemo(request):
	temp=loader.get_template('index.html')#here no data is being rendered with the index file so nothing will be displayed in the response in browsing page
	return HttpResponse(temp.render)

def dateDemo(req):
	today=datetime.datetime.now().date()
	temp=loader.get_template('index.html')
	return HttpResponse(temp.render({'d':today}))

def loopDemo(req):
	temp=loader.get_template("index.html")
	return HttpResponse(temp.render({'table':[2,4,6,8]}))

def dictDemo(req):
	return render(req,"Test.html",{'a':23,'b':[1,2,3,4],'c':"Hello"})

def ifDemo(req):
	today=datetime.datetime.now().date()
	temp=loader.get_template("IfTest.html")
	return HttpResponse(temp.render({'a':10,'b':10}))

def maxDemo(req):
	temp=loader.get_template("maxDemo.html")
	return HttpResponse(temp.render({'x':23,'y':13}))

def dictTest(req):
	d={1:"Hello",2:"Python",3:"JAVA",4:"C",5:"Android"}
	return render(req,"dictTest.html",{"data":d})