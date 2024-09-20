from django.contrib import admin
from .models import Product,CartItem,Signup,Contact
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','type','price','description','detaildescription','rating','review','img']

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display=['product_id','buyer_name','product_name','quantity','subtotal','contact','address','time']
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'message']
