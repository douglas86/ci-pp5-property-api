from django.urls import path

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileListView.as_view({'get': 'retrieve'}), name='profiles'),
    path('login/', views.LoginView.as_view({'post': 'retrieve'}), name='login_view'),
    # path('profiles/change_password/', views.ChangePassword.as_view(), name='change_password'),
]
