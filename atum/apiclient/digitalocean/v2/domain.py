from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class Domain(do_v2_object_factory_classes['DomainBase']):

    def add(self, name, ip_address, wrap=True, dc=None):
        """ Add domains
        :param name: Domain name
        :param ip_address: IP address to point to domain
        :param wrap: wrap the result into Object specific class
        :return:
        """
        params = {"name": name, "ip_address": ip_address}
        result = self.request(self.url, "POST", params).get("domain", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['DomainObject'], wrap, dc)

    create = add

    def get(self, id, wrap=True, dc=None):
        """ Retrieve an domain with ID
        :param wrap: Wrap the result into object specific instance
        :param obj: domain object
        :return: domain key
        """
        result = self.request("%s/%s" % (self.url, id), "GET").get("domain", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['DomainObject'], wrap, dc)

do_v2_object_classes.update({"Domain": Domain})
