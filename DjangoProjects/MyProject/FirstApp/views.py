from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
	return HttpResponse("<h1>Hello My First Application</h1>")

def sum(request):
	a,b=10,34
	c=a+b
	return HttpResponse("<h3> Sum is ={}</h3>".format(c))

def diff(request):
	a,b=34,10
	c=a-b
	return HttpResponse("<h3> Difference is ={}</h3>".format(c))