from django.urls import path

from .views import BasketView, BascketAddView


url_orders = [
    path('bucket/', BasketView.as_view(), name='bucket'),
    path('add-on-bucket/', BascketAddView.as_view())
]