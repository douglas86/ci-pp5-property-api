from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def upload_location(_, filename):
    return 'images/{filename}'.format(filename=filename)


class Stocks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property_image = models.ImageField(
        upload_to=upload_location,
        default='https://res.cloudinary.com/dtm8tjo1f/image/upload/v1712434760/default_post_r8m7an.jpg'
    )
    property_address = models.CharField(max_length=100)
    property_area = models.CharField(max_length=100)
    area_code = models.CharField(max_length=100)
    rent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
