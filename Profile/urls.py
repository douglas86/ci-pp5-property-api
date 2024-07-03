from django.urls import path, include

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileListView.as_view({'get': 'retrieve'}), name='profiles'),
    path('<int:pk>/', views.ProfileByIdView.as_view({'get': 'retrieve'}), name='profile_by_id'),
    path('delete/<int:pk>/', views.ProfileDeleteView.as_view({'delete': 'destroy'}), name='delete_profile'),
    path('logout/', views.LogoutView.as_view(), name='logout_view'),
    path('change_password/', views.ChangePasswordView.as_view({'post': 'retrieve'}), name='change_password'),
]
