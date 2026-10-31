from django.contrib import admin
from django.urls import path 
from app2.views import app2hifunction , app2byefunction

urlpatterns = [
  path('app2hi/',app2hifunction,{'status':'Ok'},name="HiFunctionApp2"),
  path('app2bye/',app2byefunction,name="ByeFunctionApp2")
  
]