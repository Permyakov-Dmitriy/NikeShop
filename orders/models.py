from django.db import models

from auth_nike.models import NikeUser

from shop_nike.models import Product


class BucketModel(models.Model):
    user_id = models.ForeignKey(NikeUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id.email} {self.product_id.title_product}'