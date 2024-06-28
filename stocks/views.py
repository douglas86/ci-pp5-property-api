from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from adrf.viewsets import ViewSet

from .models import Stocks
from .serilizers import StockSerializer
from property.views import AsyncViewSet


# Create your views here.
# Create
class PropertyCreateView(ViewSet):
    """
    Create a new property and store it in the database
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = StockSerializer

    message = 'You have successfully created a property.'
    error_message = 'Something went wrong saving the property data.'

    def retrieve(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'message': self.message, 'status': status.HTTP_200_OK})
        else:
            return Response({'message': self.error_message, 'status': status.HTTP_400_BAD_REQUEST})


# Read
class StockListView(ViewSet):
    """
    Fetches all Property data from a database
    """

    model = Stocks.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    message = "You have successfully fetched property data."
    error_message = "Something went wrong fetching property data."

    def get_properties(self, request):
        try:
            data = AsyncViewSet(self.model).retrieve()
            serializer = StockSerializer(instance=data, many=True, context={'request': request})
            return {'message': self.message, 'status': status.HTTP_200_OK, 'data': serializer.data}
        except AssertionError:
            return {'message': self.error_message, 'status': status.HTTP_400_BAD_REQUEST, 'data': None}

    def retrieve(self, request):
        return Response(self.get_properties(request))
