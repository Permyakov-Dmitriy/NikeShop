from django.db import models


class Product(models.Model):
    title_product = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.TextField()

    def __str__(self):
        return self.title_product
    