from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)


class Order(models.Model):
    customer = models.IntegerField()
    items = models.CharField(max_length=200)
    totalamount = models.FloatField()
    orderdate = models.DateField()