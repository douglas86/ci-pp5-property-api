from django.urls import path

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile_view'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
]
