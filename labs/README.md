# AB-100 Complete Hands-On Labs & Solution Manual (Beginner to Advanced)

Welcome to the **Hands-On Lab Suite** for **Exam AB-100: Microsoft Certified: Agentic AI Business Solutions Architect**.

Every single lab in this folder is designed so that you can learn in **two ways simultaneously**:
1. **Cloud Portal & CLI Step-by-Step Walkthrough:** Exact click-by-click instructions for **Microsoft Copilot Studio**, **Microsoft Foundry (`ai.azure.com`)**, **Microsoft 365 Copilot**, **Power Platform Maker & Admin Portals**, **Dynamics 365**, and **Microsoft Purview / Entra ID**.
2. **Complete In-Place Solution Code & Artifacts (`solution/` folder in every lab):** Even if you do not currently have a paid Dynamics 365 Finance license or an Azure PTU reservation, every lab includes **complete, runnable Python simulators/scripts, Copilot Studio `.mcs.yml` YAML definitions, Declarative Agent JSON manifests, OpenAPI specifications, APIM XML policies, Bicep templates, and CI/CD pipelines** right inside its `solution/` directory so you can inspect, run, and verify every solution locally!

---

## Complete Hands-On Lab Directory

| Lab # | Lab Title | Difficulty | Exam Domain & Modules | Key Skills & Solution Artifacts Included |
| :---: | :--- | :---: | :--- | :--- |
| **[Lab 01](./Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md)** | **Enterprise AI Readiness, 5-Dimension Grounding Audit & ROI / Model Router Simulator** | Beginner -> Intermediate | Domain 1 (Modules 01–04) | • 5-Dimension Grounding Data Quality Auditor (`grounding_data_quality_audit.py`)<br>• 3-Year TCO, ROI %, Payback Period & Model Router Cost Simulator (`roi_and_model_router_simulator.py`) |
| **[Lab 02](./Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/README.md)** | **Creating a SharePoint Site Embedded Agent & Extending M365 Copilot with a Declarative Agent** | Beginner -> Intermediate | Domain 1 & 2 (Modules 01, 03, 06) | • SharePoint Embedded Agent with PDFs/Word docs, OBO Auth & Citations<br>• Declarative Agent Manifest (`declarativeAgent.json`), API Plugin (`ai-plugin.json`) & OpenAPI Spec (`openapi-service-cases.yaml`) |
| **[Lab 03](./Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/README.md)** | **Copilot Studio Task & Autonomous Agents, Custom Fallback Topics & Human Escalation** | Intermediate | Domain 2 (Module 05) | • Custom `Fallback.mcs.yml` Topic with Rephrase Counter, App Insights Telemetry & Automatic Escalation<br>• Autonomous Event-Driven Agent (`AutonomousOrderTriage.mcs.yml`) & `agent.mcs.yml` |
| **[Lab 04](./Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/README.md)** | **Using Copilot to Create Dataverse Tables, AI Builder Sentiment Analysis Flow & Canvas App AI** | Beginner -> Intermediate | Domain 2 (Modules 05, 07) | • Dataverse `CustomerReviews` Table Schema (`dataverse-reviews-schema.json`)<br>• AI Builder Sentiment Analysis Flow (`sentiment-routing-flow.json`) & Power Fx Canvas App formulas |
| **[Lab 05](./Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/README.md)** | **Building an Enterprise Model Context Protocol (MCP) Server & Integrating with Copilot Studio** | Intermediate -> Advanced | Domain 2 (Module 06) | • Runnable Python MCP Server (`mcp_enterprise_server.py`) for Study Plan Generation & ERP Inventory<br>• Automated MCP Test Client (`test_mcp_client.py`) & Copilot Studio `mcp-streamable-1.0` Swagger |
| **[Lab 06](./Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/README.md)** | **Microsoft Foundry Model Catalog, Multi-Tool Agent, Predictive AI Services & A2A Orchestration** | Intermediate -> Advanced | Domain 2 (Modules 05, 06) | • Serverless Model Deployment & Leaderboard Trade-offs<br>• Multi-Tool Agent (Web Search + Code Interpreter) & A2A Orchestrator (`foundry_multi_agent_orchestrator.py`)<br>• Predictive AI Services: Speech, Translator & PII Redaction (`pii_and_predictive_services.py`) |
| **[Lab 07](./Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/README.md)** | **Dynamics 365 Business Terms, Sales Connectors, Contact Center & F&O Knowledge Interoperability** | Intermediate -> Advanced | Domain 2 (Modules 05, 07) | • D365 Customer Service Business Terms & Sales Connector Config (`d365-business-terms-and-connectors.json`)<br>• D365 Finance & Supply Chain In-App Help Knowledge Extension (`fno-knowledge-interoperability.yaml`) |
| **[Lab 08](./Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/README.md)** | **Agent Evaluation (Groundedness/Relevance/Coherence), AI Red Teaming & Content Safety Guardrails** | Advanced | Domain 3 (Modules 08, 09, 11) | • Runnable Evaluation & Red Teaming Suite (`agent_evaluation_suite.py`)<br>• Content Safety Guardrails, Prompt Shields & Blocklist Config (`guardrails_and_blocklist_config.json`) |
| **[Lab 09](./Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/README.md)** | **Enterprise AI Gateway with Azure API Management (APIM) & Microsoft Foundry** | Advanced | Domain 3 (Modules 04, 08, 11) | • APIM Inbound/Outbound Policy (`apim-ai-gateway-policy.xml`): Token Rate-Limiting, Semantic Caching, PTU->PayGo Failover & MCP Auth<br>• Modular Bicep Infrastructure (`main.bicep`) |
| **[Lab 10](./Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/README.md)** | **Creating a Power Platform Managed Solution & Automated Agentic ALM CI/CD Pipelines** | Intermediate -> Advanced | Domain 3 (Module 10) | • PAC CLI Unmanaged->Managed Automation (`pac-alm-commands.sh`)<br>• Environment Variables & Connection References (`deployment-settings.json`)<br>• GitHub Actions CI/CD Workflow (`github-actions-alm-pipeline.yml`) |
| **[Lab 11](./Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/README.md)** | **Enterprise AI Security: Microsoft Entra Agent ID, Purview DSPM for AI, DLP & Prompt Injection Defense** | Advanced | Domain 3 (Module 11) | • Power Platform DLP & Purview Governance Manifest (`dlp-and-purview-governance.json`)<br>• Runnable Indirect Prompt Injection (XPIA), Spotlighting & PII Validator (`prompt_injection_defense_validator.py`) |

---

## How to Set Up Your Free / Trial Lab Environments

1. **Local Python Verification (Zero Cloud Account Needed!):**
   - Python 3.10+ is pre-installed in most workspaces. You can run every `.py` solution script in Labs 01, 05, 06, 08, and 11 directly from your terminal to see real outputs!
2. **Microsoft Power Apps Developer Plan (Free):**
   - Sign up at `https://powerapps.microsoft.com/developerplan/` with a work/school account to get up to 3 free **Developer Environments** with **Microsoft Dataverse** included.
3. **Microsoft Copilot Studio Trial (Free 30-Day Trial):**
   - Sign up at `https://copilotstudio.microsoft.com` to build Topics, Knowledge Sources, Agent Flows, and Custom Fallback topics.
4. **Azure Free Account & Microsoft Foundry:**
   - Sign up at `https://azure.microsoft.com/free/` and access `https://ai.azure.com` for the Model Catalog, Foundry Agents, Evaluators, and Guardrails.
