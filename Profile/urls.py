from django.urls import path

from Profile import views

urlpatterns = [
    path('', views.ProfileView.as_view, name='index'),
]
