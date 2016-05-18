from .models import Datacenter
from .serializers import DatacenterSerializer, UserSerializer, FlavorSerializer, \
    ImageSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet
from functools import lru_cache
from rest_framework import status
from atum.apiclient import get_client as atum_get_client
from ast import literal_eval


class DatacenterViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,)
    serializer_class = DatacenterSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return Datacenter.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


@lru_cache()
def get_client(datacenter):
    dc_obj = Datacenter.objects.get(name=datacenter)
    auth_data = literal_eval(dc_obj.auth)
    dc_type = dc_obj.type
    return atum_get_client(dc_type, auth_data)


class FlavorViewSet(ViewSet):
    serializer_class = FlavorSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        flavor_list = client.flavor.list(wrap=True, dc=dc_name)
        serializer = FlavorSerializer(
            instance=flavor_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.flavor.get(id, wrap=True, dc=dc_name)

        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FlavorSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class ImageViewSet(ViewSet):
    serializer_class = ImageSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        image_list = client.image.list(wrap=True, dc=dc_name)
        serializer = ImageSerializer(
            instance=image_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.image.get(int(id), wrap=True, dc=dc_name)
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ImageSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)
