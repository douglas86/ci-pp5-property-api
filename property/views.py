from adrf.viewsets import ViewSet
from rest_framework.response import Response


class PropertyListView(ViewSet):
    message = 'This is the home view'

    async def list(self, request):
        return Response({'message': self.message})
