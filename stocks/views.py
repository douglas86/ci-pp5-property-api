from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.views import APIView, Response

from .models import Stocks
from .serilizers import StockSerializer


# Create your views here.
# Create
class StocksCreateView(generics.ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stocks.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})

        return context


# Read
class StocksList(APIView):
    model = Stocks

    def get(self, request):
        return Response(self.model.objects.all())
