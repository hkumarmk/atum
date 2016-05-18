from rest_framework import serializers
from .models import Datacenter
from django.contrib.auth.models import User
from .custom_serializer_field import ParameterisedHyperlinkedIdentityField


class DatacenterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(
        view_name='datacenter-detail',
        lookup_field='name'
    )

    flavors = serializers.HyperlinkedIdentityField(
        view_name='flavor-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    images = serializers.HyperlinkedIdentityField(
        view_name='image-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    regions = serializers.HyperlinkedIdentityField(
        view_name='region-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )

    class Meta:
        model = Datacenter
        fields = ('url', 'name', 'type', 'owner', 'auth', 'flavors', 'images', 'regions')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    datacenters = serializers.HyperlinkedRelatedField(
        many=True, view_name='datacenter-detail', read_only=True, lookup_field='name')

    class Meta:
        model = User
        fields = ('url', 'username', 'datacenters')


class FlavorSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='flavor-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    available = serializers.BooleanField()
    cpus = serializers.IntegerField()
    memory = serializers.IntegerField()
    disk = serializers.IntegerField()
    transfer = serializers.FloatField()
    x_cph = serializers.CharField()

    class Meta:
        fields = '__all__'


class ImageSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='image-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    public = serializers.BooleanField()
    min_disk = serializers.IntegerField()
    #created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    created_at = serializers.CharField()
    x_distribution = serializers.CharField()
    x_type = serializers.CharField()

    class Meta:
        fields = '__all__'


class RegionSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='region-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    x_available = serializers.BooleanField()
    x_features = serializers.CharField()
    x_flavors = serializers.CharField()

    class Meta:
        fields = '__all__'
