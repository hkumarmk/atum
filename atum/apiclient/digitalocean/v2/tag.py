from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class Tag(do_v2_object_factory_classes['TagBase']):

    def add(self, name, wrap=False):
        """ Add tags
        :param name: Name of the key
        :param wrap: wrap the result into Object specific class
        :return:
        """
        params = {"name": name}
        result = self.request(self.url, "POST", params).get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap)

    def get(self, obj=None, id=None, wrap=False):
        """ Retrieve an tag with ID
        :param id: tag id
        :param obj: tag object either id or tag must be provided
        :return: tag key
        """
        id_ = self._id_or_object(id, obj)
        result = self.request("%s/%s" % (self.url, id_), "GET").get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap)

    def rename(self, new_name, obj=None, id=None, wrap=False):
        id_ = self._id_or_object(id, obj)
        params = {"name": new_name}
        print("%s/%s" % (self.url, id_))
        result = self.request("%s/%s" % (self.url, id_), "PUT", params).get("tag", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['TagObject'], wrap)

    def tag_server(self, server, tag):
        pass

    def untag_server(self, server, tag):
        pass

do_v2_object_classes.update({"Tag": Tag})
