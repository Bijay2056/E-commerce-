# Generated by Django 5.0.1 on 2024-03-13 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_orders_amount_alter_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2024, 3, 13, 17, 22, 2, 639625)),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
