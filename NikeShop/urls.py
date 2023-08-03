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
from social_django import urls

from main.views import Home, FavoriteView, FavoriteDeleteView
from auth_nike.views import RegView, AuthView, VKEmailView
from shop_nike.views import ShopView, ProductView, ProductsSearchView

from orders.urls import url_orders
from auth_nike.urls import url_profile, url_reset_password


url_shop = [
    path('product/', ProductView.as_view()),
    path('product/fav/', FavoriteView.as_view()),
    path('product/fav-del/', FavoriteDeleteView.as_view()),
    path('find/', ProductsSearchView.as_view()),
    path('', ShopView.as_view(), name='shop'),
]

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('registration/', RegView.as_view(), name='reg'),
    path('auth/', AuthView.as_view()),
    path('vk-email/', VKEmailView.as_view(), name='VKEmail'),
    path('profile/', include(url_profile)),
    path('password-reset/', include(url_reset_password)),
    path('shop/', include(url_shop)),
    path('social-auth/', include(urls, namespace='social')),
    path('orders/', include((url_orders, 'orders')))
]
