from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient
from atum.apiclient.region import RegionBase, RegionObject


class Region(APIClient, RegionBase):
    """Manage Regions."""

    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            "id": "slug",
            "name": "name",
            "x_available": "available",
            "x_features": "features",
            "x_flavors": "sizes",
        }
        self.object_class = RegionObject

    def list(self, filters=None, wrap=False):
        # URL https://api.digitalocean.com/v2/regions
        result = self.request("regions", "GET")["regions"]
        if filters:
            regions = self._filter(filters, result)
        else:
            regions = result

        return to_object(regions, self.field_map, RegionObject, wrap)
