from django.shortcuts import render,HttpResponse

# Create your views here.


def Output(request):
    return HttpResponse("Hello Django World !!!")
    
def name(request):
    return HttpResponse("Hello Mohit")