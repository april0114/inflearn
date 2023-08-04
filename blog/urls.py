from django.urls import path
from blog import views


app_name ='blog'
urlpattern =[
    path('post/<int:pk>/', views.PostDetailTV.as_view(), name = 'post_detail'),
]