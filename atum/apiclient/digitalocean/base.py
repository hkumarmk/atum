from atum.apiclient.digitalocean import Connection
from atum.apiclient.digitalocean.flavor import Flavor

DIGITALOCEAN_ENDPOINT = "https://api.digitalocean.com/v2/"


class DigitalOcean(object):

    def __init__(self, connection):
        self.flavor = Flavor(connection)


def get_client(auth, endpoint=DIGITALOCEAN_ENDPOINT):
    """ get_client is the gateway to the provider.
    :param auth: A dictionary with appropriate keys.
    :param endpoint:
    :return:
    """
    connection = Connection(endpoint, auth)
    return DigitalOcean(connection)