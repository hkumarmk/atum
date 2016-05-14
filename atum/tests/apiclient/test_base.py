import unittest

from atum.apiclient import base
from atum.apiclient.digitalocean.v2.params import PARAMS
from atum.tests.common import digitalocean_output

atum_base = base.AtumBase()

class APIClientBaseTestCase(unittest.TestCase):

    def _filter(self, filters, data, expected_result):

        atum_base.field_map = PARAMS["Flavor"]["field_map"]
        result = atum_base._filter(filters, data)
        self.assertEqual(result, expected_result)

    def test_filters(self):
        inputs = [
            {
                "filters": {"memory": 512, "vcpus": 1},
                "data": digitalocean_output["Flavor"],
                "expected_result": [digitalocean_output["Flavor"][0]],
            },
            {
                "filters": {"memory": 1024, "vcpus": 1},
                "data": digitalocean_output["Flavor"],
                "expected_result": [digitalocean_output["Flavor"][1]],
            },
            {
                "filters": {"vcpus": 1},
                "data": digitalocean_output["Flavor"],
                "expected_result": digitalocean_output["Flavor"],
            },
            {
                "filters": {},
                "data": digitalocean_output["Flavor"],
                "expected_result": digitalocean_output["Flavor"],
            }
        ]
        for input in inputs:
            self._filter(**input)

    def test_to_json(self):
        json_data = '[{"foo": ["bar"]}, {"is_true": true}]'
        data = [
            {"foo": ["bar"]},
            {"is_true": True}
        ]
        self.assertEqual(atum_base.to_json(data), json_data)
