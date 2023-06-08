# Generated by Django 4.1.7 on 2023-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_nike', '0002_alter_nikeuser_options_alter_nikeuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nikeuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='nikeuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='nikeuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='nikeuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='nikeuser',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='nikeuser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='nikeuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
