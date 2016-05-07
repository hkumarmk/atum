from atum.apiclient.common.flavor import FlavorBase, FlavorObject
from atum.apiclient.digitalocean import APIClient
from atum.apiclient.common import to_object


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
