from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sec_view(request):
	return HttpResponse("<h2> Sec App Demo</h2>")

def sum(request,a,b):
	c=a+b
	return HttpResponse("<h2>Sum is= {}</h2>".format(c))

def show(request,fname,lname):
	name=fname+" "+lname
	return HttpResponse("<h2>Name: {}</h2>".format(name))

def queryStr(request):
	name=request.GET['name']
	return HttpResponse("<h1> Name: {}</h1>".format(name))

def query_P_Str(request):
	name=request.GET['name']
	passw=request.GET['pass']
	return HttpResponse("<h1> Name: {} <br> Password: {} </h1>".format(name,passw))