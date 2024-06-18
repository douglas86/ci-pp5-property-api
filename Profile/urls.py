from django.urls import path, include

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileListView.as_view({'get': 'retrieve'}), name='profiles'),
    path('<int:pk>/', views.ProfileByIdView.as_view({'get': 'retrieve'}), name='profile_by_id'),
    path('logout/', views.LogoutView.as_view(), name='logout_view'),
    # path('profiles/change_password/', views.ChangePassword.as_view(), name='change_password'),
]
