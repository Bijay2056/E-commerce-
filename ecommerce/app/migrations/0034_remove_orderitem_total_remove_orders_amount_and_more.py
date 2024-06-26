# Generated by Django 5.0.1 on 2024-03-13 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_remove_orderitem_image_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2024, 3, 13, 19, 41, 41, 456274)),
        ),
    ]
