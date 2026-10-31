from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HellowApp1(request):
    return HttpResponse("Hello app 1 message one")

def WelcomeApp1(request):
    return HttpResponse("Hellow welcome app 1")

def loginPage(request):
    return render(request,'app1/login.html')

def registration(request):
    return render(request,'app1/registration.html')