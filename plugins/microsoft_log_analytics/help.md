# Description

Edit, run log queries with data in Azure Monitor Logs

# Key Features

* Send Log Data
* Get Log Data
* Create or Update Saved Search
* Get Saved Search
* Delete Saved Search
* List All Saved Searches
* Search Trigger

# Requirements

Requires Azure workspace and client credentials from Azure Portal such as client ID, subscription ID, tenant ID, client secret key, resouce group name and workspace name.

# Supported Product Versions

* 2022-03-18

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|tenant_id|string|None|True|This is Active Directory ID|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|

Example input:

```
{
  "client_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "client_secret": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "tenant_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

## Technical Details

### Actions

#### Create or Update Saved Search

This action creates or updates a saved search for a given workspace.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|properties|properties|None|True|Saved search properties object|None|{"properties":{"category":"Saved Search Test Category","displayName":"Create or Update Saved Search Test","functionAlias":"heartbeat_func","functionParameters":"a:int=1","query":"Heartbeat | summarize Count() by Computer | take a","tags":[{"name":"Group","value":"Computer"}]}}|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|saved_search_name|string|None|True|Name of the saved search (case sensitive)|None|ExampleSavedSearchName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "properties": "{\"properties\":{\"category\":\"Saved Search Test Category\",\"displayName\":\"Create or Update Saved Search Test\",\"functionAlias\":\"heartbeat_func\",\"functionParameters\":\"a:int=1\",\"query\":\"Heartbeat | summarize Count() by Computer | take a\",\"tags\":[{\"name\":\"Group\",\"value\":\"Computer\"}]}}",
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|Fully qualified resource ID for the resource|
|name|string|True|Saved search name|
|properties|properties|True|Saved search properties object|

Example output:

```
```

#### Delete Saved Search by Name

This action deletes the specified saved search in a given workspace.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|saved_search_name|string|None|True|Name of the saved search (case sensitive)|None|ExampleSavedSearchName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted_saved_search|saved_search|True|Data of deleted saved search|
|message|string|True|Text message indicates that log data has been added to workspace|

Example output:

```
{
  "message": "Saved search ExampleSavedSearchName has been deleted",
  "deleted_saved_search": {
    "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/ExampleSavedSearchName",
    "name": "ExampleSavedSearchName",
    "properties": {
      "category": " Saved Search Test Category",
      "displayName": "Delete Saved Search Example",
      "query": "* | where TimeGenerated > ago(1h)"
    }
  }
}
```

#### Get Saved Search

This action gets the saved searche from Log Analytics by it's name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|saved_search_name|string|None|True|Name of the saved search (case sensitive)|None|ExampleSavedSearchName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|Fully qualified resource ID for the resource|
|name|string|True|Saved search name|
|properties|properties|True|Saved search properties object|

Example output:

```
{
  "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/ExampleSavedSearchName",
  "name": "ExampleSavedSearchName",
  "properties": {
    "category": " Saved Search Test Category",
    "displayName": "Get Saved Search Example",
    "query": "* | where TimeGenerated > ago(1h)"
  }
}
```

#### List All Searches

This action gets the saved searches for a given Log Analytics workspace.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|saved_searches|[]saved_search|True|List of found saved searches results|

Example output:

```
{
  "saved_searches": [
    {
      "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2015",
      "name": "test-new-saved-search-id-2015",
      "properties": {
        "category": " Saved Search Test Category",
        "displayName": "Create or Update Saved Search Test",
        "query": "* | measure Count() by Computer",
        "tags": [
          {
            "name": "Group",
            "value": "Computer"
          }
        ]
      }
    },
    {
      "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2016",
      "name": "test-new-saved-search-id-2016",
      "properties": {
        "category": " Saved Search Test 2",
        "displayName": "Simple Test",
        "query": "TimeGenerated"
      }
    },
    {
      "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2017",
      "name": "test-new-saved-search-id-2017",
      "properties": {
        "category": " Saved Search Test 2",
        "displayName": "Simple Test",
        "query": "TimeGenerated"
      }
    }
  ]
}
```

#### Get Log Data

This action retrieves log data from Log Analytics workspace in Azure Monitor by a specific query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Microsoft Log Analytics query|None|AzureActivity I summarize count() by Category|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "query": "AzureActivity I summarize count() by Category",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tables|[]table|True|Array of tables representing the query result, with each table containing a name, columns and rows keys|

Example output:

```
{
  "tables": [
    {
      "name": "PrimaryResult",
      "columns": [
        {
          "name": "Category",
          "type": "string"
        },
        {
          "name": "count_l",
          "type": "long"
        }
      ],
      "rows": [
        {
          "Category": "Administrative",
          "count_l": 20839
        },
        {
          "Category": "Recommendation",
          "count_l": 122
        },
        {
          "Category": "Alert",
          "count_l": 64
        },
        {
          "Category": "ServiceHealth",
          "count_l": 11
        }
      ]
    }
  ]
}
```

#### Send Log Data

This action sends log data to a Log Analytics workspace in Azure Monitor.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|log_data|[]object|None|True|JSON log data body that must include one or more records with the property name and value pairs in the following format, the property name can contain only letters, numbers, and the underscore (_) character|None|[{"property 1": "value1", "property 2": "value2", "property 3": "value3", "property 4": "value4"},{"property 1": "value1", "property 2": "value2", "property 3": "value3", "property 4": "value4"}]|
|log_type|string|None|True|Specify the record type of the data that's being submitted, that can contain only letters, numbers, and the underscore (_) character, and it can't exceed 100 characters|None|MyExampleRecordType|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "log_data": [
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    },
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    }
  ],
  "log_type": "MyExampleRecordType",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log_data|[]object|True|Data that has been sent|
|message|string|True|Text message indicates that log data has been added to workspace|

Example output:

```
{
  "message": "Log data has been added",
  "log_data": [
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    },
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    }
  ]
}
```

### Triggers

#### Search

This trigger is used to run Log Analytics query every interval time (expressed in seconds).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|60|True|Integer value that represents interval time in seconds|None|60|
|query|string|None|True|Microsoft Log Analytics query|None|AzureActivity I summarize count() by Category|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|
|subscription_id|string|None|True|Current subscription identifier that Azure application portal assigned to|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|workspace_name|string|None|True|Customer's workspace name that the application registration portal is assigned|None|ExampleWorkspaceName|

Example input:

```
{
  "interval": 60,
  "query": "AzureActivity I summarize count() by Category",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tables|[]table|True|Array of tables representing the query result, with each table containing a name, columns and rows keys|

Example output:

```
{
  "tables": [
    {
      "name": "PrimaryResult",
      "columns": [
        {
          "name": "Category",
          "type": "string"
        },
        {
          "name": "count_l",
          "type": "long"
        }
      ],
      "rows": [
        {
          "Category": "Administrative",
          "count_l": 20839
        },
        {
          "Category": "Recommendation",
          "count_l": 122
        },
        {
          "Category": "Alert",
          "count_l": 64
        },
        {
          "Category": "ServiceHealth",
          "count_l": 11
        }
      ]
    }
  ]
}
```

### Custom Output Types

#### column

| Name      |Type|Required|Description|
|-----------|----|--------|-----------|
| Name      |string|False|Column's name|
| Data Type |string|False|Column's data type|

#### table

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Columns|[]column|False|Table's columns|
|Name|string|False|Table's name|
|Rows|[]object|False|Table's rows|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - Added new actions (Actions: Create or Update Saved Search, Get Saved Search, Delete Saved Search, List All Saved Searches)
* 1.1.0 - Search trigger thats run Log Analytics query every interval time
* 1.0.0 - Initial plugin (Actions: Get Log Data, Send Log Data)

# Links

## References

* [Microsoft Azure Portal](https://azure.microsoft.com/en-us/features/azure-portal/)
* [Microsoft Log Analytics Data Collector API](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
* [Microsoft Log Analytics Query API](https://docs.microsoft.com/en-gb/azure/azure-monitor/logs/api/overview)

