from django.urls import path

from .views import BucketView, BucketAddView


url_orders = [
    path('bucket/', BucketView.as_view(), name='bucket'),
    path('add-on-bucket/', BucketAddView.as_view())
]