from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
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
