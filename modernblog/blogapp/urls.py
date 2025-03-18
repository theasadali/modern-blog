from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post')
]