from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Profile

# Create your views here.
def HellowApp1(request):
    return HttpResponse("Hello app 1 message one")

def WelcomeApp1(request):
    return HttpResponse("Hellow welcome app 1")

def loginPage(request):
    return render(request,'app1/login.html')

def registration(request):
    return render(request,'app1/registration.html')


def profileDetails(request):
    profile_details = Profile.objects.all()
    print(profile_details)
    return render(request,'app1/profile.html')

def fetchSingleProfile(request):
    # single_data = Profile.objects.get()
    # print(single_data)
    return render(request,'app1/profile.html')