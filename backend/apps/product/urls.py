from django.conf.urls import url, inclue
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products' ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]