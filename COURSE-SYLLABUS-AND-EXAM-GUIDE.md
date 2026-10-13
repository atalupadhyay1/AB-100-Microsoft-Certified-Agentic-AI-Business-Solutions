# Official AB-100 Course Syllabus & Exam Blueprint Guide

> **Exam Code:** AB-100  
> **Official Title:** Microsoft Certified: Agentic AI Business Solutions Architect  
> **Official Course Code:** Course AB-100T00-A: *Architecting agentic AI business solutions*  
> **Official Microsoft Learn Learning Path:** *Architect AI solutions for business productivity* (11 Modules)  
> **Last Synced with Microsoft Learn Study Guide:** October 2026 Update (Skills measured as of October 14, 2026)

---

## 1. Welcome: How This Course & Exam Fit Together

If you are picking up this repository for the first time—whether you are a **complete beginner** to agentic AI who wants to understand how modern AI agents work, a **functional consultant or developer** moving into solution architecture, or a **seasoned enterprise architect** preparing to pass Exam AB-100—this guide is built to walk beside you step by step.

Think of the **AB-100 certification** not as a memorization test of where buttons live in a portal, but as a test of **architectural judgment**. On the job (and on the exam), a stakeholder walks into your room and says:
> *"Our customer service team is drowning in 40,000 support tickets a month across email, live chat, and phone. Our sales team uses Dynamics 365 Sales, our finance data lives in Dynamics 365 Finance and SAP, and our policies sit in SharePoint PDFs. Should we buy Microsoft 365 Copilot licenses, build a custom agent in Copilot Studio, or engineer a multi-agent workflow in Microsoft Foundry? How do we secure it, govern it, test it, deploy it across Dev/Test/Prod, and prove to the CFO that it will pay for itself in six months?"*

By the time you finish the 11 modules, 11 hands-on labs, and the full quiz and mock exam suite in this repository, you will be able to answer that question with total clarity and confidence.

---

## 2. Exam Logistics & Certification Prerequisites

### Exam At a Glance

| Attribute | Official Detail |
| :--- | :--- |
| **Exam Code** | AB-100 |
| **Credential Awarded** | Microsoft Certified: Agentic AI Business Solutions Architect (Expert Level) |
| **Target Role** | Solution Architect / Enterprise AI Architect / Lead Technical Consultant |
| **Passing Score** | **700 / 1000** (scaled score) |
| **Typical Exam Format** | 45–60 questions (Single-choice, Multiple-choice, Drag-and-Drop Sequence, Yes/No Solution Series, and 1–3 Multi-Question Enterprise Case Studies) |
| **Time Limit** | ~100–120 minutes (Open-book access to Microsoft Learn is available during the exam, though time management is critical!) |
| **Renewal Policy** | Every 12 months via a free, unproctored online renewal assessment on Microsoft Learn |

### Prerequisite Certifications (Important!)

Because **Microsoft Certified: Agentic AI Business Solutions Architect** is an **Expert-level** certification, passing Exam AB-100 is half the equation. To be awarded the official Expert badge and certificate in your Microsoft Learn profile, you must **also** hold at least **one** qualifying Associate-level certification from Microsoft's approved prerequisite pathways:

1. **Microsoft Certified: Azure AI Engineer Associate** (Exam AI-102)
2. **Microsoft Certified: Power Platform Functional Consultant Associate** (Exam PL-200)
3. **Microsoft Certified: Power Platform Developer Associate** (Exam PL-400)
4. **Microsoft Certified: Power Platform Solution Architect Expert** (Exam PL-600)
5. **Microsoft Certified: Power Automate RPA Developer Associate** (Exam PL-500)
6. **Microsoft Certified: Dynamics 365 Contact Center AI Engineer Associate** (Exam AB-250)
7. **Microsoft Certified: Dynamics 365 Sales Functional Consultant Associate** (Exam MB-210)
8. **Microsoft Certified: Dynamics 365 Customer Service Functional Consultant Associate** (Exam MB-230)
9. **Microsoft Certified: Dynamics 365 Field Service Functional Consultant Associate** (Exam MB-240)
10. **Microsoft Certified: Dynamics 365 Customer Experience Analyst Associate** (Exam MB-280)
11. **Microsoft Certified: Dynamics 365 Finance Functional Consultant Associate** (Exam MB-310)
12. **Microsoft Certified: Dynamics 365 Supply Chain Management Functional Consultant Associate** (Exam MB-330)
13. **Microsoft Certified: Dynamics 365: Finance and Operations Apps Developer Associate** (Exam MB-500)
14. **Microsoft Certified: Dynamics 365 Business Central Functional Consultant / Developer Associate** (Exam MB-800 / MB-820)

> **Human Tip:** You can take Exam AB-100 *before* or *after* earning your prerequisite Associate certification! As soon as both are active on your Microsoft Learn profile, the Expert certification automatically unlocks.

---

## 3. Preserved Course Structure: How the 3 Exam Domains Map to the 11 Official Modules

The official **Course AB-100T00-A** (*Architect AI solutions for business productivity*) is structured into **11 core modules** that map directly to the **3 official AB-100 exam domains**:

| Exam Domain | Exam Weight | Official Course Modules | Corresponding Hands-On Labs |
| :--- | :---: | :--- | :--- |
| **Domain 1: Plan AI-Powered Business Solutions** | **25–30%** | **Module 01:** Introduction to agentic AI business solutions<br>**Module 02:** Analyze requirements for AI-powered business solutions<br>**Module 03:** Design overall AI strategy for business solutions<br>**Module 04:** Evaluate costs and benefits of AI solutions | **Lab 01:** Enterprise AI Readiness, Grounding Audit & ROI/Model Router Simulator<br>**Lab 02:** SharePoint Embedded & M365 Copilot Declarative Agent |
| **Domain 2: Design AI-Powered Business Solutions** | **25–30%** | **Module 05:** Design AI agents for business solutions<br>**Module 06:** Design extensibility of AI solutions<br>**Module 07:** Orchestrate configuration of prebuilt agents and apps | **Lab 03:** Copilot Studio Topics, Custom Fallback & Autonomous Agent Flows<br>**Lab 04:** Dataverse Table with Copilot & AI Builder Sentiment Flow<br>**Lab 05:** Model Context Protocol (MCP) Server with Copilot Studio & Foundry<br>**Lab 06:** Microsoft Foundry Model Catalog, Multi-Tool Agent & A2A<br>**Lab 07:** Dynamics 365 Copilot Customization & ERP/CRM Orchestration |
| **Domain 3: Deploy AI-Powered Business Solutions** | **40–45%** | **Module 08:** Monitor, analyze, and tune AI agents<br>**Module 09:** Manage testing AI-powered business solutions<br>**Module 10:** Design ALM process for AI-powered business solutions<br>**Module 11:** Design responsible AI security, governance, risk management, and compliance | **Lab 08:** Foundry Agent Evaluation, AI Red Teaming & Content Safety Guardrails<br>**Lab 09:** AI Gateway with Azure API Management (APIM) & Foundry<br>**Lab 10:** Power Platform Managed Solutions & Agentic ALM CI/CD Pipelines<br>**Lab 11:** Enterprise AI Security, Purview DLP, Entra Agent ID & Prompt Defense |

> **Architect's Exam Strategy Insight:** Notice that **Domain 3 (Deploy AI-Powered Business Solutions)** carries **40–45%** of the total exam weight! Nearly half of your exam score comes from monitoring, evaluation, testing, ALM (Application Lifecycle Management across Dev/Test/Prod), security, governance, and Responsible AI. Never skip Modules 08–11!

---

## 4. Verbatim Official Skills Measured (October 2026 Study Guide)

Below is the complete, verbatim checklist of every skill measured on Exam AB-100, cross-referenced to the exact module and lab in this repository where you will master it.

### Domain 1: Plan AI-Powered Business Solutions (25–30%)

#### 1.1 Analyze requirements for AI-powered business solutions *(Covered in Module 01 & Module 02, Lab 01)*
- [x] Assess the use of agents in task automation, data analytics, and decision-making
- [x] Review data for grounding, including accuracy, relevance, timeliness, cleanliness, and availability
- [x] Organize business solution data to be available for other AI systems

#### 1.2 Design overall AI strategy for business solutions *(Covered in Module 03, Lab 01 & Lab 02)*
- [x] Implement the AI adoption process from the Cloud Adoption Framework for Azure
- [x] Design the strategy for building AI and agents in business solutions
- [x] Design a multi-agent solution by using platforms such as Microsoft 365 Copilot, Copilot Studio, and Microsoft Foundry
- [x] Develop the use cases for prebuilt agents in the solution
- [x] Define the solution rules and constraints when building AI components with Copilot Studio, Microsoft Foundry, and Microsoft Foundry Tools
- [x] Determine the use of generative AI and knowledge sources in agents built with Copilot Studio
- [x] Determine when to build custom agents or extend Microsoft 365 Copilot
- [x] Determine when custom AI models should be created
- [x] Provide guidelines for creating a prompt library
- [x] Develop the use cases for customized small language models (SLMs) for the solution
- [x] Provide prompt engineering guidelines and techniques for AI-powered business solutions
- [x] Include the elements of the Microsoft AI Center of Excellence (AI CoE)
- [x] Design AI solutions that use multiple Dynamics 365 apps

#### 1.3 Evaluate the costs and benefits of an AI-powered business solution *(Covered in Module 04, Lab 01)*
- [x] Select ROI criteria for AI-powered business solutions, including the total cost of ownership (TCO)
- [x] Create an ROI analysis for the proposed AI solution for a business process
- [x] Analyze whether to build, buy, or extend AI components for business solutions
- [x] Implement a model router to intelligently route requests to the most suitable model

---

### Domain 2: Design AI-Powered Business Solutions (25–30%)

#### 2.1 Design AI and agents for business solutions *(Covered in Module 05, Labs 03, 04, 06, 07)*
- [x] Design business terms for Copilot in Dynamics 365 apps for customer experience and service
- [x] Design customizations of Copilot in Dynamics 365 apps for customer experience and service
- [x] Design connectors for Copilot in Dynamics 365 Sales
- [x] Design agents for integration with Dynamics 365 Contact Center channels
- [x] Design task agents
- [x] Design autonomous agents
- [x] Design prompt and response agents
- [x] Propose Microsoft Foundry Tools for a given requirement
- [x] Propose code-first generative pages and the use of an agent feed for apps
- [x] Design topics for Copilot Studio, including fallback
- [x] Design data processing for AI models and grounding
- [x] Design a business process to include AI components in a Power Apps canvas app
- [x] Apply the Microsoft Power Platform Well-Architected Framework to intelligent application workloads
- [x] Determine when to use standard natural language processing (NLP), conversational language understanding (CLU), or generative AI orchestration in Copilot Studio
- [x] Design agents and agent flows with Copilot Studio
- [x] Design prompt actions in Copilot Studio

#### 2.2 Design extensibility of AI solutions *(Covered in Module 06, Labs 02, 05, 06)*
- [x] Design AI solutions by using custom models in Microsoft Foundry
- [x] Design agents in Microsoft 365 Copilot
- [x] Design agent extensibility in Copilot Studio
- [x] Design agent extensibility with Model Context Protocol (MCP) in Copilot Studio
- [x] Design agents to automate tasks in apps and websites by using Computer Use in Copilot Studio
- [x] Design agent behaviors in Copilot Studio, including reasoning and voice mode
- [x] Optimize solution design by using agents in Microsoft 365, including Teams and SharePoint

#### 2.3 Orchestrate configuration for prebuilt agents and apps *(Covered in Module 07, Lab 07)*
- [x] Orchestrate AI features in Dynamics 365 apps for finance and supply chain
- [x] Orchestrate AI features in Dynamics 365 apps for customer experience and service
- [x] Propose Microsoft 365 agents for business scenarios
- [x] Orchestrate the configuration of Microsoft 365 Copilot for Sales and Microsoft 365 Copilot for Service
- [x] Propose Microsoft Power Platform AI features, including AI Hub (AI Builder)
- [x] Design interoperability of the finance and operations agent chats to use additional knowledge sources
- [x] Recommend the process of adding knowledge sources to in-app help and guidance for Dynamics 365 Finance or Dynamics 365 Supply Chain Management apps

---

### Domain 3: Deploy AI-Powered Business Solutions (40–45%)

#### 3.1 Analyze, monitor, and tune AI-powered business solutions *(Covered in Module 08, Labs 08 & 09)*
- [x] Recommend the process and tools required for monitoring agents
- [x] Analyze backlog and user feedback of AI and agent usage
- [x] Apply AI-based tools to analyze and identify issues and perform tuning
- [x] Monitor agent performance and metrics
- [x] Interpret telemetry data for performance and model tuning

#### 3.2 Manage the testing of AI-powered business solutions *(Covered in Module 09, Lab 08)*
- [x] Recommend the process and metrics to test agents
- [x] Create validation criteria of custom AI models
- [x] Validate effective Copilot prompt best practices
- [x] Design end-to-end test scenarios of AI solutions that use multiple Dynamics 365 apps
- [x] Build the strategy for creating test cases by using Copilot

#### 3.3 Design the ALM process for AI-powered business solutions *(Covered in Module 10, Lab 10)*
- [x] Design the ALM process for data used in AI models and agents
- [x] Design the ALM process for Copilot Studio agents, connectors, and actions
- [x] Design the ALM process for Microsoft Foundry Agent Service
- [x] Design the ALM process for custom AI models
- [x] Design the ALM process for AI in Dynamics 365 apps for finance and supply chain
- [x] Design the ALM process for AI in Dynamics 365 apps for customer experience and service

#### 3.4 Design responsible AI, security, governance, risk management, and compliance *(Covered in Module 11, Labs 08, 09, 11)*
- [x] Design security for agents
- [x] Design governance for agents
- [x] Design model security
- [x] Analyze solution and AI vulnerabilities and mitigations, including prompt manipulation
- [x] Review solution for adherence to responsible AI principles
- [x] Validate data residency and movement compliance
- [x] Design access controls on grounding data and model tuning
- [x] Design audit trails for changes to models and data

---

## 5. Essential Microsoft Terminology & Rename Cheat Sheet

Microsoft frequently updates product names. On Exam AB-100, **always recognize the current 2026 terminology**:

| Legacy / Older Name | Current Official AB-100 Name | What It Actually Is |
| :--- | :--- | :--- |
| Azure AI Studio / Azure AI Foundry | **Microsoft Foundry** | The unified pro-code/low-code enterprise AI platform (`ai.azure.com`) for models, agents, evaluations, and guardrails. |
| Azure AI Services / Cognitive Services | **Microsoft Foundry Tools** | Prebuilt & customizable AI APIs (Document Intelligence, Vision, Speech, Language, Translator, Content Safety). |
| Power Virtual Agents (PVA) | **Microsoft Copilot Studio** | Low-code graphical & YAML studio for building custom agents, agent flows, and extending M365 Copilot. |
| Copilot for Microsoft 365 | **Microsoft 365 Copilot** | Work-grounded productivity assistant across Word, Excel, PowerPoint, Outlook, Teams, and Business Chat (Work IQ). |
| Bing Chat Enterprise | **Microsoft 365 Copilot Chat** | Web-grounded enterprise chat included with M365 commercial licenses (can run metered Copilot Studio agents). |
| Copilot for Sales / Copilot for Service | **Microsoft 365 Copilot for Sales / Service** | Role-specific M365 Copilot extensions that bridge M365 (Outlook/Teams) with CRM systems (Dynamics 365 / Salesforce). |
| Azure Active Directory (Azure AD) | **Microsoft Entra ID** | Cloud identity and access management platform. |
| Service Principal for Agents | **Microsoft Entra Agent ID** | First-class identity assigned specifically to AI agents for RBAC, Conditional Access, and audit logging. |
| Cloud Flows inside Copilot Studio | **Agent Flows** | Deterministic, structured workflow sequences with AI actions orchestrated inside Copilot Studio. |
| Robotic UI Screen Scraping | **Computer Use (CUA) in Copilot Studio** | Vision-reasoning agent capability that interacts with legacy desktop/web UIs via virtual mouse and keyboard when no API exists. |

---

## 6. Architect's Portal Directory (Know Which Portal Does What!)

On Exam AB-100, many questions ask *where* an administrator or architect configures a specific control. Memorize this table:

| Portal Name | URL | Key AB-100 Responsibilities |
| :--- | :--- | :--- |
| **Microsoft 365 Admin Center (Copilot Control System)** | `https://admin.microsoft.com` | Assign M365 Copilot licenses, approve/block declarative & shared agents under **Copilot -> Agents**, configure web search policies. |
| **Microsoft Copilot Studio** | `https://copilotstudio.microsoft.com` | Author custom agents, topics, knowledge sources, MCP actions, Agent Flows, Computer Use, channels, and built-in analytics. |
| **Microsoft Foundry Portal** | `https://ai.azure.com` | Deploy models from Model Catalog, configure Model Router, build Foundry Agents, run Evaluations, AI Red Teaming, Content Safety Guardrails, and Foundry Control Plane governance. |
| **Power Platform Admin Center (PPAC)** | `https://admin.powerplatform.microsoft.com` | Manage environments (Dev/Test/Prod), Managed Environments, Data Loss Prevention (DLP) policies (including blocking/allowing MCP servers and connectors), capacity/message packs, and Customer Managed Keys (CMK). |
| **Power Apps Maker Portal** | `https://make.powerapps.com` | Build Dataverse tables, Canvas/Model-driven apps, AI Hub (AI Builder prompts & models), Solutions, and Power Platform Pipelines. |
| **Microsoft Purview Portal** | `https://purview.microsoft.com` | Sensitivity labels, Information Protection, Data Loss Prevention (DLP), AI Hub (Data Security Posture Management for AI / DSPM for AI), Audit logs, eDiscovery, and Communication Compliance. |
| **Microsoft Entra Admin Center** | `https://entra.microsoft.com` | Microsoft Entra ID, **Microsoft Entra Agent ID**, Managed Identities, App Registrations, Conditional Access, and Privileged Identity Management (PIM). |
| **Microsoft Viva Insights (Copilot Dashboard)** | `https://analysis.insights.viva.office.com` | Executive readiness, adoption, usage frequency, time saved, and user sentiment metrics for Microsoft 365 Copilot and agents. |
| **Copilot Studio Kit (Power CAT)** | Installed in Power Platform | Advanced automated testing harness, KPI aggregation, conversation transcript analysis, and prompt validation for Copilot Studio agents. |
