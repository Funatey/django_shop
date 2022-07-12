from rest_framework import serializers
from .models import Product, CartProduct, Cart, Category, Customer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'slug', 'image', 'description', 'price')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'owner', 'products', 'total_products', 'final_price', 'in_order', 'for_anonimous_user')

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'user', 'cart', 'product', 'qty', 'final_price')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'user', 'phone', 'address')