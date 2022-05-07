from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index, name='home'),
    path("feedback",views.feedback, name='feedback'),
    path("FullstackDeveloper",views.FullstackDeveloper, name='FullstackDeveloper'),
    path("Redux",views.Redux, name='Redux'),
    path("SoftwareDeveloper",views.SoftwareDeveloper, name='SoftwareDeveloper'),
    path("DjangoDeveloper",views.DjangoDeveloper, name='DjangoDeveloper'),
    path("DataScientist",views.DataScientist, name='DataScientist'),
    path("FlutterDeveloper",views.FlutterDeveloper, name='FlutterDeveloper'),
    path("Profile",views.Profile, name='Profile'),
    
    
]