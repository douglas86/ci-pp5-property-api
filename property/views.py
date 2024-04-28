from adrf.viewsets import ViewSet
from rest_framework.response import Response


class PropertyListView(ViewSet):
    message = 'This is the async list method of the PropertyListView'

    async def list(self, request):
        return Response({
            'message': self.message
        })
