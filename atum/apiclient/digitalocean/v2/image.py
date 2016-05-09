from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient
from atum.apiclient.base import AtumBase
from atum.apiclient import item_object_factory_classes


class Image(APIClient, AtumBase):
    """Manage Images."""

    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            "id": "id",
            "name": "slug",
            "public": "public",
            "created_at": "created_at",
            "min_disk": "min_disk_size",
            "x_distribution": "distribution",
            "x_regions": "regions",
            "x_type": "type",
        }

    def list(self, filters=None, wrap=False):
        # URL https://api.digitalocean.com/v2/images
        result = self.request("images", "GET")["images"]
        if filters:
            images = self._filter(filters, result)
        else:
            images = result

        return to_object(images, self.field_map,
                         item_object_factory_classes["ImageObject"], wrap)
