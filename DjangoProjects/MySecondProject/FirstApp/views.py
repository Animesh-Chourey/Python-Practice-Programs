from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_view(request):
	return HttpResponse("<h2> First App Demo of second project </h2>")

def f_view(request):
	return HttpResponse("<h2> Call at browser loading </h2>")