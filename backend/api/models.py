from django.utils import timezone 
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    detaildescription = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.IntegerField()
    img = models.CharField(max_length=100)
    def __str__(self):
        return self.description


class CartItem(models.Model):
    # customer_id= models.IntegerField()
    product_id = models.IntegerField()
    buyer_name=models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    contact=models.IntegerField()
    address=models.CharField(max_length=255,default='N/A')
    time=models.DateTimeField( default=timezone.now)

class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name