from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [

    path('home/',views.home),
    path('add-std/',views.add_std),
    
]
