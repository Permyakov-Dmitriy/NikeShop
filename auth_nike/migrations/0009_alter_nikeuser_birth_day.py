# Generated by Django 4.2.2 on 2023-07-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_nike', '0008_nikeuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nikeuser',
            name='birth_day',
            field=models.DateField(null=True),
        ),
    ]
