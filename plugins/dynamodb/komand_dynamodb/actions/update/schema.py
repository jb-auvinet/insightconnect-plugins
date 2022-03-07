# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an object in Dyanmo"


class Input:
    CONDITION_EXPRESSION = "condition_expression"
    EXPRESSION_ATTRIBUTE_NAMES = "expression_attribute_names"
    EXPRESSION_ATTRIBUTE_VALUES = "expression_attribute_values"
    KEY = "key"
    RETURN_CONSUMED_CAPACITY = "return_consumed_capacity"
    RETURN_ITEM_COLLECTION_METRICS = "return_item_collection_metrics"
    RETURN_VALUES = "return_values"
    TABLE_NAME = "table_name"
    UPDATE_EXPRESSION = "update_expression"
    

class Output:
    SUCCESS = "success"
    

class UpdateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "condition_expression": {
      "type": "string",
      "title": "Condition Expression",
      "description": "An optional expression that can be used to reject updates based on evaluating existing data",
      "order": 3
    },
    "expression_attribute_names": {
      "type": "object",
      "title": "Expression Attribute Names",
      "description": "One or more substitution tokens for attribute names in an expression",
      "order": 8
    },
    "expression_attribute_values": {
      "type": "object",
      "title": "Expression Attribute Values",
      "description": "One or more values that can be substituted in an expression",
      "order": 9
    },
    "key": {
      "type": "object",
      "title": "Key",
      "description": "The primary key and optionally the sort key of the object to update. Provided as a pair of key/values",
      "order": 2
    },
    "return_consumed_capacity": {
      "type": "string",
      "title": "Return Consumed Capacity",
      "description": "Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response",
      "enum": [
        "INDEXES",
        "TOTAL"
      ],
      "order": 5
    },
    "return_item_collection_metrics": {
      "type": "boolean",
      "title": "Return Item Collection Metrics",
      "description": "Determines whether item collection metrics are returned",
      "order": 6
    },
    "return_values": {
      "type": "string",
      "title": "Return Values",
      "description": "Use ReturnValues if you want to get the item attributes as they appear before or after they are updated",
      "enum": [
        "ALL_OLD",
        "UPDATE_OLD",
        "ALL_NEW",
        "UPDATED_NEW"
      ],
      "order": 4
    },
    "table_name": {
      "type": "string",
      "title": "Table Name",
      "description": "The table name to store into",
      "order": 1
    },
    "update_expression": {
      "type": "string",
      "title": "Update Expression",
      "description": "An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them",
      "order": 7
    }
  },
  "required": [
    "key",
    "table_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
