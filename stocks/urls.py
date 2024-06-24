from stocks import views
from django.urls import path

urlpatterns = [
    path('', views.StocksList.as_view(), name='stock_views'),
    path('create/', views.PropertyCreateView.as_view({'post': 'retrieve'}), name='stocks_create'),
]
