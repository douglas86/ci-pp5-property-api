from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Profile import views

app_name = 'Profile'

urlpatterns = [
    path('', views.ProfileListView.as_view({'get': 'retrieve'}), name='profiles'),
    path('login/', views.LoginView.as_view({'post': 'retrieve'}), name='login_view'),
    path('logout/', views.LogoutView.as_view({'get': 'retrieve'}), name='logout_view'),
    path('token/', views.TokenView.as_view(), name='token_view'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('profiles/change_password/', views.ChangePassword.as_view(), name='change_password'),
]
