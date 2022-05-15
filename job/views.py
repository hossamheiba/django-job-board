from django.shortcuts import render
from django.http import HttpResponse  
# Create your views here.
def job(requset):
    return HttpResponse("job")