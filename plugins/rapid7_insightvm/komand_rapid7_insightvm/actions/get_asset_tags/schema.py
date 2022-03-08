# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a listing of all tags for an asset"


class Input:
    ASSET_ID = "asset_id"
    

class Output:
    TAGS = "tags"
    

class GetAssetTagsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_id": {
      "type": "integer",
      "title": "Asset ID",
      "description": "Identifier of asset",
      "order": 1
    }
  },
  "required": [
    "asset_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAssetTagsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "List of tags",
      "items": {
        "$ref": "#/definitions/tag"
      },
      "order": 1
    }
  },
  "required": [
    "tags"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    },
    "tag": {
      "type": "object",
      "title": "tag",
      "properties": {
        "color": {
          "type": "string",
          "title": "Color",
          "description": "Tag color",
          "order": 1
        },
        "created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "description": "Tag creation date",
          "format": "date-time",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Tag ID",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Tag name",
          "order": 5
        },
        "riskModifier": {
          "type": "string",
          "title": "Risk Modifier",
          "description": "Tag risk score modifier",
          "order": 6
        },
        "searchCriteria": {
          "type": "object",
          "title": "Search Criteria",
          "description": "Tag search criteria",
          "order": 7
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Tag source",
          "order": 8
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Tag type",
          "order": 9
        }
      },
      "required": [
        "id",
        "name",
        "type"
      ],
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "URL",
              "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Link relation type following RFC 5988",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
