from rest_framework import serializers
from .models import Datacenter
from django.contrib.auth.models import User


class DatacenterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(
        view_name='datacenter-detail',
        lookup_field='name'
    )

    class Meta:
        model = Datacenter
        fields = ('url', 'name', 'type', 'auth', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    datacenters = serializers.HyperlinkedRelatedField(
        many=True, view_name='datacenter-detail', read_only=True, lookup_field='name')

    class Meta:
        model = User
        fields = ('url', 'username', 'datacenters')
