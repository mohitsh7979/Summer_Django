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

def product_detail(request,id):
    filter_product = Product.objects.get(id=id)
    context = {
        
        'product':filter_product
    }
    return render(request,'single-product.html',context)

def shop_category(request):
    product = Product.objects.all()
    return render(request,'category.html')


def add_to_cart(request,id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        user = request.user 
        quantity = request.POST['myquantity']
        print(quantity,"quantity")
        AddToCart(user=user,product=product,quantity=quantity).save()
    
    data = AddToCart.objects.filter(user=request.user)
    print(data)
    return render(request,'cart.html',{'data':data})

def checkout(request):
    return render(request,'checkout.html')
