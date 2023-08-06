# from django.contrib.auth.models import User
# from django.shortcuts import render

# from rest_framework import viewsets
# from api2.serializers import UserSerializer, PostSerializer, CommentSerializer
# from blog.models import Post, Comment

# # Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from blog.models import Post, Comment
from django.contrib.auth.models import User

from api2.serializers import CommentSerializer, UserSerializer, PostRetrieveSerializer, PostListSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer