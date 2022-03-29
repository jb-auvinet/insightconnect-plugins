import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_palo_alto_cortex_xdr.connection import Connection
from icon_palo_alto_cortex_xdr.connection.schema import Input
import logging
import json


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_KEY: {"secretKey": "api_key"},
            Input.API_KEY_ID: 1,
            Input.SECURITY_LEVEL: "Standard",
            Input.URL: "example.com",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = ""

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("url") == "https://example.com/public_api/v1/incidents/get_incidents/":
            return MockResponse("get_incidents", 200)
        raise Exception("Not implemented")
