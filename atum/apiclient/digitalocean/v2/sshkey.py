from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class SSHKey(do_v2_object_factory_classes['SSHKeyBase']):

    def add(self, name, public_key, wrap=False):
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

    def get(self, obj=None, id=None, wrap=False):
        """ Retrieve an ssh key with ID
        :param id: ssh key id
        :param obj: sshkey object either id or sshkey must be provided
        :return: ssh key
        """
        id_ = self._id_or_object(id, sshkey)
        result = self.request("%s/%s" % (self.url, id_), "GET").get("ssh_key", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

    def rename(self, new_name, obj=None, id=None, wrap=False):
        id_ = self._id_or_object(id, obj)
        params = {"name": new_name}
        result = self.request("%s/%s" % (self.url, id_), "PUT", params).get("ssh_key", {})
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

do_v2_object_classes.update({"SSHKey": SSHKey})
