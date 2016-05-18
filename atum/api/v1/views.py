from .models import Datacenter
from . import serializers
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet
from functools import lru_cache
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from atum.apiclient import get_client as atum_get_client
from ast import literal_eval
from atum.common import exceptions

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'datacenters': reverse('datacenter-list', request=request, format=format),
    })

class DatacenterViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,)
    serializer_class = serializers.DatacenterSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return Datacenter.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@lru_cache()
def get_client(datacenter):
    dc_obj = Datacenter.objects.get(name=datacenter)
    auth_data = literal_eval(dc_obj.auth)
    dc_type = dc_obj.type
    return atum_get_client(dc_type, auth_data)


class FlavorViewSet(ViewSet):
    serializer_class = serializers.FlavorSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        flavor_list = client.flavor.list(wrap=True, dc=dc_name)
        serializer = serializers.FlavorSerializer(
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
        serializer = serializers.FlavorSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class ImageViewSet(ViewSet):
    serializer_class = serializers.ImageSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        image_list = client.image.list(wrap=True, dc=dc_name)
        serializer = serializers.ImageSerializer(
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
        serializer = serializers.ImageSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class RegionViewSet(ViewSet):
    serializer_class = serializers.RegionSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        region_list = client.region.list(wrap=True, dc=dc_name)
        serializer = serializers.RegionSerializer(
            instance=region_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.region.get(id, wrap=True, dc=dc_name)
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.RegionSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class SSHKeyViewSet(ViewSet):
    serializer_class = serializers.SSHKeySerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        sshkey_list = client.sshkey.list(wrap=True, dc=dc_name)
        serializer = serializers.SSHKeySerializer(
            instance=sshkey_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.sshkey.get(id, wrap=True, dc=dc_name)
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.SSHKeySerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class FloatingIPViewSet(ViewSet):
    serializer_class = serializers.FloatingIPSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        floatingip_list = client.floatingip.list(wrap=True, dc=dc_name)
        serializer = serializers.FloatingIPSerializer(
            instance=floatingip_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.floatingip.get(id, wrap=True, dc=dc_name)
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.FloatingIPSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class TagViewSet(ViewSet):
    serializer_class = serializers.TagSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        tag_list = client.tag.list(wrap=True, dc=dc_name)
        serializer = serializers.TagSerializer(
            instance=tag_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        data = client.tag.get(id, wrap=True, dc=dc_name)
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TagSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)


class DomainViewSet(ViewSet):
    serializer_class = serializers.DomainSerializer
    lookup_field = 'id'

    def list(self, request, dc_name=None):
        client = get_client(dc_name)
        domain_list = client.domain.list(wrap=True, dc=dc_name)
        serializer = serializers.DomainSerializer(
            instance=domain_list,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, id, dc_name):
        client = get_client(dc_name)
        try:
            data = client.domain.get(id, wrap=True, dc=dc_name)
        except exceptions.APIResourceNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.DomainSerializer(
            instance=data, context={'request': request})
        return Response(serializer.data)