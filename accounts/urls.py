"""
"""
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view()),
]
