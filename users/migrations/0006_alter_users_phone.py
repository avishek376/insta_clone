# Generated by Django 4.1 on 2024-02-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(default=890883924, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
