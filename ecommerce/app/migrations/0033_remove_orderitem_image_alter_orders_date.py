# Generated by Django 5.0.1 on 2024-03-13 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_orders_quantity_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='image',
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2024, 3, 13, 19, 32, 46, 862688)),
        ),
    ]
