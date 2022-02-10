import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from ..icon_cisco_umbrella_destinations.actions.dlCreate import DlCreate
from icon_cisco_umbrella_destinations.actions.dlCreate.schema import Input
import json
import logging
from unit_test.mock import STUB_CONNECTION, mock_request_200, STUB_DESTINATION_LIST_ID


class TestDlCreate(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlCreate()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.data = {
            "access": "allow",
            "isGlobal": True,
            "name": "NewName",
        }

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_successful(self, mock_post):
        response = self.action.run()
        expected_response = []