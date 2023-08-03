from django.contrib import admin
from django.urls import path, include
from social_django import urls

from main.views import Home, FavoriteView, FavoriteDeleteView
from auth_nike.views import RegView, AuthView, VKEmailView

from orders.urls import url_orders
from auth_nike.urls import url_profile, url_reset_password
from shop_nike.urls import url_shop


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
