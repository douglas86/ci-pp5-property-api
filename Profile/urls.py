from django.urls import path

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile_view'),
]
