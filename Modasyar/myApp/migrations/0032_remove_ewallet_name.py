# Generated by Django 5.0.6 on 2024-06-23 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0031_ewallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ewallet',
            name='name',
        ),
    ]