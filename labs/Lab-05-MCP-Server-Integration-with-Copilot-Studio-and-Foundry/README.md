# Lab 05: Building an Enterprise Model Context Protocol (MCP) Server & Integrating with Copilot Studio and Microsoft Foundry

> **AB-100 Exam Alignment:** Domain 2 — Design AI-Powered Business Solutions (Design Extensibility with MCP)  
> **Modules Covered:** Module 03 & Module 06  
> **Estimated Time:** 40 minutes  
> **Level:** Intermediate to Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Trey Research** wants to standardize how its internal microservices and Microsoft Learn skilling catalogs are exposed to **Microsoft Copilot Studio** and **Microsoft Foundry** agents. Instead of manually authoring and maintaining separate Power Platform custom connector actions every time a backend API changes, you need to design and deploy a **Model Context Protocol (MCP) Server**.

In this lab, you will:
1. **Build an Enterprise MCP Server in Python (`mcp_enterprise_server.py`):**
   - Expose **MCP Tool 1 (`generate_certification_study_plan`):** Generates a structured **3-month study plan** (for **AB-100** or **AI-102**) grounded in official Microsoft Learn modules based on the learner's weekly study hours and domain confidence scores.
   - Expose **MCP Tool 2 (`check_realtime_erp_stock`):** Queries live warehouse inventory and lead times by SKU.
   - Expose **MCP Resource (`trey://governance/mcp-security-standards`):** Returns Trey Research's MCP security and DLP policy standards.
2. **Onboard the MCP Server into Microsoft Copilot Studio:**
   - Configure the OpenAPI custom connector wrapper with the `x-ms-agentic-protocol: mcp-streamable-1.0` specification so Copilot Studio dynamically discovers all tools and schemas at runtime!
3. **Run the Automated MCP Verification Client (`test_mcp_client.py`):**
   - Verify JSON-RPC 2.0 `tools/list`, `resources/list`, and `tools/call` responses locally.

---

## 2. Step-by-Step Hands-On Instructions

### Task 1: Inspect and Run the MCP Server & Verification Suite Locally
1. Review [`solution/mcp_enterprise_server.py`](./solution/mcp_enterprise_server.py) to see how an MCP server advertises **Tools** (with rich descriptions and JSON Schemas so the Generative Orchestrator in Copilot Studio knows when to call each tool) and **Resources**.
2. Execute the complete verification test client in your terminal:
   ```bash
   python3 labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/solution/test_mcp_client.py
   ```

---

### Task 2: Connect the MCP Server to Microsoft Copilot Studio
1. **Create the MCP Custom Connector in Power Platform / Copilot Studio:**
   - Sign in to `https://copilotstudio.microsoft.com` (inside your unmanaged solution in the Development environment).
   - Select **Agents -> Trey Research Concierge -> Actions -> + Add an action -> New custom connector (Import an OpenAPI file)**.
   - Use the OpenAPI specification below, which includes the critical **`x-ms-agentic-protocol: mcp-streamable-1.0`** extension on the `/mcp` POST operation:

   ```yaml
   swagger: '2.0'
   info:
     title: Trey Research Enterprise MCP Server
     description: Model Context Protocol (MCP) Server providing dynamic Microsoft Learn study plans and live ERP inventory tools.
     version: 1.0.0
   host: mcp.treyresearch.net
   basePath: /
   schemes:
     - https
   paths:
     /mcp:
       post:
         summary: Trey Research MCP Streamable HTTP Endpoint
         x-ms-agentic-protocol: mcp-streamable-1.0
         operationId: InvokeMCPServer
         consumes:
           - application/json
         produces:
           - application/json
           - text/event-stream
         responses:
           '200':
             description: Dynamic MCP JSON-RPC 2.0 tool discovery and execution response
   ```
2. **Configure Security & DLP Governance:**
   - Under the **Security** tab of the custom connector, select **OAuth 2.0 (Microsoft Entra ID)** (or API Key stored in Azure Key Vault / Environment Variable for service-to-service calls).
   - In **Power Platform Admin Center -> Policies -> Data policies**, classify the **Trey Research Enterprise MCP Server** connector in the **Business** data group and configure **Connector Endpoint Filtering** to allow only `https://mcp.treyresearch.net/*`.
3. **Test Dynamic Tool Discovery in Copilot Studio:**
   - Open the **Test your agent** pane in Copilot Studio and enter:
     > *"Create a 3-month study plan for AB-100. I can study 8 hours per week, and my weakest domain is Deploy AI-powered business solutions."*
   - Open the **Activity Map (Trace view)** in Copilot Studio: notice how Generative Orchestration automatically discovered `generate_certification_study_plan` from the MCP Server, populated `exam_code="AB-100"`, `hours_per_week=8`, and `weakest_domain="Deploy"`, and rendered the 12-week Microsoft Learn schedule!

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/mcp_enterprise_server.py`](./solution/mcp_enterprise_server.py) — Full MCP JSON-RPC 2.0 & FastMCP compatible server implementation.
- [`solution/test_mcp_client.py`](./solution/test_mcp_client.py) — Runnable verification test script.
- [`solution/requirements.txt`](./solution/requirements.txt) — Python package dependencies.
