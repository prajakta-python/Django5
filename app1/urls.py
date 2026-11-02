from django.contrib import admin
from django.urls import path
from app1.views import HellowApp1 , WelcomeApp1 , loginPage , registration , profileDetails ,fetchSingleProfile

urlpatterns = [
    path('app1hellofunction/',HellowApp1,name="HelloFunction"),
    path('app1welcomefunction/',WelcomeApp1,name="welcomeFunction"),
    path('login/',loginPage,name="LoginPage"),
    path('register/',registration,name="REgistrationPage"),
    path('profileDetails/',profileDetails,name="ProfileDetails"),
    path('fetchSingleProfile/',fetchSingleProfile,name="SingleProfile")

]
