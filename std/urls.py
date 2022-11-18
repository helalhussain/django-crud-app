from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [

    path('',views.home),
    path('add-std/',views.add_std),
    path('delete-std/<int:roll>',views.delete_std),
    path('edit-std/<int:roll>',views.update_std),
    path('do-edit-std/<int:roll',views.do_edit),
    
]
