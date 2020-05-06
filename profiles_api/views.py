from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

    def put(self, request, pk=None):
        """Update an entire entry in DB, It's replacing the existing entry"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partial update (only fields) of an entry in DB"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an entry in DB"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        return Response(
            {
                'message': 'Hello',
                'a_viewset':
                    [
                    'Uses actions (list, create, retrieve, update and partial_update)',
                    'Automatically maps to URLs using Routers',
                    'Provides more functionality with less code',
                    ]
            }
        )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Hello {name}'})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Subclass of ObtainAuthToken to make it browsable though the API admin pages"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ """
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
