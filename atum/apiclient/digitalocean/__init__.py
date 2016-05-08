from atum.apiclient.digitalocean.v2.base import Connection
from atum.apiclient.digitalocean.v2.flavor import Flavor
from atum.apiclient.digitalocean.v2.image import Image
from atum.apiclient.digitalocean.v2.region import Region
from atum.apiclient.digitalocean.v2.server import Server

DIGITALOCEAN_ENDPOINT = "https://api.digitalocean.com/v2/"


class DigitalOcean(object):

    def __init__(self, connection):
        self.flavor = Flavor(connection)
        self.image = Image(connection)
        self.region = Region(connection)
        self.server = Server(connection)


def get_digitalocean(auth, endpoint=DIGITALOCEAN_ENDPOINT):
    """ get_client is the gateway to the provider.
    :param auth: A dictionary with appropriate keys.
    :param endpoint:
    :return:
    """
    connection = Connection(endpoint, auth)
    return DigitalOcean(connection)
