from django.urls import path

from shop_nike.views import ShopView, ProductView, ProductsSearchView
from main.views import FavoriteDeleteView, FavoriteView


url_shop = [
    path('product/', ProductView.as_view()),
    path('product/fav/', FavoriteView.as_view()),
    path('product/fav-del/', FavoriteDeleteView.as_view()),
    path('find/', ProductsSearchView.as_view()),
    path('', ShopView.as_view(), name='shop'),
]