from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class Datacenter(models.Model):
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
    owner = models.ForeignKey('auth.User', related_name='datacenters')
