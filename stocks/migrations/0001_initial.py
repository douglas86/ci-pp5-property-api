# Generated by Django 4.2.11 on 2024-05-31 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('Profile', '0003_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_image', models.ImageField(default='../default_profile_rkmhff', upload_to='images/')),
                ('property_address', models.CharField(max_length=100)),
                ('property_area', models.CharField(max_length=100)),
                ('area_code', models.CharField(max_length=100)),
                ('rent', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
    ]
