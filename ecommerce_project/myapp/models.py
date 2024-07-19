from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRODUCT_CATEGORY = [
    
    ("men","men"),
    ("women","women"),
    ("kids","kids"),
    ("FEATUREDPRODUCT","FEATUREDPRODUCT"),
    ("NEWPRODUCTS","NEWPRODUCTS"),
    ("INSPIREDPRODUCTS","INSPIREDPRODUCTS")
]

PRODUCT_SIZE = [
    
    ('S','S'),
    ('M','M'),
    ('XL','Xl'),
    ('XXL','XXL')
]


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    size = models.CharField(choices=PRODUCT_SIZE,max_length=50)
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=50)
    image = models.ImageField(upload_to='media')
    
    
    def __str__(self):
        return self.title
        
        

class AddToCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    