from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'form.html')

def Data(request):
    return render(request,'table.html')
