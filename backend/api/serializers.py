from rest_framework import serializers
from .models import Product,CartItem,Signup,Contact
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','type','price','description','detaildescription','rating','review','img',]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_id','buyer_name', 'product_name', 'quantity','subtotal','contact','address','time']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signup
        fields=['name', 'email', 'password']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']