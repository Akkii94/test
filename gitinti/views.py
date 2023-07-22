from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(r):
    return HttpResponse('<h1>this is home page</h1>')
