from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2hifunction(request,**kwargs):
    status = kwargs.get('status')
    return HttpResponse(f"This app 2 hi function {status}")

def app2byefunction(request):
    return HttpResponse("This is Bye to app 2 function")