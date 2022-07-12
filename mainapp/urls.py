from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartProductViewSet, CartViewSet, CustomerViewSet, CategoryViewSet
router = DefaultRouter()
router.register('customer', CustomerViewSet)
router.register('category', CategoryViewSet)
router.register('cart', CartViewSet)
router.register('cartProduct', CartProductViewSet)
router.register('product', ProductViewSet)

urlpatterns = router.urls