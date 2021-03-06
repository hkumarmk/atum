from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class Provider(models.Model):
    OPENSTACK = 'openstack'
    DIGITALOCEAN = 'digitalocean'

    PROVIDER_CHOICES = (
        (OPENSTACK, 'Openstack'),
        (DIGITALOCEAN, 'DigitalOcean')
    )

    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=20, choices=PROVIDER_CHOICES,
                            default=DIGITALOCEAN)
    auth = JSONField()
    owner = models.ForeignKey('auth.User', related_name='providers')


class Datacenter(models.Model):
    name = models.CharField(max_length=30, unique=True)
    provider = models.ForeignKey(Provider, related_name='datacenters')
    owner = models.ForeignKey('auth.User', related_name='datacenters')
    region = models.CharField(max_length=30)
