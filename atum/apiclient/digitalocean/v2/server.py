from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class Server(do_v2_object_factory_classes['ServerBase']):

    def add(self, name, region, flavor, image, ssh_keys=None,
            backups=False, ipv6=False, user_data=None,
            private_networking=False, wrap=True):
        """ Add servers
        :param private_networking: Enable/disable private Networking
        :param name: Name of the Server,
                    Can be a list of names in which case multiple servers
                    with the names in the list is created
                    This can be a string also, in which case one server with
                    the name provided
        :param image: Image, type: Image object
        :param flavor: Flavor, type: Flavor object
        :param region: Region, type: Region object
        :param user_data: Userdata string
        :param ipv6: Whether to enable ipv6, Type: Bool, Default: False
        :param backups: Whether to enable backups, Type: Bool, Default: False
        :param ssh_keys: A List of ssh key objects, Type: list
        :param wrap: wrap the result into Object specific class, Type: Bool, Default: True
        :return: Server object or dict
        """
        if isinstance(name, list):
            params = {"names": [name]}
        else:
            params = {"name": name}

        # In case of string, need to convert to list
        if ssh_keys:
            if not isinstance(ssh_keys, list):
                ssh_keys = [ssh_keys]

            ssh_keys = [key.id for key in ssh_keys]

        params.update({"region": region.id, "size": flavor.id, "image": image.id,
                       "ssh_keys": ssh_keys, "backups": backups,
                       "ipv6": ipv6, "user_data": user_data,
                       "private_networking": private_networking})
        result = self.request(self.url, "POST", params).get("droplet", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    create = add

    def get(self, id, wrap=True):
        """ Retrieve an server with ID
        :param wrap: wrap the result into Object specific class, Type: Bool, Default: True
        :param obj: server object
        :return: server key
        """
        result = self.request("%s/%s" % (self.url, id), "GET").get("droplet", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def reboot(self, obj, wrap=True):
        params = {"type": "reboot"}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)


    def power_cycle(self, obj, wrap=True):
        params = {"type": "power_cycle"}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def shutdown(self, obj, wrap=True):
        params = {"type": "shutdown"}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def power_off(self, obj, wrap=True):
        params = {"type": "power_off"}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def power_on(self, obj, wrap=True):
        params = {"type": "power_on"}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def resize(self, obj, flavor, resize_disk=False, wrap=True):
        params = {"type": "resize", "disk": resize_disk, "size": flavor.id}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def rebuild(self, obj, image, wrap=True):
        params = {"type": "rebuild", "image": image}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

    def rename(self, obj, name,  wrap=True):
        params = {"type": "rename", "name": name}
        result = self.request("%s/%s/actions" % (self.url, obj.id), "POST", params).get("action", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['ServerObject'], wrap)

do_v2_object_classes.update({"Server": Server})
