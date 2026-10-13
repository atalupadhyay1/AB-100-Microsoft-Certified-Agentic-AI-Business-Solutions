# AB-100: Microsoft Certified: Agentic AI Business Solutions Architect — Complete Study Material, Hands-On Labs & Exam Solutions

> **Official Exam Code:** `AB-100`  
> **Official Certification:** *Microsoft Certified: Agentic AI Business Solutions Architect (Expert)*  
> **Official Course Structure Preserved:** Course `AB-100T00-A` (*Architecting agentic AI business solutions*) & Microsoft Learn Path (*Architect AI solutions for business productivity* — All 11 Modules & 117 Units)  
> **Syllabus Alignment:** Synced with the **October 2026 Exam AB-100 Study Guide**

---

## Welcome! How This Repository Is Designed (Beginner to Advanced)

Whether you are **new to Agentic AI** and want plain-English mental models that demystify how AI agents perceive, reason, and act—or you are a **practicing Solution Architect, Consultant, or AI Engineer** preparing to pass **Exam AB-100** with flying colors—this repository is your complete, self-contained companion.

### What Makes This Study Material Different?
1. **Humanized Conceptual Mastery (Beginner -> Intermediate -> Advanced):**
   - Every topic begins with **real-world analogies and visual ASCII architecture diagrams** before diving into **intermediate portal/SDK mechanics** and **advanced Solution Architect trade-off matrices**.
2. **100% Preserved Official Course Structure (All 3 Domains & 11 Modules):**
   - Preserves the exact sequence of all **11 official Microsoft Learn modules** and **every single verbatim exam objective** across **Plan (25–30%)**, **Design (25–30%)**, and **Deploy (40–45%)**.
3. **11 Complete Step-by-Step Hands-On Labs with All Solutions in Place (`labs/`):**
   - Covers **Microsoft Copilot Studio**, **SharePoint & M365 Copilot Declarative Agents**, **Model Context Protocol (MCP) Servers**, **Agent2Agent (A2A)**, **Microsoft Foundry (Model Catalog, Model Router, Multi-Tool Agents, Predictive AI Tools, Evaluators, AI Red Teaming, Guardrails)**, **Azure API Management (APIM) AI Gateway**, **Power Platform (Dataverse, AI Builder Sentiment Flows, Canvas Apps, Managed Solutions, PAC CLI & GitHub Actions CI/CD)**, **Dynamics 365 (Sales, Customer Service, Contact Center, Finance & Supply Chain Management)**, and **Microsoft Purview / Entra Agent ID Security**.
   - Every lab has a dedicated `solution/` folder with **complete, runnable Python scripts, `.mcs.yml` Copilot Studio YAML definitions, Declarative Agent JSON manifests, OpenAPI specs, APIM XML policies, Bicep templates, and CI/CD workflows**.
4. **Complete Quizzes, Case Studies & 60-Question Mock Exam with Full Solutions (`quizzes-and-exams/`):**
   - Over **165+ practice questions and enterprise case study items** across module assessments, domain deep-dives, and a full-length 60-question mock exam—every single one with **complete answers and architect rationales in place**.

---

## Repository Structure at a Glance

```text
AB-100-Microsoft-Certified-Agentic-AI-Business-Solutions/
├── README.md                                      # Master Course Hub, Navigation & Study Roadmap
├── COURSE-SYLLABUS-AND-EXAM-GUIDE.md              # Official October 2026 AB-100 Blueprint, Prerequisites & Portals
├── GLOSSARY-AND-MENTAL-MODELS.md                  # Humanized Beginner-to-Architect Primer (MCP, A2A, RAG, Foundry)
│
├── modules/                                       # All 11 Official Course Modules (Beginner -> Advanced + Quizzes)
│   ├── Module-01-Introduction-to-Agentic-AI-Business-Solutions.md
│   ├── Module-02-Analyze-Requirements-for-AI-Powered-Business-Solutions.md
│   ├── Module-03-Design-Overall-AI-Strategy-for-Business-Solutions.md
│   ├── Module-04-Evaluate-Costs-and-Benefits-of-AI-Solutions.md
│   ├── Module-05-Design-AI-Agents-for-Business-Solutions.md
│   ├── Module-06-Design-Extensibility-of-AI-Solutions.md
│   ├── Module-07-Orchestrate-Configuration-of-Prebuilt-Agents-and-Apps.md
│   ├── Module-08-Monitor-Analyze-and-Tune-AI-Agents.md
│   ├── Module-09-Manage-Testing-AI-Powered-Business-Solutions.md
│   ├── Module-10-Design-ALM-Process-for-AI-Powered-Business-Solutions.md
│   └── Module-11-Design-Responsible-AI-Security-Governance-and-Compliance.md
│
├── labs/                                          # 11 Step-by-Step Hands-On Labs + Complete `solution/` Code
│   ├── README.md                                  # Master Lab Guide & Free/Trial Environment Setup
│   ├── Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/
│   ├── Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/
│   ├── Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/
│   ├── Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/
│   ├── Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/
│   ├── Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/
│   ├── Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/
│   ├── Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/
│   ├── Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/
│   ├── Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/
│   └── Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/
│
└── quizzes-and-exams/                             # Complete Quizzes, Case Studies & 60-Question Mock Exam
    ├── README.md                                  # Exam Strategy & Time Management Guide
    ├── Module-Quizzes-01-to-11-With-Solutions.md  # 55 Module Knowledge Check Questions + Full Solutions
    ├── Domain-1-Plan-Practice-Quiz-and-Scenarios.md
    ├── Domain-2-Design-Practice-Quiz-and-Scenarios.md
    ├── Domain-3-Deploy-Practice-Quiz-and-Scenarios.md
    └── Full-Length-AB-100-Mock-Exam-With-Solutions.md # 60 Questions + 3 Case Studies + Complete Rationales
```

---

## Step 0: Start Here — Essential Primers

1. **[Official Course Syllabus, Prerequisites, Portals & Terminology Guide (`COURSE-SYLLABUS-AND-EXAM-GUIDE.md`)](./COURSE-SYLLABUS-AND-EXAM-GUIDE.md)**
   - Read this first to understand the exam format, the 14 qualifying Associate-level prerequisite certifications, the **Microsoft Product Rename Table** (`Microsoft Foundry`, `Microsoft Foundry Tools`, `Microsoft Entra Agent ID`, `Agent Flows`, `Computer Use`), and the **Architect's Portal Directory**.
2. **[Humanized Mental Models & A–Z Glossary (`GLOSSARY-AND-MENTAL-MODELS.md`)](./GLOSSARY-AND-MENTAL-MODELS.md)**
   - Builds your intuition with everyday analogies for the **Agent Spectrum** (Rule-based -> Retrieval -> Task Agent -> Autonomous Agent -> Multi-Agent System), **Grounding (RAG) vs. Fine-Tuning**, **MCP vs. A2A**, **Build vs. Buy vs. Extend**, and **Model Routers**.

---

## Step 1: Complete Course Modules (Preserved Official 11-Module Curriculum)

### Domain 1: Plan AI-Powered Business Solutions (25–30% Exam Weight)

| Module | Official Module Title & Study Link | Units | Key Architectural Concepts Covered |
| :---: | :--- | :---: | :--- |
| **01** | **[Introduction to Agentic AI Business Solutions](./modules/Module-01-Introduction-to-Agentic-AI-Business-Solutions.md)** | 8 Units | Architect's role in AI transformation; Microsoft AI ecosystem mapping; Out-of-the-box M365 & Dynamics 365 agents (**Sales Qualification, Supplier Communications, Account Reconciliation, Customer Knowledge Management,Customer Intent, Employee Self-Service, Facilitator, Interpreter, Researcher, Analyst**). |
| **02** | **[Analyze Requirements for AI-Powered Business Solutions](./modules/Module-02-Analyze-Requirements-for-AI-Powered-Business-Solutions.md)** | 6 Units | Workload classification (**Task Automation vs. Data Analytics vs. Decision-Making**); The **5 Dimensions of Grounding Data Quality** (**Accuracy, Relevance, Timeliness, Cleanliness, Availability**); Organizing enterprise data with **Microsoft Fabric OneLake**, **Dataverse**, **Graph Connectors**, and **Azure AI Search**. |
| **03** | **[Design Overall AI Strategy for Business Solutions](./modules/Module-03-Design-Overall-AI-Strategy-for-Business-Solutions.md)** | 19 Units | **Cloud Adoption Framework (CAF) for AI**; Multi-agent orchestration patterns (**Orchestrator-Specialist, Sequential, Parallel Fan-Out, Maker-Checker, Handoff**); Copilot Studio knowledge sources (and the **Uploaded Files ACL trap!**); **Declarative Agent vs. Custom Engine Agent**; **Small Language Models (SLMs)**; **GCSE Prompt Engineering & Prompt Libraries**; **AI Center of Excellence (AI CoE)**; Cross-Dynamics 365 architecture. |
| **04** | **[Evaluate Costs and Benefits of AI Solutions](./modules/Module-04-Evaluate-Costs-and-Benefits-of-AI-Solutions.md)** | 7 Units | **Total Cost of Ownership (TCO = CapEx + OpEx)**; **ROI (%) & Payback Period math**; Licensing & metering (**M365 Copilot per-user vs. Copilot Credits vs. Foundry PayGo / PTU / Batch API**); **Build vs. Buy vs. Extend** economics; **Microsoft Foundry Model Router** architecture. |

---

### Domain 2: Design AI-Powered Business Solutions (25–30% Exam Weight)

| Module | Official Module Title & Study Link | Units | Key Architectural Concepts Covered |
| :---: | :--- | :---: | :--- |
| **05** | **[Design AI Agents for Business Solutions](./modules/Module-05-Design-AI-Agents-for-Business-Solutions.md)** | 21 Units | Responsible AI design tenets; **Dynamics 365 Business Terms**, Case Summary customizations, Sales connectors & **Contact Center omnichannel integration**; **Task vs. Autonomous vs. Prompt/Response agents**; **Microsoft Foundry Tools** (**Document Intelligence, Speech, Language, Vision, Translator, Content Safety**); **Code-First Generative Pages & Agent Feed**; **Fallback Topic design**; **Standard NLP vs. CLU vs. Generative Orchestration**; **Agent Flows & JSON Prompt Actions**; **Power Platform Well-Architected Framework**. |
| **06** | **[Design Extensibility of AI Solutions](./modules/Module-06-Design-Extensibility-of-AI-Solutions.md)** | 10 Units | Custom fine-tuned & predictive ML models in **Microsoft Foundry**; M365 Copilot extensibility tiers; **Model Context Protocol (MCP)** in Copilot Studio (`x-ms-agentic-protocol: mcp-streamable-1.0`); **Computer Use (CUA)** for legacy GUI automation without APIs; **Reasoning Mode & Voice Mode** (Barge-In, SSML, DTMF); Optimizing agents for **Microsoft Teams (SSO) & SharePoint (OBO)**. |
| **07** | **[Orchestrate Configuration of Prebuilt Agents and Apps](./modules/Module-07-Orchestrate-Configuration-of-Prebuilt-Agents-and-Apps.md)** | 10 Units | Orchestrating AI in **Dynamics 365 Finance & Supply Chain Management**; **Dynamics 365 Customer Service & Customer Insights**; **Microsoft 365 Copilot for Sales & Copilot for Service** (connecting Outlook/Teams to D365 & Salesforce); **Power Platform AI Hub (AI Builder)** prebuilt vs. custom models; Extending **`Copilot for finance and operations apps`** in-app help with **SharePoint knowledge sources** and CRM interoperability. |

---

### Domain 3: Deploy AI-Powered Business Solutions (40–45% Exam Weight — Highest Weight!)

| Module | Official Module Title & Study Link | Units | Key Architectural Concepts Covered |
| :---: | :--- | :---: | :--- |
| **08** | **[Monitor, Analyze, and Tune AI Agents](./modules/Module-08-Monitor-Analyze-and-Tune-AI-Agents.md)** | 8 Units | Monitoring tool selection (**Copilot Studio Analytics, Azure Application Insights / KQL, Foundry Control Plane, Viva Insights, Copilot Studio Kit**); Session outcomes (**Resolved, Escalated, Abandoned**); Backlog clustering; Telemetry root-cause diagnosis (**High Retrieval + Low Groundedness vs. Low Retrieval**, HTTP 429 throttling, prompt token bloat). |
| **09** | **[Manage Testing AI-Powered Business Solutions](./modules/Module-09-Manage-Testing-AI-Powered-Business-Solutions.md)** | 8 Units | **5 Core AI Evaluation Metrics** (**Groundedness, Relevance, Retrieval, Coherence/Fluency, Tool Call Accuracy**); **Copilot Studio Kit** automated testing; Custom model validation criteria (**Precision vs. Recall vs. F1**); **AI Red Teaming (PyRIT)**; Cross-Dynamics 365 E2E testing (**Playwright / Test Engine / RSAT**); AI-assisted test generation + mandatory **Human SME Golden Dataset sign-off**. |
| **10** | **[Design ALM Process for AI-Powered Business Solutions](./modules/Module-10-Design-ALM-Process-for-AI-Powered-Business-Solutions.md)** | 9 Units | **Data ALM (DataOps)** & Blue-Green vector index promotion; **Configuration Migration Tool (CMT)** for Business Terms/reference data; **Managed vs. Unmanaged Solutions**; **Environment Variables, Connection References & `deployment-settings.json`**; **Power Platform CLI (`pac`)** & **GitHub Actions / Azure DevOps CI/CD**; **Shadow & Canary model rollouts** in Foundry; Synchronizing **F&O Deployable Packages** with Power Platform Solutions. |
| **11** | **[Design Responsible AI, Security, Governance, Risk Management, and Compliance](./modules/Module-11-Design-Responsible-AI-Security-Governance-and-Compliance.md)** | 11 Units | **On-Behalf-Of (OBO)** vs. **Microsoft Entra Agent ID**; **Power Platform DLP Policies & Connector Endpoint Filtering**; **Direct (UPIA) vs. Indirect Prompt Injection (XPIA)**; **Azure AI Content Safety Prompt Shields, Spotlighting, Groundedness Detection & Blocklists**; **Microsoft Purview DSPM for AI & Sensitivity Label Inheritance**; **Data Residency (`Data Zone Standard` vs. `Global Standard`)**; Grounding ACLs vs. Fine-Tuning security; **Immutable Audit Trails**. |

---

## Step 2: Complete Hands-On Labs with Full Solutions (`labs/`)

Every lab includes step-by-step instructions plus a `solution/` directory containing ready-to-use code and configuration artifacts:

1. **[Lab 01: Enterprise AI Readiness, 5-Dimension Grounding Audit & ROI / Model Router Simulator](./labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md)**
   - *Solutions included:* [`grounding_data_quality_audit.py`](./labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/grounding_data_quality_audit.py), [`roi_and_model_router_simulator.py`](./labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/roi_and_model_router_simulator.py)
2. **[Lab 02: SharePoint Site Embedded Agent & M365 Copilot Declarative Agent with API Plugin](./labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/README.md)**
   - *Solutions included:* [`declarativeAgent.json`](./labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/solution/declarativeAgent.json), [`ai-plugin.json`](./labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/solution/ai-plugin.json), [`openapi-service-cases.yaml`](./labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/solution/openapi-service-cases.yaml)
3. **[Lab 03: Copilot Studio Topics, Custom Fallback Topic & Event-Driven Autonomous Agent Flows](./labs/Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/README.md)**
   - *Solutions included:* [`agent.mcs.yml`](./labs/Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/solution/agent.mcs.yml), [`Fallback.mcs.yml`](./labs/Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/solution/Fallback.mcs.yml), [`AutonomousOrderTriage.mcs.yml`](./labs/Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/solution/AutonomousOrderTriage.mcs.yml)
4. **[Lab 04: Creating Dataverse Tables with Copilot, AI Builder Sentiment Flow & Canvas App AI](./labs/Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/README.md)**
   - *Solutions included:* [`dataverse-reviews-schema.json`](./labs/Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/solution/dataverse-reviews-schema.json), [`sentiment-routing-flow.json`](./labs/Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/solution/sentiment-routing-flow.json)
5. **[Lab 05: Model Context Protocol (MCP) Server Integration with Copilot Studio & Microsoft Foundry](./labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/README.md)**
   - *Solutions included:* [`mcp_enterprise_server.py`](./labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/solution/mcp_enterprise_server.py), [`test_mcp_client.py`](./labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/solution/test_mcp_client.py)
6. **[Lab 06: Microsoft Foundry Model Catalog, Multi-Tool Agent, Predictive AI Services & A2A Orchestration](./labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/README.md)**
   - *Solutions included:* [`foundry_multi_agent_orchestrator.py`](./labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/foundry_multi_agent_orchestrator.py), [`pii_and_predictive_services.py`](./labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/pii_and_predictive_services.py)
7. **[Lab 07: Dynamics 365 Business Terms, Sales Connectors, Contact Center & F&O Knowledge Interoperability](./labs/Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/README.md)**
   - *Solutions included:* [`d365-business-terms-and-connectors.json`](./labs/Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/solution/d365-business-terms-and-connectors.json), [`fno-knowledge-interoperability.yaml`](./labs/Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/solution/fno-knowledge-interoperability.yaml)
8. **[Lab 08: Foundry Agent Evaluation, AI Red Teaming & Content Safety Guardrails](./labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/README.md)**
   - *Solutions included:* [`agent_evaluation_suite.py`](./labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/solution/agent_evaluation_suite.py), [`guardrails_and_blocklist_config.json`](./labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/solution/guardrails_and_blocklist_config.json)
9. **[Lab 09: Enterprise AI Gateway with Azure API Management (APIM) & Microsoft Foundry](./labs/Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/README.md)**
   - *Solutions included:* [`apim-ai-gateway-policy.xml`](./labs/Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/solution/apim-ai-gateway-policy.xml), [`main.bicep`](./labs/Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/solution/main.bicep)
10. **[Lab 10: Power Platform Managed Solutions & Automated Agentic ALM CI/CD Pipelines](./labs/Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/README.md)**
    - *Solutions included:* [`pac-alm-commands.sh`](./labs/Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/solution/pac-alm-commands.sh), [`deployment-settings.json`](./labs/Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/solution/deployment-settings.json), [`github-actions-alm-pipeline.yml`](./labs/Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/solution/github-actions-alm-pipeline.yml)
11. **[Lab 11: Enterprise AI Security — Entra Agent ID, Purview DSPM for AI, DLP & Prompt Injection Defense](./labs/Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/README.md)**
    - *Solutions included:* [`dlp-and-purview-governance.json`](./labs/Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/solution/dlp-and-purview-governance.json), [`prompt_injection_defense_validator.py`](./labs/Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/solution/prompt_injection_defense_validator.py)

### Quick-Run All Runnable Python Lab Solutions Locally
You can execute all 6 interactive Python lab verification scripts right from the repository root:
```bash
python3 labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/grounding_data_quality_audit.py
python3 labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/roi_and_model_router_simulator.py
python3 labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/solution/test_mcp_client.py
python3 labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/foundry_multi_agent_orchestrator.py
python3 labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/pii_and_predictive_services.py
python3 labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/solution/agent_evaluation_suite.py
python3 labs/Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/solution/prompt_injection_defense_validator.py
```

---

## Step 3: Complete Quizzes, Domain Scenarios & Full-Length Mock Exam (`quizzes-and-exams/`)

- **[Assessment Strategy & Exam Tips (`quizzes-and-exams/README.md`)](./quizzes-and-exams/README.md)**
- **[Consolidated 55-Question Module Quizzes (Modules 01–11) with Solutions](./quizzes-and-exams/Module-Quizzes-01-to-11-With-Solutions.md)**
- **[Domain 1 (Plan) Practice Quiz & Enterprise Case Study with Solutions](./quizzes-and-exams/Domain-1-Plan-Practice-Quiz-and-Scenarios.md)**
- **[Domain 2 (Design) Practice Quiz & Enterprise Case Study with Solutions](./quizzes-and-exams/Domain-2-Design-Practice-Quiz-and-Scenarios.md)**
- **[Domain 3 (Deploy) Practice Quiz & Enterprise Case Study with Solutions](./quizzes-and-exams/Domain-3-Deploy-Practice-Quiz-and-Scenarios.md)**
- **[Full-Length 60-Question AB-100 Practice Exam + 3 Enterprise Case Studies with Complete Solutions](./quizzes-and-exams/Full-Length-AB-100-Mock-Exam-With-Solutions.md)**

---

## Recommended 4-Week Study Plan (Beginner to Exam-Ready)

| Week | Focus Area | Modules to Read | Hands-On Labs to Complete | Assessments to Pass |
| :---: | :--- | :--- | :--- | :--- |
| **Week 1** | **Foundations & Domain 1 (Plan AI Solutions — 25–30%)** | `COURSE-SYLLABUS-AND-EXAM-GUIDE.md`, `GLOSSARY-AND-MENTAL-MODELS.md`, **Modules 01, 02, 03, 04** | **Lab 01** & **Lab 02** | Module 01–04 Quizzes + `Domain-1-Plan-Practice-Quiz-and-Scenarios.md` (Target $\ge 80\%$) |
| **Week 2** | **Domain 2 (Design AI & Agent Architectures — 25–30%)** | **Modules 05, 06, 07** | **Lab 03, Lab 04, Lab 05, Lab 06, Lab 07** | Module 05–07 Quizzes + `Domain-2-Design-Practice-Quiz-and-Scenarios.md` (Target $\ge 80\%$) |
| **Week 3** | **Domain 3 (Deploy, Monitor, Test, ALM & Security — 40–45%)** | **Modules 08, 09, 10, 11** | **Lab 08, Lab 09, Lab 10, Lab 11** | Module 08–11 Quizzes + `Domain-3-Deploy-Practice-Quiz-and-Scenarios.md` (Target $\ge 85\%$) |
| **Week 4** | **Full Exam Simulation & Final Review** | Review Decision Matrices & Rename Table | Re-run all Lab Solution Scripts & Inspect YAML/Bicep/XML Artifacts | **`Full-Length-AB-100-Mock-Exam-With-Solutions.md`** (60 Questions, timed 100 mins, Target $\ge 83\%$) |
