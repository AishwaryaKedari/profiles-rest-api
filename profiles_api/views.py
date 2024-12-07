# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permission

# Create your views here.
class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as finctions (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test viewset """

    serializer_class = serializers.HelloSerializer

    def list(self,request):

        a_viewset = [
            "viewset list(create, retirve,update,partial update,destroy)",
            "automaically maps to urls to router",
            "provide more functionality with less code",
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """create viewset"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Getting an object id"""
        return Response({'HTTP_method': 'GET'})

    def update(self, request, pk=None):
        """Updating an object"""
        return Response({'HTTP_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """updating part of object"""
        return Response({'HTTP_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Deleting an object"""
        return Response({'HTTP_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """creating updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)


