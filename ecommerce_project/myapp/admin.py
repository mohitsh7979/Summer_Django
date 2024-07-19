from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','description','size','category','image']
    
    
@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
