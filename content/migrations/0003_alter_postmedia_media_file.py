# Generated by Django 4.1 on 2024-02-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_userpost_is_published_alter_userpost_caption_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='media_file',
            field=models.ImageField(upload_to='media_name'),
        ),
    ]