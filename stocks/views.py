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

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response({message: "You have successfully saved a new property"}, status=status.HTTP_201_CREATED)
        return Response({message: "There was an error saving to database"}, status=status.HTTP_400_BAD_REQUEST)


# Read
class StocksList(APIView):
    model = Stocks

    def get(self, request):
        return Response(self.model.objects.all())
