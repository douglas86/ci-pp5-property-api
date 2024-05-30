from django.db import models
from Profile.models import Profile


# Create your models here.
class Stocks(models.Model):
    product = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property_image = models.ImageField(upload_to='images/', default='../default_profile_rkmhff')
    property_address = models.CharField(max_length=100)
    property_area = models.CharField(max_length=100)
    area_code = models.CharField(max_length=100)
    rent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
