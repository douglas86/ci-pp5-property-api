# Generated by Django 4.2.11 on 2024-05-31 21:17

from django.db import migrations, models
import stocks.models


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0004_alter_stocks_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='property_image',
            field=models.ImageField(default='default_profile_rkmhff', upload_to=stocks.models.upload_location),
        ),
    ]
