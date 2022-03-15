# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Download modified file by URL"


class Input:
    
    IS_VERIFY = "is_verify"
    POLL = "poll"
    URL = "url"
    USER_AGENT = "user_agent"
    

class Output:
    
    BYTES = "bytes"
    STATUS_CODE = "status_code"
    

class PollFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "is_verify": {
      "type": "boolean",
      "title": "Is Verify",
      "description": "Validate certificate",
      "default": true,
      "order": 3
    },
    "poll": {
      "type": "integer",
      "title": "Poll",
      "description": "Poll in seconds",
      "default": 60,
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to Download",
      "order": 1
    },
    "user_agent": {
      "type": "string",
      "title": "User Agent",
      "description": "Send requests with user agent",
      "default": "Mozilla/5.0",
      "order": 4
    }
  },
  "required": [
    "is_verify",
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PollFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bytes": {
      "type": "string",
      "title": "Base64 Encoded File",
      "displayType": "bytes",
      "description": "Bytes",
      "format": "bytes",
      "order": 1
    },
    "status_code": {
      "type": "integer",
      "title": "Status Codes",
      "description": "Status code",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
