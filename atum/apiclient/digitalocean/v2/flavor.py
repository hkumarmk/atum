from atum.apiclient.flavor import FlavorBase, FlavorObject
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient


class Flavor(APIClient, FlavorBase):
    """Manage Flavors"""
    FIELD_MAPS = {
        'name': 'slug',
        'cpus': 'vcpus',
        'cph': 'price_hourly',
        'cpm': 'price_monthly',
        }

    def list(self):
        flavors = self.request("sizes", "GET")["sizes"]
        return to_object(flavors, self.FIELD_MAPS, FlavorObject)

    def get(self):
        pass
