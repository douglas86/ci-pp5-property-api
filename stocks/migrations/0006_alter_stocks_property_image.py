# Generated by Django 4.2.11 on 2024-06-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0005_alter_stocks_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='property_image',
            field=models.CharField(max_length=1000),
        ),
    ]