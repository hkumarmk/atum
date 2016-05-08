from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient
from atum.apiclient.server import ServerBase, ServerObject


class Server(APIClient, ServerBase):
    """Manage Servers."""

    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            "id": "id",
            "name": "name",
            "cpus": "vcpus",
            "memory": "memory",
            "disk": "disk",
            "status": "status",
            "created_at": "created_at",
            "image": "image",
            "flavor": "flavor",
            "networks": "networks",
            "region": "region",
            "x_tags": "tags",
            "x_locked": "locked",
            "x_kernel": "kernel",
            "x_features": "features",
            "x_backup_ids": "backup_ids",
            "x_snapshot_ids": "snapshot_ids",
        }
        self.object_class = ServerObject

    def list(self, filters=None, wrap=False):
        # URL https://api.digitalocean.com/v2/droplets
        result = self.request("droplets", "GET")["droplets"]
        if filters:
            servers = self._filter(filters, result)
        else:
            servers = result

        return to_object(servers, self.field_map, ServerObject, wrap)
