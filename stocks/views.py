from django.shortcuts import render
from rest_framework.views import APIView, Response

from .models import Stocks


# Create your views here.
class StocksList(APIView):
    model = Stocks

    def get(self, request):
        return Response(self.model.objects.all())
