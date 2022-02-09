import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dDelete import DDelete
from icon_cisco_umbrella_destinations.actions.dDelete.schema import Input
import logging
from unit_test.mock import STUB_CONNECTION, mock_request_200, STUB_DESTINATION_LIST_ID


class TestDDelete(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DDelete()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_successful(self, mock_delete):
        response = self.action.run({Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID, Input.PAYLOAD: '1234 5678'})
        expected_response = {
            "success": {
                "status": {"code": 200, "text": "OK"},
                "data": {
                    "id": 15755711,
                    "organizationId": 2372338,
                    "access": "allow",
                    "isGlobal": False,
                    "name": "CreateListTest",
                    "thirdpartyCategoryId": None,
                    "createdAt": "2022-01-28T16:03:36+0000",
                    "modifiedAt": "2022-02-09T11:47:00+0000",
                    "isMspDefault": False,
                    "markedForDeletion": False,
                    "bundleTypeId": 1,
                    "meta": {"destinationCount": 5},
                },
            }
        }
        self.assertEqual(response, expected_response)
