"""NikeShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import Home, ProfileView
from auth_nike.views import RegView, LogoutView, AuthView
from auth_nike.views import UserForgotPasswordView, UserPasswordResetConfirmView


url_reset_password = [
    path('', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('profile/', ProfileView.as_view()),
    path('profile/logout/', LogoutView.as_view()),
    path('registration/', RegView.as_view(), name='reg'),
    path('auth/', AuthView.as_view()),
    path('password-reset/', include(url_reset_password)),
]
