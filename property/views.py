from rest_framework.response import Response
from rest_framework.views import APIView


class PropertyListView(APIView):
    message = 'This is the home view'

    def get(self, request):
        return Response({'message': self.message})
