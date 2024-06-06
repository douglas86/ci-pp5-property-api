from django.urls import path

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('profiles/', views.ProfileView.as_view({'get': 'retrieve'}), name='profile_view'),
    path('profiles/change_password/', views.ChangePassword.as_view(), name='change_password'),
]
