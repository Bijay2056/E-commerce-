# Generated by Django 5.0.1 on 2024-03-13 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2024, 3, 13, 16, 32, 16, 478892)),
        ),
    ]