from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class Profile(models.Model):
    """
    Profile model is used to store user profile information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{str(self.user)}'
