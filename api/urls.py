from django.urls import path, include
from .views import get_user, post_register, post_login



urlpatterns = [
    # path('', include('rest_framework.urls')),  # login, logout
    path('<user>', get_user),
    path('auth/register', post_register),
    path('auth/login', post_login),
]

