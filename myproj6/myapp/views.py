from django.shortcuts import render,HttpResponse,redirect
from .models import Information

# Create your views here.

def getform(request):
    if request.method == "POST":
        user_name = request.POST['username']
        user_email = request.POST['useremail']
        user_age = request.POST['userage']  
        Information(name=user_name,email=user_email,age=user_age).save()
        return redirect('/data/') 
    return render(request,'form.html')

def getdata(request):
    data = Information.objects.all()  # orm query for getting all from database
    context = {
        
        'mydata':data,
    }
    return render(request,'data.html',context)

def deletehandle(request,id):     
    # data = Information.objects.filter(id=id)
    data = Information.objects.get(id=id)
    data.delete()
    return redirect('/data/')

def updatehandle(request,id):
    data = Information.objects.get(id=id)
    if request.method == "POST":
        data.name = request.POST['username']
        data.email = request.POST['useremail']
        data.age = request.POST['userage']
        data.save()
        return redirect('/data/')
    print(data)
    context = {
        'data':data
    }
    return render(request,'update.html',context)


# curd 

# create update read delete 