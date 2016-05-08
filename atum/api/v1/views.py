from .models import Datacenter
from .serializers import DatacenterSerializer, UserSerializer
from .permissions import IsOwner

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet


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
