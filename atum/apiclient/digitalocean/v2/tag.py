from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class Tag(do_v2_object_factory_classes['TagBase']):

    def add(self, name, wrap=True, dc=None):
        """ Add tags
        :param name: Name of the key
        :param wrap: wrap the result into Object specific class
        :return:
        """
        params = {"name": name}
        result = self.request(self.url, "POST", params).get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap, dc)

    create = add

    def get(self, id, wrap=True, dc=None):
        """ Retrieve an tag with ID
        :param id: tag id
        :return: tag key
        """
        result = self.request("%s/%s" % (self.url, id), "GET").get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap, dc)

    def rename(self, new_name, obj, wrap=True, dc=None):
        params = {"name": new_name}
        result = self.request("%s/%s" % (self.url, obj.id), "PUT", params).get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap, dc)

    def tag_server(self, server, tag):
        pass

    def untag_server(self, server, tag):
        pass

do_v2_object_classes.update({"Tag": Tag})
