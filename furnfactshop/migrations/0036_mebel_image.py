# Generated by Django 5.0.6 on 2024-05-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnfactshop', '0035_remove_seller_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='mebel',
            name='image',
            field=models.ImageField(null=True, upload_to='static', verbose_name='Картинка для публикации'),
        ),
    ]
