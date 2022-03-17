# Description

Azure Sentinel is Microsoft's' automated security service.

# Key Features

* Creating and updating incidents
* Deleting incidents
* Retriveing incident's details
* Listing incidents for a given workspace
* Listing bookmarks for a given incident
* Listing alerts for a given incident

# Requirements

* Set of credentials with necessary permissions to monitor and modify Sentinel incidents

# Supported Product Versions

* 2021-04-01

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|c163eff0-d1a1-4618-ee2a-453534f43cee|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|ef50c6bx9umaik9agvoxtoqec2fg9f0y|
|tenant_id|string|None|True|This is active directory ID|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|

Example input:

```
{
  "client_id": "c163eff0-d1a1-4618-ee2a-453534f43cee",
  "client_secret": "ef50c6bx9umaik9agvoxtoqec2fg9f0y",
  "tenant_id": "5ceea899-ae8c-4ff1-fffe-353646eeeff0"
}
```

## Technical Details

### Actions

#### List Entities

This action is used to get all incidents entities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]Entity|False|All the entities assigned to the given incident|

Example output:

```
{
  "entities": []
}
```

#### List Incidents

This action is used to list all the incidents matching specified criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|orderBy|string|None|False|Field to sort results by|None|properties/createdTimeUtc desc|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case-insensitive|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "orderBy": "properties/createdTimeUtc desc",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]Incident|False|List of incidents objects|

Example output:
```
{
  "incidents":[
    {
      "id":"/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "name":"1407186457",
      "etag":"\"8701a4d2-0000-0100-0000-621666620000\"",
      "type":"Microsoft.SecurityInsights/Incidents",
      "properties":{
        "title":"Test incident",
        "description":"This is a demo incident",
        "severity":"Low",
        "status":"Closed",
        "classification":"FalsePositive",
        "classificationReason":"IncorrectAlertLogic",
        "classificationComment":"Not a malicious activity",
        "labels":[],
        "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
        "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
        "lastModifiedTimeUtc":"2022-02-23T16:52:50.1945053Z",
        "createdTimeUtc":"2022-02-23T16:52:50.1945053Z",
        "incidentNumber":3,
        "additionalData":{
          "alertsCount":0,
          "bookmarksCount":0,
          "commentsCount":0,
          "alertProductNames":[]
        },
        "relatedAnalyticRuleIds":[],
        "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/eeeee-eeee-eee-eeee-df965e27aefe/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457"
      }
    }
  ]
}
```
#### Create or Update Incident

This action this action creates or updates an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|etag|string|None|False|Etag of the azure resource|None|0300bf09-0000-0000-0000-5c37296e0000|
|incidentId|string|None|True|Incident ID|None|incident-14071867|
|properties|IncidentProperties|None|True|Incident properties object|None|{'status': 'Closed'}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case-insensitive|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident-14071867",
  "etag": "1234",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "workspaceName": "workspace23",
  "properties":{
    "title":"Incident At Work",
    "description":"This is a demo incident"
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False|Etag|
|id|string|False|Full incident ID|
|name|string|False|Incident name - short ID|
|properties|IncidentProperties|False|Incident properties object|
|type|string|False|Type|

Example output:

```
{
  "id":"/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "name":"14071867",
  "etag":"\"8f04f1b4-0000-0100-0000-62275ef30000\"",
  "type":"Microsoft.SecurityInsights/Incidents",
  "properties":{
    "title":"Incident At Work",
    "description":"This is a demo incident",
    "severity":"High",
    "status":"Closed",
    "classification":"FalsePositive",
    "classificationReason":"IncorrectAlertLogic",
    "classificationComment":"Not a malicious activity",
    "owner":{
      "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70"
    },
    "labels":[
      
    ],
    "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
    "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
    "lastModifiedTimeUtc":"2022-03-08T13:49:39.1064183Z",
    "createdTimeUtc":"2022-02-09T13:05:21.7201975Z",
    "incidentNumber":2,
    "additionalData":{
      "alertsCount":0,
      "bookmarksCount":0,
      "commentsCount":0,
      "alertProductNames":[
        
      ],
      "tactics":[
        
      ]
    },
    "relatedAnalyticRuleIds":[
      
    ],
    "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867"
  }
}
```

#### Delete Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case-insensitive|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Deletion status, 200 - ok, 204 - no content|

Example output:

```
{
  "status": 204
}
```

#### List Alerts

This action is used to get all incidents alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case-insensitive|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspacename12|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspacename12"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]Alert|False|All the alerts assigned to the given incident|

Example output:

```
{
  "alerts":[
    {
      "id":"/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRG/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Entities/baa8a239-6fde-4ab7-a093-d09f7b75c58c",
      "name":"baa8a239-6fde-4ab7-a093-d09f7b75c58c",
      "type":"Microsoft.SecurityInsights/Entities",
      "kind":"SecurityAlert",
      "properties":{
        "systemAlertId":"baa8a239-6fde-4ab7-a093-d09f7b75c58c",
        "tactics":[
          
        ],
        "alertDisplayName":"myAlert",
        "confidenceLevel":"Unknown",
        "severity":"Low",
        "vendorName":"Microsoft",
        "productName":"Azure Security Center",
        "alertType":"myAlert",
        "processingEndTime":"2020-07-20T18:21:53.6158361Z",
        "status":"New",
        "endTimeUtc":"2020-07-20T18:21:53.6158361Z",
        "startTimeUtc":"2020-07-20T18:21:53.6158361Z",
        "timeGenerated":"2020-07-20T18:21:53.6158361Z",
        "resourceIdentifiers":[
          {
            "type":"LogAnalytics",
            "workspaceId":"c8c99641-985d-4e4e-8e91-fb3466cd0e5b",
            "subscriptionId":"bd794837-4d29-4647-9105-6339bfdb4e6a",
            "resourceGroup":"myRG"
          }
        ],
        "additionalData":{
          "AlertMessageEnqueueTime":"2020-07-20T18:21:57.304Z"
        },
        "friendlyName":"myAlert"
      }
    }
  ]
}
```

#### Get Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case-insensitive|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False|Etag of the incident|
|id|string|False|Full incident ID|
|name|string|False|Incident name - short ID|
|properties|IncidentProperties|False|Incident properties object|
|type|string|False|Type of the incident|

Example output:

```
{
  "id":"/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "name":"14071867",
  "etag":"\"8f04f1b4-0000-0100-0000-62275ef30000\"",
  "type":"Microsoft.SecurityInsights/Incidents",
  "properties":{
    "title":"Incident At Work",
    "description":"This is a demo incident",
    "severity":"High",
    "status":"Closed",
    "classification":"FalsePositive",
    "classificationReason":"IncorrectAlertLogic",
    "classificationComment":"Not a malicious activity",
    "owner":{
      "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70"
    },
    "labels":[
      
    ],
    "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
    "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
    "lastModifiedTimeUtc":"2022-03-08T13:49:39.1064183Z",
    "createdTimeUtc":"2022-02-09T13:05:21.7201975Z",
    "incidentNumber":2,
    "additionalData":{
      "alertsCount":0,
      "bookmarksCount":0,
      "commentsCount":0,
      "alertProductNames":[
        
      ],
      "tactics":[
        
      ]
    },
    "relatedAnalyticRuleIds":[
      
    ],
    "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867"
  }
}
```

#### List Bookmarks

This action is used to get all incidents bookmarks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bookmarks|[]HuntingBookmark|False|All the bookmarks assigned to the given incident|

Example output:

```
{
  "bookmarks":[
    {
      "id":"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/afbd324f-6c48-459c-8710-8d1e1cd03812",
      "name":"afbd324f-6c48-459c-8710-8d1e1cd03812",
      "type":"Microsoft.SecurityInsights/Entities",
      "kind":"Bookmark",
      "properties":{
        "displayName":"SecurityEvent - 868f40f4698d",
        "created":"2020-06-17T15:34:01.4265524+00:00",
        "updated":"2020-06-17T15:34:01.4265524+00:00",
        "createdBy":{
          "objectId":"b03ca914-5eb6-45e5-9417-fe0797c372fd",
          "email":"user@example.com",
          "name":"user"
        },
        "updatedBy":{
          "objectId":"b03ca914-5eb6-45e5-9417-fe0797c372fd",
          "email":"user@example.com",
          "name":"user"
        },
        "eventTime":"2020-06-17T15:34:01.4265524+00:00",
        "labels":[
          
        ],
        "query":"SecurityEvent\r\n| take 1\n",
        "queryResult":"{\"TimeGenerated\":\"2020-05-24T01:24:25.67Z\",\"Account\":\"\\\\ADMINISTRATOR\",\"AccountType\":\"User\",\"Computer\":\"SecurityEvents\",\"EventSourceName\":\"Microsoft-Windows-Security-Auditing\",\"Channel\":\"Security\",\"Task\":12544,\"Level\":\"16\",\"EventID\":4625,\"Activity\":\"4625 - An account failed to log on.\",\"AuthenticationPackageName\":\"NTLM\",\"FailureReason\":\"%%2313\",\"IpAddress\":\"176.113.115.73\",\"IpPort\":\"0\",\"LmPackageName\":\"-\",\"LogonProcessName\":\"NtLmSsp \",\"LogonType\":3,\"LogonTypeName\":\"3 - Network\",\"Process\":\"-\",\"ProcessId\":\"0x0\",\"__entityMapping\":{\"\\\\ADMINISTRATOR\":\"Account\",\"SecurityEvents\":\"Host\"}}",
        "additionalData":{
          "ETag":"\"3b00acab-0000-0d00-0000-5f15e4ed0000\"",
          "EntityId":"afbd324f-6c48-459c-8710-8d1e1cd03812"
        },
        "friendlyName":"SecurityEvent - 868f40f4698d"
      }
    }
  ]
}
```
### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### CreatedByType

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Application|string|False|Application|
|Key|string|False|Description|
|Managed Indetity|string|False|Managed Identity|
|User|string|False|User|

#### Incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False|None|
|Full Incident ID|string|False|Full incident ID|
|Incident ID|string|False|Incident name - short id|
|Incident properties|IncidentProperties|False|Incident properties object.|
|type|string|False|None|

#### IncidentAdditionalData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|List of product names of alerts in the incident|[]string|False|List of product names of alerts in the incident|
|The number of alerts in the incident|integer|False|The number of alerts in the incident|
|The number of bookmarks in the incident|integer|False|The number of bookmarks in the incident|
|The number of comments in the incident|integer|False|The number of comments in the incident|
|The tactics associated with incident|[]string|False|The tactics associated with incident|

#### IncidentLabel

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The name of the label|string|False|The name of the label|
|The type of label|string|False|The type of label.|

#### IncidentOwnerInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The name of the user the incident is assigned to.|string|False|The name of the user the incident is assigned to.|
|The email of the user the incident is assigned to.|string|False|The email of the user the incident is assigned to.|
|The object id of the user the incident is assigned to.|string|False|The object id of the user the incident is assigned to.|
|The user principal name of the user the incident is assigned to.|string|False|The user principal name of the user the incident is assigned to.|

#### IncidentProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional data on the incident|IncidentAdditionalData|False|Additional data on the incident|
|The reason the incident was closed|string|False|The reason the incident was closed|
|Describes the reason the incident was closed|string|False|Describes the reason the incident was closed|
|The classification reason the incident was closed with|string|False|The classification reason the incident was closed with|
|The time the incident was created|string|False|The time the incident was created|
|The description of the incident|string|False|The description of the incident|
|Etag of the azure resource|string|False|Etag of the azure resource|
|The time of the first activity in the incident|string|False|The time of the first activity in the incident|
|Azure resource Id|string|False|Azure resource Id|
|A sequential number|integer|False|A sequential number|
|The deep-link URL to the incident in Azure portal|string|False|The deep-link URL to the incident in Azure portal|
|List of labels relevant to this incident|[]IncidentLabel|False|List of labels relevant to this incident|
|The time of the last activity in the incident|string|False|The time of the last activity in the incident|
|The last time the incident was updated|string|False|The last time the incident was updated|
|Azure resource name|string|False|Azure resource name|
|Describes a user that the incident is assigned to|IncidentOwnerInfo|False|Describes a user that the incident is assigned to|
|List of resource ids of Analytic rules related to the incident|[]string|False|List of resource ids of Analytic rules related to the incident|
|Incidents severity|string|True|Incidents severity|
|Incidents status|string|True|Incidents status|
|Azure Resource Manager metadata containing createdBy and modifiedBy information.|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information.|
|The title of the incident|string|False|The title of the incident|
|Azure resource type|string|False|Azure resource type|

#### SystemData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The timestamp of resource creation (UTC).|date|False|The timestamp of resource creation (UTC).|
|The identity that created the resource.|string|False|The identity that created the resource.|
|The type of identity that created the resource.|CreatedByType|False|The type of identity that created the resource.|
|The timestamp of resource last modification (UTC)|date|False|The timestamp of resource last modification (UTC)|
|The identity that last modified the resource.|string|False|The identity that last modified the resource.|
|The type of identity that last modified the resource.|CreatedByType|False|The type of identity that last modified the resource.|

#### UserInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|The email of the user.|
|Name|string|False|The name of the user.|
|Object Identification|string|False|The object id of the user.|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin Initial plugin (Actions: Create or Update Incident, Delete Incident, List Incidents, Get Incident, List Alerts, List Bookmarks, List Entities)

# Links

## References

* [Microsoft's Sentinel](https://docs.microsoft.com/en-us/rest/api/securityinsights/)
* [Incidents](https://docs.microsoft.com/en-us/azure/sentinel/investigate-cases)
* [Incidents REST API](https://docs.microsoft.com/pl-pl/rest/api/securityinsights/stable/incidents)

