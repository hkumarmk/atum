from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from future.utils import viewitems
from atum.common import exceptions

DIGITALOCEAN = "DigitalOcean"


def to_object(data, field_maps, cls):
    """It does below stuffs
    1. Convert the data to common convention,
    2. Wrap the converted data to provided class
       and return the instance of that class

    :param data: this data should be either a list of dicts or dict itself
    :param field_maps: a dict of mapping values in form of {mapping: original}
    :param cls: Class to which the data to be wrapped
    :return: instance of cls
    """
    if isinstance(data, list):
        for instance in data:
            for mapping, orig in viewitems(field_maps):
                instance[mapping] = instance.pop(orig, None)
        return [cls(**instance) for instance in data]
    elif isinstance(data, dict):
        for mapping, orig in viewitems(field_maps):
            data[mapping] = data.pop(orig, None)
        return cls(**data)


def get_client(provider, auth, endpoint=None):
    """ get_client is the gateway to the provider.
    :param provider: Provider type
    :param auth: A dictionary with appropriate keys for provider auth.
    :param endpoint: Provider endpoint
    :return: provider instance
    """
    if provider == DIGITALOCEAN:
        from atum.apiclient.digitalocean import get_digitalocean
        return get_digitalocean(auth)
    else:
        exceptions.UnknownProviderException("Unknown provider - %s" % provider)
