from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiView = [
        'User HTTP methods as function (get, post, patch, put and delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]
        return Response(
            {
                'message': 'Hello',
                'an_api_view': an_apiView
            }
        )

    def post(self, request):
        """Create entry with the provided name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
