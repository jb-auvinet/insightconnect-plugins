import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlDelete import DlDelete
from icon_cisco_umbrella_destinations.actions.dlDelete.schema import Input
import json
import logging
from unit_test.mock import STUB_CONNECTION, mock_request_200, STUB_DESTINATION_LIST_ID


class TestDlDelete(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlDelete()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_successful(self, mock_delete):
        response = self.action.run({Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID})
        expected_response = {"success": []}

        self.assertEqual(response, expected_response)
