// AB-100 Lab 09 Solution: Modular Bicep for Microsoft Foundry AI Gateway (APIM + PTU/PayGo Failover Pool + App Insights)
targetScope = 'resourceGroup'

@description('Primary Azure region for deployment')
param location string = resourceGroup().location

@description('Unique prefix for enterprise resources')
param prefix string = 'humongous-ai'

@description('Primary PTU Foundry OpenAI Endpoint URL')
param primaryPtuEndpoint string = 'https://foundry-ptu-eastus2.openai.azure.com/openai'

@description('Secondary Pay-As-You-Go Foundry OpenAI Endpoint URL for automatic failover')
param secondaryPayGoEndpoint string = 'https://foundry-paygo-swedencentral.openai.azure.com/openai'

// 1. User-Assigned Managed Identity for Zero-Secret Authentication
resource uami 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${prefix}-gateway'
  location: location
}

// 2. Log Analytics Workspace & Application Insights for Unified Agent Telemetry
resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: 'log-${prefix}-ops'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 90
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appi-${prefix}-telemetry'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
}

// 3. Azure API Management Instance (AI Gateway)
resource apim 'Microsoft.ApiManagement/service@2023-09-01-preview' = {
  name: 'apim-${prefix}-gateway'
  location: location
  sku: {
    name: 'StandardV2'
    capacity: 1
  }
  identity: {
    type: 'SystemAssigned, UserAssigned'
    userAssignedIdentities: {
      '${uami.id}': {}
    }
  }
  properties: {
    publisherEmail: 'aicoe@humongousinsurance.com'
    publisherName: 'Humongous Insurance AI CoE'
  }
}

// 4. Primary Backend (PTU - Priority 1) with Circuit Breaker on HTTP 429/503
resource backendPrimaryPtu 'Microsoft.ApiManagement/service/backends@2023-09-01-preview' = {
  parent: apim
  name: 'foundry-ptu-primary'
  properties: {
    url: primaryPtuEndpoint
    protocol: 'http'
    circuitBreaker: {
      rules: [
        {
          name: 'OpenOnThrottling429'
          failureCondition: {
            count: 1
            interval: 'PT10S'
            statusCodeRanges: [
              { min: 429, max: 429 }
              { min: 500, max: 503 }
            ]
          }
          tripDuration: 'PT30S'
          acceptRetryAfter: true
        }
      ]
    }
  }
}

// 5. Secondary Backend (PayGo - Priority 2 Failover)
resource backendSecondaryPayGo 'Microsoft.ApiManagement/service/backends@2023-09-01-preview' = {
  parent: apim
  name: 'foundry-paygo-secondary'
  properties: {
    url: secondaryPayGoEndpoint
    protocol: 'http'
  }
}

// 6. Priority Load-Balanced Backend Pool (Routes to Priority 1 PTU; overflows to Priority 2 PayGo)
resource backendPool 'Microsoft.ApiManagement/service/backends@2023-09-01-preview' = {
  parent: apim
  name: 'foundry-ptu-paygo-priority-pool'
  properties: {
    type: 'Pool'
    pool: {
      services: [
        {
          id: backendPrimaryPtu.id
          priority: 1
          weight: 100
        }
        {
          id: backendSecondaryPayGo.id
          priority: 2
          weight: 100
        }
      ]
    }
  }
}

output apimGatewayUrl string = apim.properties.gatewayUrl
output appInsightsConnectionString string = appInsights.properties.ConnectionString
