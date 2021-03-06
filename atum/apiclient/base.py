from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from future.moves.urllib.parse import urljoin
from future.utils import with_metaclass, viewitems

from abc import ABCMeta, abstractmethod

import json
import requests

from atum.common import exceptions


class AtumBase(object):

    def __init__(self):
        self.field_map = {}
        self.object_class = None

    def list(self, filters=None, wrap=True):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def _filter(self, filters, data):

        for m, o in viewitems(self.field_map):
            if m in filters and o not in filters:
                filters[o] = filters.pop(m, None)

        return [i for i in data
                if all([True if i.get(k) == v else False
                        for k, v in viewitems(filters)])]

    def get(self, id_, wrap=True, dc=None):
        filters = {'id': id_}
        obj = self.list(filters, wrap, dc)
        if obj:
            return obj[0]

    @staticmethod
    def to_json(data):
        return json.dumps(data)


class BaseConnection(with_metaclass(ABCMeta)):
    def __init__(self, endpoint, auth, content_type="application/json"):
        """ Create a session and populate headers
        :param endpoint: cloud endpoint
        :param auth: authentication credentials, it is a dictionary with
                     appropriate keys
        :param content_type: requests content_type, which may be overridden
                             if required
        """
        self.endpoint = endpoint
        self.auth = auth
        self.content_type = content_type
        self.headers = {"content-type": content_type}
        self._set_auth()
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    @abstractmethod
    def _set_auth(self):
        pass


class BaseAPIClient(object):

    def __init__(self, connection):
        self.connection = connection
        self.session = self.connection.session

    def _get(self, url, params=None):
        return self.session.get(url)

    def _post(self, url, params):
        return self.session.post(url, data=json.dumps(params))

    def _put(self, url, params):
        self.session.params = params
        return self.session.put(url)

    def _delete(self, url, params):
        self.session.params = params
        return self.session.delete(url)

    def _head(self, url, params=None):
        return self.session.head(url)

    def _request(self, url, method, params):
        methods = {
            "GET": self._get,
            "POST": self._post,
            "PUT": self._put,
            "DELETE": self._delete,
            "HEAD": self._head
        }

        request_method = methods[method.upper()]
        url = urljoin(self.connection.endpoint, url)

        return request_method(url, params=params)

    def request(self, url, method, params=None):
        params = params or {}

        response = self._request(url, method, params)

        if response.status_code == 204:
            result = ""
        else:
            try:
                result = response.json()
            except ValueError:
                raise exceptions.JSONDecodeError()

            if not response.ok:
                if response.status_code >= 500:
                    raise exceptions.APIResponseError(
                        "Server response error. {:d} {:s}".format(
                            response.status_code, response.reason))
                if response.status_code == 404:
                    raise exceptions.APIResourceNotFoundError

                raise exceptions.APIRequestError("{:d} {:s}. Message: {:s}".format(
                    response.status_code, response.reason, result["message"]))

        return result


class BaseObject(object):
    """A Base class to derive all *Object classes
    to wrap the data got from get requests"""
    def __init__(self, **kwargs):
        for k, v in viewitems(kwargs):
            setattr(self, k, v)
