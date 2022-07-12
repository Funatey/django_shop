from django.contrib import admin
from .models import Cart, CartProduct, Customer, Category, Product

admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Product)
# Register your models here.
