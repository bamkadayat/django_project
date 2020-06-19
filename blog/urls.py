from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # name is used for dynamic url in navbar link tag
    path('about/', views.about, name='blog-about')
]