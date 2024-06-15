# Generated by Django 5.0.6 on 2024-05-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnfactshop', '0033_seller_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='timezone',
        ),
        migrations.AddField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
