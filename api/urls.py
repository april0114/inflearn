from django.urls import path
from api import views

app_name = 'api'
urlpatterns =[
    path('post/list/',  views.ApiPostLV.as_View(), name ='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name ='post-deatil'),
    path('catetag/', views.ApiCateTagView.as_view(), name ='catetag_list'),
    path('like/<int:pk>/', views.ApiPostDV.as_view(), name ='post-like'),
    path('comment/create/', views.ApiCommentCV.as_view(), name ='comment_create'),
]