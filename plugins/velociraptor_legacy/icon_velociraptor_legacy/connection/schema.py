# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_CONNECTION_STRING = "api_connection_string"
    CA_CERTIFICATE = "ca_certificate"
    CLIENT_CERT = "client_cert"
    CLIENT_PRIVATE_KEY = "client_private_key"
    USERNAME = "username"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_connection_string": {
      "type": "string",
      "description": "Velociraptor API Connection Address",
      "order": 2
    },
    "ca_certificate": {
      "$ref": "#/definitions/credential_secret_key",
      "description": "A base64 encoded CA_Certificate Key",
      "order": 3
    },
    "client_cert": {
      "$ref": "#/definitions/credential_secret_key",
      "description": "A base64 encoded Client_Cert Key",
      "order": 4
    },
    "client_private_key": {
      "$ref": "#/definitions/credential_secret_key",
      "description": "A base64 encoded Client_Private Key",
      "order": 5
    },
    "username": {
      "type": "string",
      "description": "User to run command as",
      "order": 1
    }
  },
  "required": [
    "api_connection_string",
    "ca_certificate",
    "client_cert",
    "client_private_key",
    "username"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
