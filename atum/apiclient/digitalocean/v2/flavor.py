from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from atum.apiclient.flavor import FlavorBase, FlavorObject
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient


class Flavor(APIClient, FlavorBase):
    """Manage Flavors"""
    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            "id": "slug",
            "name": "slug",
            "cpus": "vcpus",
            "x_cph": "price_hourly",
            "x_cpm": "price_monthly",
            "x_regions": "regions",
            }

    def list(self, filters=None, wrap_to_object=True):
        # URL https://api.digitalocean.com/v2/sizes
        result = self.request("sizes", "GET")["sizes"]
        if filters:
            flavors = self._filter(filters, result)
        else:
            flavors = result

        if wrap_to_object:
            return to_object(flavors, self.field_map, FlavorObject)
        else:
            return flavors

