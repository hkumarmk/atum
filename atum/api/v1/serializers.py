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
    sshkeys = serializers.HyperlinkedIdentityField(
        view_name='sshkey-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    floatingips = serializers.HyperlinkedIdentityField(
        view_name='floatingip-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    tags = serializers.HyperlinkedIdentityField(
        view_name='tag-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    domains = serializers.HyperlinkedIdentityField(
        view_name='domain-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )
    servers = serializers.HyperlinkedIdentityField(
        view_name='server-list',
        lookup_url_kwarg="dc_name",
        lookup_field='name'
    )


    class Meta:
        model = Datacenter
        fields = ('url', 'name', 'type', 'owner', 'auth', 'region', 'flavors',
                  'regions', 'sshkeys', 'floatingips', 'tags', 'domains',
                  'servers', 'images')


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


class SSHKeySerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='sshkey-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    fingerprint = serializers.CharField()
    public_key = serializers.CharField()

    class Meta:
        fields = '__all__'


class FloatingIPSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='floatingip-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    ip = serializers.CharField()
    server = serializers.CharField()

    class Meta:
        fields = '__all__'


class TagSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='tag-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    resources = serializers.CharField()

    class Meta:
        fields = '__all__'


class DomainSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='domain-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    ttl = serializers.CharField()
    zone = serializers.CharField()

    class Meta:
        fields = '__all__'


class ServerSerializer(serializers.Serializer):

    url = ParameterisedHyperlinkedIdentityField(
        view_name='server-detail',
        lookup_fields=(('datacenter', 'dc_name'), ('id', 'id')),
        read_only=True
    )

    name = serializers.CharField()
    cpus = serializers.IntegerField()
    memory = serializers.IntegerField()
    disk = serializers.IntegerField()
    status = serializers.CharField()
    created_at = serializers.CharField()
    image = serializers.CharField()
    flavor = serializers.CharField()
    networks = serializers.CharField()
    x_tags = serializers.CharField()
    x_locked = serializers.BooleanField()
    x_kernel = serializers.CharField()
    x_features = serializers.CharField()
    x_backup_ids = serializers.CharField()
    x_snapshot_ids = serializers.CharField()

    class Meta:
        fields = '__all__'
