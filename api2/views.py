from django.contrib.auth.models import User, Post
from django.shortcuts import render
from rest_framework import viewsets
from api2.serializers import UserSerializer, PostSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer