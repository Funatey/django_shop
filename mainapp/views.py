from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartProduct, Customer, Category, Product
from .serializer import CategorySerializer, CartSerializer, CartProductSerializer, CustomerSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
