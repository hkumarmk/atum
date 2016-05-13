from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class SSHKey(do_v2_object_factory_classes['SSHKeyBase']):

    def add(self, name, public_key, wrap=True):
        """ Add sshkeys
        :param name: Name of the key
        :param public_key: SSH Public key string
        :param wrap: wrap the result into Object specific class
        :return:
        """
        params = {"name": name, "public_key": public_key}
        result = self.request(self.url, "POST", params).get("ssh_key", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

    create = add

    def get(self, id, wrap=True):
        """ Retrieve an ssh key with ID
        :param id: sshkey id
        :return: ssh key
        :param wrap: wrap the result into Object specific class instance
        """
        result = self.request("%s/%s" % (self.url, id), "GET").get("ssh_key", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

    def rename(self, new_name, obj, wrap=True):
        params = {"name": new_name}
        result = self.request("%s/%s" % (self.url, obj.id), "PUT", params).get("ssh_key", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

do_v2_object_classes.update({"SSHKey": SSHKey})
