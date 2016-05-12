from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class Domain(do_v2_object_factory_classes['DomainBase']):

    def add(self, name, ip_address, wrap=False):
        """ Add domains
        :param name: Domain name
        :param ip_address: IP address to point to domain
        :param wrap: wrap the result into Object specific class
        :return:
        """
        params = {"name": name, "ip_address": ip_address}
        result = self.request(self.url, "POST", params).get("domain", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['DomainObject'], wrap)

    def get(self, obj=None, id=None, wrap=False):
        """ Retrieve an domain with ID
        :param id: domain id
        :param obj: domain object either id or domain must be provided
        :return: domain key
        """
        id_ = self._id_or_object(id, obj)
        result = self.request("%s/%s" % (self.url, id_), "GET").get("domain", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['DomainObject'], wrap)

do_v2_object_classes.update({"Domain": Domain})
