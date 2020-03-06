# 3. THIS is where we redirect the stuff in not the biggest counties in the world

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
