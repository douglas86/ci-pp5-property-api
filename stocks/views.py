from django.shortcuts import render
from rest_framework.views import APIView

from .models import Stocks


# Create your views here.
class StocksList(APIView):
    model = Stocks
