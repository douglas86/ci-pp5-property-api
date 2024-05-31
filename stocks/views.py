from django.shortcuts import render
from rest_framework.views import APIView, Response

from .models import Stocks


# Create your views here.
# Create
class StocksCreateView(APIView):
    model = Stocks

    def post(self, request):
        return Response("Hello World")


# Read
class StocksList(APIView):
    model = Stocks

    def get(self, request):
        return Response(self.model.objects.all())
