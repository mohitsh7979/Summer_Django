from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    FEATURED_PRODUCT = Product.objects.filter(category="FEATUREDPRODUCT")
    NEW_PRODUCT = Product.objects.filter(category="NEWPRODUCTS")
    
    context = {'FEATURED_PRODUCT':FEATURED_PRODUCT,'NEW_PRODUCT':NEW_PRODUCT}
    
    return render(request,'Home.html',context)

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')
