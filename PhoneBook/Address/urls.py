from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('phone/', views.PhoneAPIView.as_view()),
    path('phone/<str:id>', views.PhoneAPIView.as_view())
]
