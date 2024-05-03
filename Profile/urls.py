from django.urls import path

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_view'),
]
