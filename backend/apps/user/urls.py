from django.conf.urls import url, include
from rest_framework import routers
from .views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'users', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
