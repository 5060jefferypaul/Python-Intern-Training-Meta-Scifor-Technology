from django.shortcuts import render
from django.http import HttpResponse


#Create your views here.

def members(request):
    return render(request,'Portfolio.html')