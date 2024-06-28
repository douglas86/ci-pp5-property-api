from stocks import views
from django.urls import path

urlpatterns = [
    path('', views.StockListView.as_view({'get': 'retrieve'}), name='stock_views'),
    path('create/', views.PropertyCreateView.as_view({'post': 'retrieve'}), name='stocks_create'),
    path('delete/<int:pk>/', views.StockDeleteView.as_view({'delete': 'retrieve'}), name='stocks_delete'),
]
