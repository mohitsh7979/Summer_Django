from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Form.html')

def Table(request):
    return render(request,'Table.html')
