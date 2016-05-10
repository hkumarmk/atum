from .v2.base import Connection, do_v2_object_factory_classes
from future.utils import viewitems

DIGITALOCEAN_ENDPOINT = "https://api.digitalocean.com/v2/"


class DigitalOcean(object):

    def __init__(self, connection):
        for cls_name, cls in viewitems(do_v2_object_factory_classes):
            setattr(self, cls_name.lower(), cls(connection))


def get_digitalocean(auth, endpoint=DIGITALOCEAN_ENDPOINT):
    """ get_client is the gateway to the provider.
    :param auth: A dictionary with appropriate keys.
    :param endpoint:
    :return:
    """
    connection = Connection(endpoint, auth)
    return DigitalOcean(connection)
