# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gets a comment for a given incident"


class Input:
    INCIDENTCOMMENTID = "incidentCommentId"
    INCIDENTID = "incidentId"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WORKSPACENAME = "workspaceName"
    

class Output:
    COMMENT = "comment"
    

class GetCommentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidentCommentId": {
      "type": "string",
      "title": "Incident Comment ID",
      "description": "Incident Comment ID",
      "order": 1
    },
    "incidentId": {
      "type": "string",
      "title": "Incident ID",
      "description": "Incident ID",
      "order": 2
    },
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription. The name is case insensitive",
      "order": 3
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 4
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 5
    }
  },
  "required": [
    "incidentCommentId",
    "incidentId",
    "resourceGroupName",
    "subscriptionId",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCommentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "$ref": "#/definitions/IncidentComment",
      "title": "Comment",
      "description": "Requested comment",
      "order": 1
    }
  },
  "definitions": {
    "ClientInfo": {
      "type": "object",
      "title": "ClientInfo",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the client",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the client",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object ID",
          "description": "The object id of the client",
          "order": 3
        },
        "userPrincipaName": {
          "type": "string",
          "title": "User Principa Name",
          "description": "The user principal name of the client",
          "order": 4
        }
      }
    },
    "CommentProperties": {
      "type": "object",
      "title": "CommentProperties",
      "properties": {
        "author": {
          "$ref": "#/definitions/ClientInfo",
          "title": "Author",
          "description": "Describes the client that created the comment",
          "order": 1
        },
        "createdTimeUtc": {
          "type": "string",
          "title": "Created Time UTC",
          "displayType": "date",
          "description": "The time the comment was created",
          "format": "date-time",
          "order": 2
        },
        "lastModifiedTimeUtc": {
          "type": "string",
          "title": "Last Modified Time UTC",
          "displayType": "date",
          "description": "The time the comment was updated",
          "format": "date-time",
          "order": 3
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "The comment message",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the resource",
          "order": 5
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "System Data",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
          "order": 6
        }
      },
      "definitions": {
        "ClientInfo": {
          "type": "object",
          "title": "ClientInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the client",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the client",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object ID",
              "description": "The object id of the client",
              "order": 3
            },
            "userPrincipaName": {
              "type": "string",
              "title": "User Principa Name",
              "description": "The user principal name of the client",
              "order": 4
            }
          }
        },
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Indetity",
          "description": "Managed identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "IncidentComment": {
      "type": "object",
      "title": "IncidentComment",
      "properties": {
        "etag": {
          "type": "string",
          "title": "Etag",
          "description": "Entity tag of the resource",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Resource ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the resource",
          "order": 3
        },
        "properties": {
          "$ref": "#/definitions/CommentProperties",
          "title": "Properties",
          "description": "Comment properties",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of the resource",
          "order": 4
        }
      },
      "definitions": {
        "ClientInfo": {
          "type": "object",
          "title": "ClientInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the client",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the client",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object ID",
              "description": "The object id of the client",
              "order": 3
            },
            "userPrincipaName": {
              "type": "string",
              "title": "User Principa Name",
              "description": "The user principal name of the client",
              "order": 4
            }
          }
        },
        "CommentProperties": {
          "type": "object",
          "title": "CommentProperties",
          "properties": {
            "author": {
              "$ref": "#/definitions/ClientInfo",
              "title": "Author",
              "description": "Describes the client that created the comment",
              "order": 1
            },
            "createdTimeUtc": {
              "type": "string",
              "title": "Created Time UTC",
              "displayType": "date",
              "description": "The time the comment was created",
              "format": "date-time",
              "order": 2
            },
            "lastModifiedTimeUtc": {
              "type": "string",
              "title": "Last Modified Time UTC",
              "displayType": "date",
              "description": "The time the comment was updated",
              "format": "date-time",
              "order": 3
            },
            "message": {
              "type": "string",
              "title": "Message",
              "description": "The comment message",
              "order": 4
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the resource",
              "order": 5
            },
            "systemData": {
              "$ref": "#/definitions/SystemData",
              "title": "System Data",
              "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
              "order": 6
            }
          },
          "definitions": {
            "ClientInfo": {
              "type": "object",
              "title": "ClientInfo",
              "properties": {
                "email": {
                  "type": "string",
                  "title": "Email",
                  "description": "The email of the client",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of the client",
                  "order": 2
                },
                "objectId": {
                  "type": "string",
                  "title": "Object ID",
                  "description": "The object id of the client",
                  "order": 3
                },
                "userPrincipaName": {
                  "type": "string",
                  "title": "User Principa Name",
                  "description": "The user principal name of the client",
                  "order": 4
                }
              }
            },
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            },
            "SystemData": {
              "type": "object",
              "title": "SystemData",
              "properties": {
                "createdAt": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "description": "The timestamp of resource creation (UTC)",
                  "format": "date-time",
                  "order": 1
                },
                "createdBy": {
                  "type": "string",
                  "title": "Created By",
                  "description": "The identity that created the resource",
                  "order": 2
                },
                "createdByType": {
                  "$ref": "#/definitions/CreatedByType",
                  "title": "Created By Type",
                  "description": "The type of identity that created the resource",
                  "order": 3
                },
                "lastModifiedAt": {
                  "type": "string",
                  "title": "Last Modified At",
                  "displayType": "date",
                  "description": "The timestamp of resource last modification (UTC)",
                  "format": "date-time",
                  "order": 4
                },
                "lastModifiedBy": {
                  "type": "string",
                  "title": "Last Modified By",
                  "description": "The identity that last modified the resource",
                  "order": 5
                },
                "lastModifiedByType": {
                  "$ref": "#/definitions/CreatedByType",
                  "title": "Last Modified By Type",
                  "description": "The type of identity that last modified the resource",
                  "order": 6
                }
              },
              "definitions": {
                "CreatedByType": {
                  "type": "object",
                  "title": "CreatedByType",
                  "properties": {
                    "Application": {
                      "type": "string",
                      "title": "Application",
                      "description": "Application",
                      "order": 1
                    },
                    "Key": {
                      "type": "string",
                      "title": "Key",
                      "description": "Description",
                      "order": 2
                    },
                    "ManagedIdentity": {
                      "type": "string",
                      "title": "Managed Indetity",
                      "description": "Managed identity",
                      "order": 3
                    },
                    "User": {
                      "type": "string",
                      "title": "User",
                      "description": "User",
                      "order": 4
                    }
                  }
                }
              }
            }
          }
        },
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC)",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "The identity that created the resource",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Created By Type",
          "description": "The type of identity that created the resource",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "Last Modified At",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "The identity that last modified the resource",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Last Modified By Type",
          "description": "The type of identity that last modified the resource",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
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
