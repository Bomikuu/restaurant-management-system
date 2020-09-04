from django.conf.urls import url, include
from rest_framework import routers
from .views import AccountViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', AccountViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
