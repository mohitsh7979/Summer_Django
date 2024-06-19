from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()

