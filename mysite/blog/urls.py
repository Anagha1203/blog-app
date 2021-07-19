from . import views
from django.urls import path,include
from django.contrib import admin
from blog.views import post_admin


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('admin_login', post_admin, name='admin_login'),
    
]