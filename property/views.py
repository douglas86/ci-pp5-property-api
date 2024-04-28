from adrf.viewsets import ViewSet


class PropertyListView(ViewSet):
    message = 'This is the async list method of the PropertyListView'

    async def list(self, request):
        return Response({
            'message': self.message
        })
