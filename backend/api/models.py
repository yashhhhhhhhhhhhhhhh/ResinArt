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
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
