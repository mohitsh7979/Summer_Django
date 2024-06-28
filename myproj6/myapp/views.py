from django.shortcuts import render,HttpResponse,redirect
from .models import Information
from .forms import SinupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

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


def signuphandle(request):
    if request.method == "POST":
        form = SinupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
                                  
            if User.objects.filter(username=username).first():
                messages.success(request,'This is username is already taken !!')
            
            elif User.objects.filter(email=email).first():
                messages.success(request,'This email is already taken !!')
            
            elif password != confirm_password:
                messages.success(request,'Both password field should be same')
            
            else:
                user = User(username=username,email=email)
                user.set_password(password)
                user.save()
                messages.success(request,'Account Successfully Created !!')
                return redirect('/signup/')
    form = SinupForm()
    context = {
        'form':form
    }
    return render(request,'Signup.html',context)

def loginhandle(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.success(request,'Wrong Password')
            
    form = LoginForm()
    return render(request,'Login.html',{'form':form})


def logouthandle(request):
    logout(request)
    return redirect('/login/')


