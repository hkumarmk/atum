from .v2 import Connection, do_v2_object_classes, ENDPOINT
from future.utils import viewitems


class DigitalOcean(object):

    def __init__(self, connection):
        for cls_name, cls in viewitems(do_v2_object_classes):
            setattr(self, cls_name.lower(), cls(connection))


def get_digitalocean(auth, endpoint=ENDPOINT):
    """ get_client is the gateway to the provider.
    :param auth: A dictionary with appropriate keys.
    :param endpoint:
    :return:
    """
    connection = Connection(endpoint, auth)
    return DigitalOcean(connection)
