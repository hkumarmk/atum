from atum.apiclient.digitalocean.flavor import Flavor
from atum.apiclient.common import BaseConnection, BaseAPIClient

DIGITALOCEAN_ENDPOINT = "https://api.digitalocean.com/v2/"


class Connection(BaseConnection):

    def _set_auth(self):
        """Setting auth header"""
        token = self.auth.get('token', None)
        self.headers.update({"Authorization": "Bearer {:s}".format(token)})


class APIClient(BaseAPIClient):

    def __init__(self, connection):
        super(APIClient, self).__init__(connection)


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
