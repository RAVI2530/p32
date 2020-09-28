from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

def filter_demo(request):
    return render(request,"filter_demo.html",{'data':"python Django class",'a':1000,'b':999,'num':999})