from atum.apiclient.base import BaseConnection, BaseAPIClient


class Connection(BaseConnection):

    def _set_auth(self):
        """Setting auth header"""
        token = self.auth.get('token', None)
        self.headers.update({"Authorization": "Bearer {:s}".format(token)})


class APIClient(BaseAPIClient):

    def __init__(self, connection):
        super(APIClient, self).__init__(connection)
