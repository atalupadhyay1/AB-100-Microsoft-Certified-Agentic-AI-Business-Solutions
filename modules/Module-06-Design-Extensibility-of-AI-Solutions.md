# Module 06: Design Extensibility of AI Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** All 10 Units (Introduction -> Custom Models in Microsoft Foundry -> Design Agents in M365 Copilot -> Extensible Agents in Copilot Studio -> Extensibility with MCP in Copilot Studio -> Computer Use in Copilot Studio -> Agent Behaviors: Reasoning and Voice Mode -> Optimize Agents in M365 Teams & SharePoint -> Module Assessment -> Summary)  
> **Associated Hands-On Labs:** [Lab 02: SharePoint & M365 Declarative Agent](../labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/README.md), [Lab 05: MCP Server with Copilot Studio & Foundry](../labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/README.md), [Lab 06: Microsoft Foundry Models, Multi-Tool Agent & A2A](../labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Giving Your Agent "Superpowers": Eyes, Hands, Deep Thought, and Universal Adapters

Out of the box, a base language model is like a brilliant professor locked inside a soundproof glass booth:
- It can talk to you,
- Calling on its memory from university,
- **But it cannot reach outside the booth** to check your live ERP database, click a button on an old legacy shipping website, speak on a live telephone line, or plug into your company's custom predictive machine learning models.

**Extensibility** is how we give the agent a way out of the glass booth:
1. **Custom Models in Microsoft Foundry** = Giving the agent a specialized calculator or domain-trained brain (e.g., an ML model that predicts equipment failure or a fine-tuned legal LLM).
2. **Model Context Protocol (MCP)** = Giving the agent a **universal USB-C port** so it can plug into any tool server and automatically discover all available actions and data resources.
3. **Computer Use (CUA)** = Giving the agent **virtual eyes and a virtual mouse/keyboard** so when an old 2004 desktop or web app has *no API at all*, the agent can look at the screen, click buttons, fill forms, and adapt even if a button moves 20 pixels to the left!
4. **Reasoning Mode & Voice Mode** = Letting the agent switch gears between **deep slow thinking** (for complex audits) and **ultra-fast natural speech** (for live telephone calls).

Let's master all 10 official units of Module 06!

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Design AI Solutions by Using Custom Models in Microsoft Foundry

When an enterprise scenario requires capabilities beyond standard out-of-the-box prompt engineering, you design a solution using **Custom Models in Microsoft Foundry**:

#### 1. The 3 Categories of Custom Models Integrated via Microsoft Foundry
| Custom Model Type | What It Is & How It Is Built | How Agents Consume It |
| :--- | :--- | :--- |
| **1. Fine-Tuned Generative Models (SLMs & LLMs)** | A base model from the **Foundry Model Catalog** (e.g., `Phi-4`, `GPT-4o-mini`, `GPT-4o`, `Llama-3.3`) trained via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), or Reinforcement Fine-Tuning (RFT) on curated JSONL pairs. | Deployed to a **Managed Online Endpoint** or **Provisioned Throughput (PTU)** endpoint in Foundry; called by Foundry Agents or connected to Copilot Studio via HTTP / Azure OpenAI connector. |
| **2. Custom Foundry Tools Models (Domain AI)** | • **Custom Document Intelligence** (trained on 5–15 labeled sample PDFs of proprietary forms)<br>• **Custom Translator** (parallel corporate glossaries)<br>• **Custom Vision / Custom Speech** | Called as deterministic tool steps inside an **Agent Flow**, **Power Automate flow**, or **Foundry Agent tool** to extract structured JSON before LLM reasoning. |
| **3. Custom Predictive ML Models (Azure Machine Learning / Databricks / Fabric)** | Traditional tabular ML models (XGBoost, PyTorch churn prediction, demand forecasting, fraud scoring) registered in the **Azure ML / Foundry Model Registry**. | Exposed as REST endpoints with OpenAPI schemas (or wrapped in an **MCP Server**) so an agent can pass customer features and get back a deterministic probability score (`churn_probability: 0.87`). |

> **Architect Best Practice ("Predictive + Generative = Better Together"):** Never ask a Generative LLM to guess next quarter's numerical inventory demand from raw sales rows! Instead, have the **Generative Agent** invoke a **Custom Predictive ML Forecasting Model** as a tool, retrieve the exact numerical forecast (`14,250 units`), and then use the Generative LLM to explain the forecast and draft the purchase order.

---

### Unit 3 & Unit 8: Design Agents in Microsoft 365 Copilot & Optimize for Teams and SharePoint

#### Complete Extensibility Spectrum for Microsoft 365 Copilot
When extending **Microsoft 365 Copilot**, an architect chooses from **three architectural tiers**:

```
+-----------------------------------------------------------------------------------+
|                MICROSOFT 365 COPILOT EXTENSIBILITY ARCHITECTURE                   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  TIER 1: KNOWLEDGE EXTENSION (Microsoft Graph Connectors / SharePoint)            |
|  • Brings external unstructured/semi-structured content into Microsoft Graph.     |
|  • Best when M365 Copilot just needs to READ and CITE external company data.      |
|                                                                                   |
|  TIER 2: DECLARATIVE AGENTS (Agent Builder / Copilot Studio / M365 Agents Toolkit)|
|  • Reuses M365 Copilot's built-in Orchestrator + Foundation Model!                |
|  • Adds: Custom System Instructions + Scoped Knowledge (SharePoint, OneDrive,     |
|    Graph Connectors, Dataverse) + Custom Actions (API Plugins, Power Platform     |
|    Connectors, MCP Servers, Adaptive Cards).                                      |
|  • Best when you want custom domain expertise & actions inside M365 Copilot       |
|    without managing your own orchestrator or model infrastructure.                |
|                                                                                   |
|  TIER 3: CUSTOM ENGINE AGENTS (Copilot Studio Standalone / Microsoft Foundry +    |
|          Microsoft 365 Agents SDK)                                                |
|  • Brings YOUR OWN Orchestrator and YOUR OWN Foundation Model(s)!                 |
|  • Published into Microsoft Teams and M365 Copilot Chat as a collaborative agent. |
|  • Best when you need custom model routing, fine-tuned SLMs, deterministic dialog |
|    topics, or pro-code multi-agent workflows (Semantic Kernel / LangGraph).       |
+-----------------------------------------------------------------------------------+
```

#### Optimizing Solution Design for Agents in Microsoft Teams and SharePoint (Unit 8)
1. **Optimizing for SharePoint:**
   - **SharePoint Embedded Site Agents:** Scope each SharePoint agent to the specific libraries/folders relevant to that business domain (maximum recommended 20–100 high-value authoritative sources or scoped site collections to maximize retrieval precision).
   - **Promote Authoritative Sources:** Use SharePoint **Approved / Official Document** metadata and move draft/archived folders outside the agent's scope.
   - **Zero-Config OBO Security:** Because SharePoint agents execute under the signed-in user's Entra ID token, never duplicate documents into unpermissioned storage; rely on **SharePoint ACLs** and **Microsoft Purview Sensitivity Labels**.
2. **Optimizing for Microsoft Teams:**
   - **Collaborative Channel & Group Chat Context:** Configure the agent so users can `@mention` it inside a Teams channel or meeting chat to reason over team context and post **Interactive Adaptive Cards** (so the whole team can see and click action buttons like `[Approve Change Request]`).
   - **Single Sign-On (SSO):** Configure **Microsoft Entra ID SSO** for the Teams channel in Copilot Studio so employees are never prompted to log in a second time when chatting in Teams.
   - **Proactive Messaging:** For autonomous or long-running tasks, have the agent send a proactive Adaptive Card message directly to the user's Teams chat when a background job completes.

---

### Unit 4 & Unit 5: Design Agent Extensibility in Copilot Studio & Model Context Protocol (MCP)

#### 1. Overview of Extensibility Mechanisms in Copilot Studio (Unit 4)
A Copilot Studio agent can be extended with **six types of tools/extensions**:
1. **Power Platform Connectors** (1,400+ prebuilt connectors to SAP, Salesforce, ServiceNow, SQL, Zendesk, plus Custom REST OpenAPI Connectors).
2. **Agent Flows** (deterministic multi-step workflows with AI steps).
3. **Prompt Actions** (custom AI Builder prompts returning text or JSON).
4. **Model Context Protocol (MCP) Servers** (dynamic multi-tool & resource discovery).
5. **Computer Use (CUA)** (GUI automation for apps/websites without APIs).
6. **Child Agents & External Connected Agents (via A2A / Microsoft Foundry / M365)** (multi-agent delegation).

#### 2. Deep Dive: Designing Agent Extensibility with Model Context Protocol (MCP) in Copilot Studio (Unit 5)
Why is **Model Context Protocol (MCP)** such a game-changer for AB-100 Solution Architects?

- **The Old Way (Traditional Custom Connectors):**
  - If your backend team adds 5 new endpoints or changes a parameter in their internal Inventory API, a Power Platform maker has to manually export the OpenAPI swagger file, update the Custom Connector in Power Platform, update every Copilot Studio agent's action mapping, and re-publish the solution.
- **The New Way (Model Context Protocol — MCP):**
  - The backend team hosts an **MCP Server** (using Streamable HTTP or SSE transport) and registers it once in Copilot Studio (via a custom connector wrapper with the `x-ms-agentic-protocol: mcp-streamable-1.0` extension or native MCP onboarding).
  - Whenever the MCP Server adds, updates, or removes **Tools** (functions) or **Resources** (data), **Copilot Studio automatically discovers and updates the available tools dynamically at runtime** without requiring you to re-author every individual action inside the agent!

```
+-------------------------------------------------------------------------------+
|          HOW COPILOT STUDIO CONNECTS TO AN ENTERPRISE MCP SERVER              |
+-------------------------------------------------------------------------------+
|                                                                               |
|  [ Copilot Studio Agent ]                                                     |
|      |  (Generative Orchestrator reads tool schemas advertised by MCP Server) |
|      v                                                                        |
|  [ Power Platform Connector / Azure API Management AI Gateway ]               |
|      |  • Enforces Power Platform DLP Policy & OAuth 2.0 / API Key Auth       |
|      |  • Enforces APIM rate-limiting & token quotas                          |
|      v                                                                        |
|  [ Enterprise MCP Server (Python FastMCP / C# / TypeScript on Container Apps)]|
|      ├── Tool 1: calculate_shipping_tariff(origin, destination, weight_kg)    |
|      ├── Tool 2: reserve_warehouse_stock(sku, quantity, facility_id)          |
|      └── Resource: warehouse://policies/hazmat-handling-rules                 |
+-------------------------------------------------------------------------------+
```

#### Architect Governance Rules for MCP in Copilot Studio:
1. **Tool Descriptions & Input Schemas (JSON Schema / Pydantic):** Because Copilot Studio's Generative Orchestrator decides *when* to call an MCP tool based strictly on the tool's docstring/description and parameter descriptions exported by the MCP server, **every MCP tool must have a clear, non-overlapping description and typed parameter constraints**.
2. **Security & DLP Governance:** MCP connections in Copilot Studio are governed by **Power Platform Data Loss Prevention (DLP) policies** and **Azure API Management (APIM)**! Always require authentication (OAuth 2.0 / Entra ID OBO or Managed Identity) and never connect production agents to unverified public MCP servers without DLP approval.

> **Hands-On Connection:** In **[Lab 05](../labs/Lab-05-MCP-Server-Integration-with-Copilot-Studio-and-Foundry/README.md)**, you will build a complete, runnable **Python FastMCP Server** and configure its OpenAPI/MCP integration manifest for **Microsoft Copilot Studio** and **Microsoft Foundry**!

---

### Unit 6: Design Agents to Automate Tasks in Apps and Websites by Using Computer Use in Copilot Studio

What do you do when a critical business process depends on a **15-year-old legacy insurance web portal** or a **thick-client Windows desktop ERP application** that has **no REST API, no database connector, and no MCP server**?

#### Enter Computer Use (CUA — Computer-Using Agent) in Microsoft Copilot Studio!

#### How Computer Use Differs from Traditional RPA (Power Automate Desktop UI Flows)

| Feature | Traditional RPA (DOM / Selector-Based UI Automation) | Computer Use (CUA) in Copilot Studio |
| :--- | :--- | :--- |
| **How It Perceives the Screen** | Relies on hardcoded HTML DOM XPaths, CSS selectors, or fixed pixel coordinates (`div#btn_submit_42`). | Uses a **multimodal vision-reasoning model** to visually read screenshots of the screen just like a human user! |
| **What Happens When a Website Redesigns a Button or Pops Up a Cookie Banner?** | **Crashes immediately** (`SelectorNotFoundException`) until a developer manually fixes the script. | **Adapts dynamically!** Sees the cookie banner, clicks *"Accept"*, locates the moved *"Submit Claim"* button visually, and completes the task. |
| **How You Author It** | Record step-by-step clicks and maintain complex UI selector trees. | Write a **natural language goal instruction** (e.g., *"Log into the legacy FreightPortal, look up Bill of Lading #{{BOL}}, and copy the customs clearance code"*), define allowed URLs/apps, and run on a hosted Windows 365 Cloud PC or machine group. |
| **Latency & Cost** | Very fast (milliseconds per click), low compute cost. | Higher latency (seconds per visual reasoning step) and higher token/credit cost. |

#### Architect's Golden Hierarchy for Task Automation (Crucial for Exam AB-100!):
1. **First Choice (Always Prefer APIs!):** If the target system has a **REST API, Power Platform Connector, Dataverse table, or MCP Server**, **always use API/MCP integration**—it is 50x faster, cheaper, and more reliable.
2. **Second Choice (Deterministic High-Speed Legacy UI):** If there is no API, the UI never changes, and you need to process 100,000 identical rows at high speed with zero LLM token cost, use **traditional Power Automate Desktop RPA**.
3. **Third Choice (Dynamic / Unstructured / Changing UI with No API):** If there is **no API** and the legacy web/desktop interface has **dynamic layouts, pop-ups, unstructured visual tables, or third-party vendor portals** you don't control, use **Computer Use in Copilot Studio**—with strict guardrails (allowlisted domains, read-only vs. write confirmation gates, and credential vaulting in Azure Key Vault / CyberArk).

---

### Unit 7: Design Agent Behaviors in Copilot Studio, Including Reasoning and Voice Mode

In Copilot Studio, you can tune how the agent thinks and communicates based on the scenario:

#### 1. Deep Reasoning Mode (Reasoning Models in Copilot Studio)
- **What it is:** Enables the agent (or specific Prompt Actions / orchestration steps) to use **deep chain-of-thought reasoning models** (such as the OpenAI `o`-series / GPT-5 reasoning tier).
- **When to enable Reasoning Mode:**
  - Complex policy compliance checking across conflicting rules,
  - Multi-constraint resource scheduling or root-cause analysis,
  - Evaluating financial anomalies or multi-step autonomous planning.
- **When NOT to enable Reasoning Mode (Architect Trade-Off):**
  - Do **not** enable deep reasoning mode for simple greetings, password resets, or live interactive **Voice Mode** calls where the caller expects an answer in under 1 second! Deep reasoning adds several seconds of "thinking time" latency and consumes extra reasoning tokens.

#### 2. Voice Mode (Interactive Voice Response / Telephony in Copilot Studio)
When designing an agent that speaks to customers over the phone (via **Dynamics 365 Contact Center** or Azure Communication Services):
- **Turn-Taking & Barge-In:** Enable **Barge-In** so if the agent is reading a list of options and the customer interrupts (*"Just connect me to billing!"*), the agent stops speaking immediately and processes the new utterance.
- **Silence Detection & Timeout Prompts:** Configure how many milliseconds of silence indicate the caller finished speaking (e.g., 1,000 ms for short zip codes vs. 2,500 ms for describing an accident) and configure gentle re-prompts if the caller is silent.
- **Voice-Friendly Output Formatting:** Strip markdown tables, raw URLs (`https://...`), and long bulleted lists from voice responses; use **SSML** `<say-as interpret-as="telephone">` or `<say-as interpret-as="characters">` so order numbers like `ORD-4092` are read digit-by-digit ("O-R-D four zero nine two") instead of "four thousand ninety-two."

---

## Part 3: Module 06 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 6.1
**Scenario:** Margie's Travel relies on three third-party regional ferry booking websites that do not offer any REST APIs, webhooks, or partner connectors. Furthermore, these ferry operators frequently redesign their webpage HTML layouts and add seasonal promotional pop-up banners, which repeatedly break Margie's Travel's existing selector-based RPA scripts. You need to design a Microsoft Copilot Studio agent capability that can navigate these ferry websites, dismiss unexpected pop-ups, check ticket availability, and return prices to travel agents.

**What should you recommend?**
- **A.** Configure Computer Use in Microsoft Copilot Studio with natural-language task instructions and an allowlist of the three ferry domains.
- **B.** Build a Microsoft Graph Connector for SharePoint Online.
- **C.** Configure Voice Mode with SSML tags.
- **D.** Export the agent as a managed solution using Power Platform CLI.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Computer Use** in Microsoft Copilot Studio uses vision-reasoning models to interact with web and desktop user interfaces visually when **no APIs exist** and when **changing UI layouts or pop-up banners** break traditional DOM selector-based RPA scripts.
- **Why B, C, and D are Incorrect:** Graph Connectors index content into M365 search; Voice Mode configures telephony speech; managed solutions are for ALM environment promotion.
</details>

---

### Question 6.2
**Scenario:** Trey Research has an internal platform engineering team that maintains 25 microservices for lab inventory, chemical safety sheets, and equipment calibration. Previously, whenever the engineering team added a new microservice tool or updated parameters, the Power Platform makers had to manually update custom connectors and re-author actions in six different Copilot Studio agents. You need to recommend an open-standard extensibility architecture so that new and updated tools are dynamically discovered by both Copilot Studio agents and Microsoft Foundry agents without re-authoring individual actions in each agent.

**What should you recommend?**
- **A.** Expose the microservices through a centralized Model Context Protocol (MCP) server and connect the Copilot Studio and Microsoft Foundry agents to the MCP server.
- **B.** Hardcode all 25 microservice URLs inside each agent's Fallback topic.
- **C.** Upload PDF screenshots of the microservice code into each agent's direct file uploads.
- **D.** Replace all 25 microservices with Computer Use screen scraping.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Model Context Protocol (MCP)** provides an open standard for exposing **Tools, Resources, and Prompts** from a server so that MCP clients (**Microsoft Copilot Studio** and **Microsoft Foundry**) can dynamically discover tool schemas and updates at runtime without manually re-authoring actions across every agent.
- **Why B & C are Incorrect:** Hardcoding URLs in Fallback topics or uploading PDF screenshots does not provide dynamic tool discovery or execution.
- **Why D is Incorrect:** Never replace working APIs/microservices with UI screen scraping!
</details>

---

### Question 6.3
**Scenario:** City Power & Light is deploying a Microsoft Copilot Studio agent to handle inbound power-outage telephone calls through Dynamics 365 Contact Center. During pilot testing, callers report two problems:
1. When the agent reads out a caller's 8-digit meter number (`10482910`), it pronounces it as *"ten million four hundred eighty-two thousand nine hundred ten"* instead of reading each digit individually.
2. When callers try to interrupt the agent's long greeting message to report a downed power line immediately, the agent keeps talking over them until the entire greeting finishes.

**Which two Voice Mode configurations should you implement in Copilot Studio?**
- **A.** Enable Barge-In (interruption handling) and format the meter number output by using SSML `<say-as interpret-as="digits">` (or `"characters"`).
- **B.** Enable Deep Reasoning Mode (`o3`) on the Greeting topic and disable speech recognition.
- **C.** Switch the agent to an Adaptive Card markdown table and disable DTMF.
- **D.** Increase the model temperature to 0.95 and remove the Escalate topic.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** In Copilot Studio **Voice Mode**, enabling **Barge-In** allows callers to interrupt the agent mid-utterance, and **SSML (`<say-as>`)** controls how numbers, dates, and identifiers are spoken aloud by Azure AI Speech TTS.
- **Why B is Incorrect:** Deep Reasoning Mode increases response latency, which hurts live voice conversations, and disabling speech recognition breaks voice input.
- **Why C & D are Incorrect:** Adaptive Cards cannot be seen on a telephone voice call, and high temperature causes hallucinations.
</details>
