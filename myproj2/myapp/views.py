from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'Home.html')

def blog(request):
    return render(request,'Blog.html')


def about(request):
    return render(request,'About.html')
