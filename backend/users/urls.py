from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='register'),
    path('detail/', views.UserDetailView.as_view(), name='login'),
]