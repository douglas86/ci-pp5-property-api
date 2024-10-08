# Generated by Django 4.2.11 on 2024-08-11 18:54

from django.db import migrations, models
import stocks.models


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0006_alter_stocks_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='property_image',
            field=models.ImageField(
                default='https://res.cloudinary.com/dtm8tjo1f/image/upload/v1712434760/default_post_r8m7an.jpg',
                upload_to=stocks.models.upload_location),
        ),
    ]
