from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student

def home(request):
    std=Student.objects.all()
    return render(request,'std/home.html',{'std':std})
    
def add_std(request):
    if request.method=='POST':
        print("Added")
        stds_roll = request.POST.get("std_roll")
        stds_name = request.POST.get("std_name")
        stds_email = request.POST.get("std_email")
        stds_address = request.POST.get("std_address")
        stds_phone = request.POST.get("std_phone")

        s=Student()
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.address=stds_address
        s.phone=stds_phone
        s.save()
        return redirect('/std/home')



    return render(request,'std/add_std.html', {})
