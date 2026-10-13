# Lab 09: Enterprise AI Gateway with Azure API Management (APIM) & Microsoft Foundry

> **AB-100 Exam Alignment:** Domain 3 — Deploy AI-Powered Business Solutions (and Domain 1 Cost/Quota Governance)  
> **Modules Covered:** Module 04, Module 08, Module 10, Module 11  
> **Estimated Time:** 40 minutes  
> **Level:** Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Humongous Insurance** has 8 different business units building agents in **Microsoft Copilot Studio** and **Microsoft Foundry** that all share a central pool of Azure OpenAI / Foundry model deployments and internal **Model Context Protocol (MCP) Servers**.
Last Tuesday, a buggy test loop in the Marketing team's agent consumed 100% of the tenant's **Tokens-Per-Minute (TPM)** quota, causing live Customer Claims agents to fail with `HTTP 429 TooManyRequests`!

As the Lead Solution Architect, you need to deploy an **Enterprise AI Gateway using Azure API Management (APIM)** integrated directly inside **Microsoft Foundry**:
1. **Token Management & Per-Department Rate Limiting (`azure-openai-token-limit`):** Restrict each business unit subscription/agent identity to a strict **Tokens-Per-Minute (TPM)** and **Tokens-Per-Hour** quota so one noisy agent can never starve mission-critical agents.
2. **PTU-to-PayGo Priority Load Balancing & Automatic Circuit-Breaker Failover:** Route traffic to the primary **Provisioned Throughput (PTU)** deployment (`priority: 1`) first; if PTU hits capacity (`HTTP 429` or `503`), automatically fail over to a secondary **Standard Pay-As-You-Go** regional endpoint (`priority: 2`) with zero user-facing errors!
3. **Semantic Caching (`azure-openai-semantic-cache-lookup` / `store`):** Cache responses to semantically identical questions (similarity score $\ge 0.95$) in Azure Managed Redis to reduce latency and save token costs.
4. **Onboarding & Governing MCP Servers Behind the AI Gateway:** Expose enterprise MCP servers through APIM with **Microsoft Entra ID JWT validation (`validate-jwt`)**, rate limiting, and centralized token metrics emitted to **Azure Application Insights**.

---

## 2. Step-by-Step Hands-On Walkthrough

### Task 1: Enable AI Gateway in the Microsoft Foundry Portal (`ai.azure.com`)
1. Sign in to the **Microsoft Foundry Portal** (`https://ai.azure.com`) -> Open the **Management center (Admin / Control Plane)**.
2. Select your Foundry Hub -> Navigate to **AI Gateway (Azure API Management)** -> Select **+ Add AI Gateway**:
   - Link an existing **Azure API Management** instance (or provision one using [`solution/main.bicep`](./solution/main.bicep)).
   - Select the **Foundry Model Deployments** (`gpt-4o-ptu-eastus2`, `gpt-4o-paygo-swedencentral`) and **Connected MCP Servers** to govern through the gateway.

---

### Task 2: Configure the APIM Inbound/Outbound AI Gateway Policy (`apim-ai-gateway-policy.xml`)
1. Open your **Azure API Management** resource in the Azure Portal (`portal.azure.com`) -> Select **APIs -> Foundry AI & MCP Gateway -> All operations -> Inbound processing (Code editor `</>`)**.
2. Apply the production-grade policy in [`solution/apim-ai-gateway-policy.xml`](./solution/apim-ai-gateway-policy.xml), which enforces:
   - **`<validate-jwt>`:** Verifies the caller's **Microsoft Entra Agent ID / OAuth 2.0 Bearer Token** before any model or MCP server is reached.
   - **`<authentication-managed-identity>`:** Acquires an Entra ID token using APIM's **User-Assigned Managed Identity** (`https://cognitiveservices.azure.com`) so callers never possess raw Azure OpenAI API keys!
   - **`<azure-openai-token-limit>`:** Limits each calling application/department (`counter-key="@(context.Subscription.Id)"`) to **15,000 Tokens Per Minute** and **500,000 Tokens Per Hour**, returning `HTTP 429` with `Retry-After` headers only to the offending department.
   - **`<azure-openai-emit-token-metric>`:** Emits `PromptTokens`, `CompletionTokens`, and `TotalTokens` with dimensions for `Subscription ID`, `Agent ID`, and `Client IP` directly to **Azure Monitor / Application Insights** for departmental chargeback!
   - **`<azure-openai-semantic-cache-lookup>` & `<azure-openai-semantic-cache-store>`:** Caches frequent queries for 300 seconds.
   - **Backend Pool Priority Failover (`ptu-primary` -> `paygo-fallback`):** Configured in the Bicep template (`solution/main.bicep`).

---

### Task 3: Onboard an MCP Server into Azure API Management AI Gateway
1. In Azure API Management, select **APIs -> + Add API -> HTTP / OpenAPI** (or **MCP Server** in AI Gateway):
   - **Web service URL:** `https://aca-mcp-treyresearch.internal.azurecontainerapps.io/mcp`
   - **URL suffix:** `mcp`
2. Apply an inbound `<rate-limit-by-key calls="60" renewal-period="60" />` policy and `<validate-jwt>` policy on the `/mcp` route, then give **Microsoft Copilot Studio** and **Microsoft Foundry Agents** the governed APIM gateway URL (`https://apim-humongous-ai.azure-api.net/mcp`).

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/apim-ai-gateway-policy.xml`](./solution/apim-ai-gateway-policy.xml) — Complete Azure API Management AI Gateway XML policy (JWT validation, Managed Identity auth, Token Rate-Limiting, Token Chargeback Metrics, Semantic Caching, and Backend Pool Routing).
- [`solution/main.bicep`](./solution/main.bicep) — Modular Azure Bicep template provisioning User-Assigned Managed Identity, Log Analytics + Application Insights, APIM AI Gateway, and Priority PTU/PayGo Backend Pool with Circuit Breaker failover.
