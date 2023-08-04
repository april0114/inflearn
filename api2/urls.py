from django.urls import path, include
from rest_framework import routers
from api2.views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

]