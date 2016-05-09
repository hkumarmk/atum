from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from atum.apiclient import to_object
from atum.apiclient.digitalocean.v2.base import APIClient
from atum.apiclient.domain import DomainBase, DomainObject


class Domain(APIClient, DomainBase):
    """Manage Domains."""

    def __init__(self, connection):
        super().__init__(connection)
        self.field_map = {
            "id": "name",
            "name": "name",
            "ttl": "ttl",
            "zone": "zone_file",
        }
        self.object_class = DomainObject

    def list(self, filters=None, wrap=False):
        # URL https://api.digitalocean.com/v2/domains
        result = self.request("domains", "GET")["domains"]
        if filters:
            domains = self._filter(filters, result)
        else:
            domains = result

        return to_object(domains, self.field_map, DomainObject, wrap)
