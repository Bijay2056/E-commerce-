# Generated by Django 5.0.1 on 2024-01-25 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_username_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logo',
        ),
    ]