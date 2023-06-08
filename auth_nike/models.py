from django.db.models import DateField, CharField, EmailField, TextField
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class NikeUser(AbstractBaseUser, models.Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=30)
    email = EmailField(unique=True)
    password = TextField()
    birth_day = DateField()

    USERNAME_FIELD = 'email'