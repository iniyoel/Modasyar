# Generated by Django 5.0.6 on 2024-06-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(),
        ),
    ]