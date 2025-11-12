from rest_framework import routers
from products.views import ProductViewSet
from orders.views import OrderViewSet
from users.views import UserViewSet

from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet

router = DefaultRouter()

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', UserViewSet)
