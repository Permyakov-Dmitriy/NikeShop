# Generated by Django 4.1.7 on 2023-06-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_nike', '0003_alter_nikeuser_options_alter_nikeuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nikeuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]