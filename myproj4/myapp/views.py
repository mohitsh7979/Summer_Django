from django.shortcuts import render,HttpResponse,redirect
from .models import Student

# Create your views here.

def index(request):
    if request.method == "POST":
        user_name = request.POST['uname']
        user_email = request.POST['uemail']
        user_age = request.POST['uage']
        user_address = request.POST['address']
        user_mobile = request.POST['mobile']
        user_dob = request.POST['dob']
        Student(name=user_name,email=user_email,age=user_age,address=user_address,mobile=user_mobile,dob=user_dob).save()
        return redirect('/table/')
       
    return render(request,'Form.html')

def Table(request):
    data = Student.objects.all()
    context = {
        
        'Data':data
    }
    # for i in data:
    #     print(i.id,i.name,i.email,i.age)
    return render(request,'Table.html',context)

def deletehandle(request,id):   
    data = Student.objects.filter(id=id)
    data.delete()
    return redirect('/table/')
    
    
