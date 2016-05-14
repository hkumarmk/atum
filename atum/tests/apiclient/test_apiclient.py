import unittest
import mock

from atum import apiclient
from atum.apiclient.digitalocean.v2.params import PARAMS
from atum.common import exceptions
from atum.tests.common import *


class APIClientTestCase(unittest.TestCase):

    class FooClass(object):
        def __init__(self, **kwargs):
            pass

    def test_tobject_dict_wrap(self):
        result = apiclient.to_object({"bar": 1}, {"foo": "bar"}, self.FooClass)
        self.assertIsInstance(result, self.FooClass)

    def test_tobject_list_wrap(self):
        result = apiclient.to_object([{"bar": 1}, {"bar": 2}], {"foo": "bar"}, self.FooClass)
        self.assertIsInstance(result[0], self.FooClass)
        self.assertIsInstance(result[1], self.FooClass)

    def digitalocean_to_object_dict_no_wrap(self, object_name):
        field_map = PARAMS[object_name]["field_map"]
        data = digitalocean_output[object_name][0]
        result = apiclient.to_object(data, field_map, wrap=False)
        expected = digitalocean_expected_result[object_name][0]
        self.assertEqual(result, expected)

    def digitalocean_to_object_no_wrap(self, object_name):
        field_map = PARAMS[object_name]["field_map"]
        data = digitalocean_output[object_name]
        result = apiclient.to_object(data, field_map, wrap=False)
        expected = digitalocean_expected_result[object_name]
        self.assertEqual(result, expected)

    def test_digitalocean_to_object_no_wrap(self):
        object_names = ["Flavor", "Image", "Region"]
        for obj in object_names:
            self.digitalocean_to_object_no_wrap(obj)
            self.digitalocean_to_object_dict_no_wrap(obj)

    def test_get_client_with_unknown_provider(self):
        with self.assertRaises(exceptions.UnknownProviderException):
            apiclient.get_client('FooProvider', {"foo": "bar"})

        self.assertTrue("Unknown provider - FooProvider")

    @mock.patch("atum.apiclient.digitalocean.get_digitalocean")
    def test_get_client_digitalocean(self, mock_get_do):
        apiclient.get_client('digitalocean', {"foo": "bar"})
        mock_get_do.assert_called_with({"foo": "bar"})

    def test_item_object_class_factory(self):
        result = apiclient.item_object_class_factory("foo")
        self.assertEqual(apiclient.item_object_factory_classes["foo"], result)
        self.assertIsInstance(result, type)
        self.assertEqual(result.__name__, "foo")
