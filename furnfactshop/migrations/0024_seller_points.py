# Generated by Django 5.0.6 on 2024-05-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnfactshop', '0023_remove_orderitem_company_mebel_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='points',
            field=models.ManyToManyField(blank=True, related_name='Tochki', to='furnfactshop.points'),
        ),
    ]
