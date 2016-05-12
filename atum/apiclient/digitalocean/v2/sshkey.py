from .base import do_v2_object_classes, do_v2_object_factory_classes, item_object_factory_classes
from atum.apiclient import to_object


class SSHKey(do_v2_object_factory_classes['SSHKeyBase']):

    def add(self, name, public_key, wrap=False):
        """ Add sshkeys
        :param name: Name of the key
        :param public_key: SSH Public key string
        :return:
        """
        params = {"name": name, "public_key": public_key}
        result = self.request("account/keys", "POST", params)
        return to_object(result, self.field_map,
                         item_object_factory_classes['SSHKeyObject'], wrap)

    def delete(self, sshkey):
        """ Delete ssh keys
        :param sshkey: sshkey object
        :return: None
        """
        return self.request("account/keys/%s" % sshkey.id, "DELETE")

do_v2_object_classes.update({"SSHKey": SSHKey})
