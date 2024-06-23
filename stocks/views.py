from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from adrf.viewsets import ViewSet

from .models import Stocks
from .serilizers import StockSerializer


# Create your views here.
# Create
class PropertyCreateView(ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = StockSerializer

    message = 'You have successfully created a property.'
    error_message = 'Something went wrong.'

    def retrieve(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'message': self.message, 'status': status.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response({'message': self.error_message, 'status': status.HTTP_400_BAD_REQUEST,
                             'errors': serializer.errors})


# class StocksCreateView(generics.ListCreateAPIView):
#     serializer_class = StockSerializer
#     queryset = Stocks.objects.all()
#     permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
#
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#             return Response("You have successfully saved a new property", status=status.HTTP_201_CREATED)
#         return Response("There was an error saving to database", status=status.HTTP_400_BAD_REQUEST)


# Read
class StocksList(APIView):
    model = Stocks

    def get(self, request):
        return Response(self.model.objects.all())
