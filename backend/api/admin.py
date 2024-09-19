from django.contrib import admin
from .models import Product,CartItem
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','type','price','description','detaildescription','rating','review','img']

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','quantity','price','subtotal']
