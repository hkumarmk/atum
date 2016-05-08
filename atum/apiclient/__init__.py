from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from future.utils import viewitems
from atum.common import exceptions

DIGITALOCEAN = "digitalocean"


def to_object(data, field_maps, cls, wrap=False):
    """It does below stuffs
    1. Convert the data to common convention,
    2. Wrap the converted data to provided class
       and return the instance of that class

    :param data: this data should be either a list of dicts or dict itself
    :param field_maps: a dict of mapping values in form of {mapping: original}
    :param cls: Class to which the data to be wrapped
    :param wrap: Whether to wrap the data in the class or not
    :return: instance of cls
    """
    if isinstance(data, list):
        new_data = []
        for instance in data:
            new_data.append({
                mapping: instance.get(orig, None) for mapping, orig in viewitems(field_maps)
            })
        if wrap:
            return [cls(**instance) for instance in new_data]
        else:
            return new_data
    elif isinstance(data, dict):
        new_data = {mapping: data.get(orig, None) for mapping, orig in viewitems(field_maps)}
        if wrap:
            return cls(**new_data)
        else:
            return new_data


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
