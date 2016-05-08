from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient
from atum.apiclient.image import ImageBase, ImageObject


class Image(APIClient, ImageBase):
    """Manage Images."""

    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            'x_distribution': 'distribution',
            'x_regions': 'regions',
            'x_type': 'type',
        }

    def list(self, filters=None):
        # URL https://api.digitalocean.com/v2/images
        result = self.request("images", "GET")["images"]
        if filters:
            images = self._filter(filters, result)
        else:
            images = result

        return to_object(images, self.field_map, ImageObject)
