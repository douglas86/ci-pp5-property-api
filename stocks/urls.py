from stocks import views

urlpatterns = [
    path('', views.StocksList.as_view(), name='index'),
]
