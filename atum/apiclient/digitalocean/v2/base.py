from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from atum.apiclient import to_object
from atum.apiclient.base import AtumBase
from atum.apiclient import item_object_factory_classes
from atum.apiclient.base import BaseConnection, BaseAPIClient
from future.utils import viewitems, PY3
from .params import PARAMS
import atum.common.exceptions as exceptions

if PY3:
    from builtins import *

do_v2_object_factory_classes = {}


class Connection(BaseConnection):

    def _set_auth(self):
        """Setting auth header"""
        token = self.auth.get("token", None)
        self.headers.update({"Authorization": "Bearer {:s}".format(token)})


class APIClient(BaseAPIClient):

    def __init__(self, connection):
        super(APIClient, self).__init__(connection)


def do_v2_object_class_factory(name, field_map, url, result_key=None,
                               object_class_name=None,
                               base_classes=(APIClient, AtumBase)):

    """ Build Object specific classes (May be with common methods)
    :param name: Name of the class
    :param field_map: a dict of field map
    :param url: Relative url based on DIGITALOCEAN_ENDPOINT
    :param result_key: Result key to be looked at Default: name + "s"
    :param base_classes: a tuple of base classes
    :param object_class_name: object class name
    :return:
    """

    # Assuming url is only the last argument without / (e.g url = "flavors")
    if not result_key:
        result_key = url

    def __init__(self, connection):
        APIClient.__init__(self, connection)
        self.field_map = field_map
        self.url = url

    def list_(self, filters=None, wrap=False):
        # URL https://api.digitalocean.com/v2/%s % url
        result = self.request(url, "GET")[result_key]
        if filters:
            objs = self._filter(filters, result)
        else:
            objs = result

        object_cls = object_class_name or name.replace("Base", "") + "Object"
        return to_object(objs, self.field_map,
                         item_object_factory_classes[object_cls], wrap)

    def _id_or_object(self, id=None, obj=None):
        if id:
            return id
        elif obj:
            return obj.id
        else:
            raise exceptions.InvalidArgumentError("Either Object or id must be provided")

    def delete(self, obj=None, id=None):
        """ Delete the objects
        :param obj: object
        :param id: id - either id or sshkey must be provided
        :return: None
        """
        id_ = self._id_or_object(id, obj)
        return self.request("%s/%s" % (url, id_), "DELETE")

    cls_dict = {
        "__init__": __init__,
        "list": list_,
        "field_map": field_map,
        "_id_or_object": _id_or_object,
        "delete": delete,
    }
    cls = type(str(name), base_classes, cls_dict)

    do_v2_object_factory_classes.update({name: cls})
    return cls


##
# Register all Classes - These classes are require to wrap the data to object
# based classes by to_object().
# Class names should be like Domain, Flavor, Image etc,
# NOTE: Class names will need to be changed to *Base or something as create
# and update methods will be different which need different classes generated,
# in which case, they can be derived from these classes
##
for obj_name, params in viewitems(PARAMS):
    class_name = obj_name + 'Base'
    field_map = params.get("field_map", {})
    url = params.get("url", None)
    result_key = params.get("result_key", None)
    object_class_name = params.get("object_class_name", None)
    ##
    # If url is not there in PARAMS, build it by appending "s" to name
    # This should work mostly
    ##
    if not url:
        url = obj_name.lower() + "s"

    kw_arguments = {"name": class_name, "field_map": field_map, "url": url}

    if result_key:
        kw_arguments.update({"result_key": result_key})

    if object_class_name:
        kw_arguments.update({"object_class_name": object_class_name})

    do_v2_object_class_factory(**kw_arguments)


class Flavor(do_v2_object_factory_classes['FlavorBase']):
    pass


class Image(do_v2_object_factory_classes['ImageBase']):
    pass


class FloatingIP(do_v2_object_factory_classes['FloatingIPBase']):
    pass


class Region(do_v2_object_factory_classes['RegionBase']):
    pass


class Server(do_v2_object_factory_classes['ServerBase']):
    pass


do_v2_object_classes = {"Flavor": Flavor,
                        "Image": Image,
                        "FloatingIP": FloatingIP,
                        "Region": Region,
                        "Server": Server
                        }
