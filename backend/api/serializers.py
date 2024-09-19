from rest_framework import serializers
from .models import Product,CartItem
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','type','price','description','detaildescription','rating','review','img',]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_id', 'product_name', 'quantity','subtotal','time']