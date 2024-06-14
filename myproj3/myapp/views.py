from django.shortcuts import render,HttpResponse
from .models import Student
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == "POST":
        user_name = request.POST['uname']
        user_email = request.POST['uemail']
        user_age = request.POST['uage']
        user_address = request.POST['uaddress']
        user_mobile = request.POST['umobile']
        user_date = request.POST['udate']
        Student(name=user_name,email=user_email,age=user_age,address=user_address,mobile=user_mobile,date=user_date).save()
        messages.success(request,'Data Successfully add !!!')
        
    return render(request,'index.html')
