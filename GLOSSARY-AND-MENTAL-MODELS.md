# Humanized Mental Models & Glossary: From Beginner to Agentic AI Architect

> *"If you cannot explain an architecture simply using a real-world mental model, you will get trapped when the requirements change."*

Before diving into the 11 official AB-100 modules, spend 15 minutes reading this guide. We have translated every complex buzzword in the Microsoft Agentic AI ecosystem into **everyday human analogies**, followed by **exact architectural definitions**.

---

## 1. The Core Mental Model: The "Modern Digital Office"

Imagine your enterprise is hiring digital workers. Not every job requires a PhD researcher, and not every worker should have the keys to the company bank vault.

```
+-----------------------------------------------------------------------------------+
|                        THE SPECTRUM OF AI IN THE ENTERPRISE                       |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. Traditional Rule-Based Automation (Power Automate / Classic Chatbot)          |
|     - Analogy: A vending machine. Press B4 -> Get pretzels.                       |
|     - Behavior: 100% deterministic. If you ask for "something salty", it fails.   |
|                                                                                   |
|  2. Prompt-and-Response / Retrieval Assistant (Basic Copilot / RAG Bot)           |
|     - Analogy: A smart corporate librarian with an open-book policy binder.       |
|     - Behavior: You ask a question -> It searches your documents -> Summarizes.   |
|     - Limitation: Waits for a human prompt; does not take multi-step actions.     |
|                                                                                   |
|  3. Task Agent (Copilot Studio Action Agent / Declarative Agent with Plugins)     |
|     - Analogy: A helpful executive assistant sitting beside you.                  |
|     - Behavior: You say "Book my trip and log the expense." It invokes tools      |
|       (APIs, connectors, MCP servers) to execute specific tasks on your behalf.   |
|                                                                                   |
|  4. Autonomous Agent (Copilot Studio Event-Driven / Microsoft Foundry Agent)      |
|     - Analogy: A night-shift operations specialist working while you sleep.       |
|     - Behavior: Triggered by a system event (e.g., a broken supply chain shipment |
|       in Dynamics 365). It perceives the problem, reasons through options,        |
|       creates a multi-step plan, invokes tools, and only pings a human when an    |
|       exception exceeds its approval threshold ($10,000).                         |
|                                                                                   |
|  5. Multi-Agent System (Orchestrator + Specialist Agents via A2A)                 |
|     - Analogy: A Hospital Emergency Room or General Contractor with Sub-trades.   |
|     - Behavior: A Triage/Orchestrator Agent receives a complex goal, breaks it    |
|       down, delegates sub-tasks to Specialist Agents (Finance Agent, Legal Agent, |
|       Inventory Agent), synthesizes their work, and verifies the final outcome.   |
+-----------------------------------------------------------------------------------+
```

---

## 2. How an AI Agent Actually Thinks: Perceive -> Reason -> Act -> Learn

Whether an agent is built in **Microsoft Copilot Studio** or **Microsoft Foundry**, every true agentic loop follows four stages:

1. **Perceive (Sensors & Triggers):**
   - *Human Analogy:* Hearing a phone ring, reading an incoming email, or seeing a warning light on a dashboard.
   - *Microsoft Stack:* A user message in Microsoft Teams, a new row created in **Microsoft Dataverse**, an event in **Azure Event Grid**, or a business event in **Dynamics 365 Supply Chain Management**.
2. **Reason & Plan (Brain + Memory + Grounding):**
   - *Human Analogy:* Checking the company handbook, remembering what the customer said five minutes ago, and deciding which three steps are needed to solve their problem.
   - *Microsoft Stack:* **Generative AI Orchestration** (in Copilot Studio) or **Foundry Agent Service** powered by an LLM/SLM, grounded in **Microsoft Graph**, **Dataverse**, **SharePoint**, or **Azure AI Search / Foundry IQ**, using short-term thread history and long-term memory.
3. **Act (Hands & Tools):**
   - *Human Analogy:* Filling out a form in CRM, sending an invoice, or clicking buttons on an old desktop screen.
   - *Microsoft Stack:* **Power Platform Connectors**, **Agent Flows**, **REST API Plugins**, **Model Context Protocol (MCP) Servers**, **Code Interpreter**, or **Computer Use (CUA)**.
4. **Learn & Govern (Feedback & Guardrails):**
   - *Human Analogy:* A supervisor reviewing call recordings, checking compliance rules, and coaching the employee to do better next week.
   - *Microsoft Stack:* **Azure AI Content Safety Guardrails**, **Application Insights Telemetry**, **Copilot Studio Analytics**, **Foundry Evaluators**, and **Human-in-the-Loop (HITL)** feedback.

---

## 3. The "Big Five" Architectural Concepts You Must Master

### Concept A: Grounding & RAG (Retrieval-Augmented Generation) vs. Fine-Tuning
- **Beginner Analogy:**
  - **Pre-trained LLM** = A brilliant university graduate who read the public internet up to last year, but has *never* worked at your company. If you ask about your company's refund policy, they will guess (**hallucinate**).
  - **Grounding / RAG** = Giving that graduate an **open-book binder** of your latest company policies right before they answer a question, and telling them: *"Only answer using pages from this binder, and cite the page number."*
  - **Fine-Tuning (Custom Model Tuning)** = Sending that graduate to **medical school or law school** for six months so they learn a new *style, tone, domain vocabulary, or specialized task format*.
- **Architect's Exam Rule:**
  - Need the AI to know **frequently changing facts, company documents, live CRM records, or permissions-trimmed data**? -> **Use Grounding / RAG** (never fine-tuning!).
  - Need the AI to adopt a **strict proprietary output format, specialized medical/legal classification tone, or run on a tiny low-latency Small Language Model (SLM)**? -> **Use Fine-Tuning**.

### Concept B: MCP (Model Context Protocol) vs. A2A (Agent2Agent Protocol)
This is one of the highest-yield topics on Exam AB-100. Don't confuse them!

```
+------------------------+           A2A Protocol            +------------------------+
|   Orchestrator Agent   | <===============================> |    Specialist Agent    |
|   (Copilot Studio)     |   (Agent-to-Agent Delegation,     |  (Microsoft Foundry)   |
+------------------------+    Task State, Negotiation)       +------------------------+
            |                                                            |
            | MCP (Model Context Protocol)                               | MCP
            v                                                            v
+------------------------+                                   +------------------------+
|    MCP Tool Server     |                                   |    MCP Tool Server     |
| (SharePoint / ERP API) |                                   | (SQL / GitHub / Tools) |
+------------------------+                                   +------------------------+
```

- **MCP (Model Context Protocol) = "Agent-to-Tool / Agent-to-Data" (Vertical Connection)**
  - *Analogy:* **USB-C for AI.** Before USB-C, every phone and laptop needed a different charger cable. Before MCP, every AI platform needed a custom-written connector for every database or API. With MCP, an organization builds *one* MCP Server exposing **Tools** (executable functions), **Resources** (contextual data), and **Prompts** (reusable templates), and *any* MCP-compatible client (Copilot Studio, Microsoft Foundry, VS Code GitHub Copilot) can plug right into it and automatically discover tools at runtime!
- **A2A (Agent2Agent Protocol) = "Agent-to-Agent" (Horizontal Collaboration)**
  - *Analogy:* **Two specialist doctors consulting each other on a patient case.** Agent A doesn't want to know *how* Agent B queries its database or which tools Agent B uses internally. Agent A simply discovers Agent B's capabilities via an **Agent Card**, hands off a high-level task with context, and receives the completed result or status update.

### Concept C: Build vs. Buy vs. Extend (The Three-Layer Decision Pyramid)
Whenever an AB-100 exam question asks *"What should you recommend?"*, apply Microsoft's **Adopt (Buy) -> Extend -> Build** hierarchy:

1. **Adopt (Buy / Out-of-the-Box First):**
   - If a prebuilt agent already solves 80–100% of the business need (e.g., **Microsoft 365 Copilot**, **Microsoft 365 Copilot for Sales**, **Dynamics 365 Customer Service Case Summary**, **Account Reconciliation Agent in Dynamics 365 Finance**), **use it first**. Fastest time-to-value, lowest TCO, Microsoft manages model updates and security.
2. **Extend (Low-Code Customization):**
   - If users already work inside Microsoft 365 or Dynamics 365, but the prebuilt Copilot needs access to a custom line-of-business API, external knowledge source, or specific workflow, **extend it** using a **Declarative Agent**, **Microsoft Graph Connector**, **Power Platform Connector**, or **Copilot Studio Agent**.
3. **Build From Scratch (Pro-Code in Microsoft Foundry):**
   - Only build a custom engine agent in **Microsoft Foundry** when you require **multi-model selection** (e.g., Llama, Mistral, Phi, fine-tuned GPT), **custom RAG chunking/vector pipelines**, **code-first orchestration (Semantic Kernel / AutoGen / Microsoft Agent Framework)**, or embedding inside a custom consumer/enterprise web application outside M365.

### Concept D: Standard NLP vs. CLU vs. Generative AI Orchestration in Copilot Studio
In Copilot Studio, how does the agent understand what the user wants and decide which topic or tool to run?
- **Standard NLP (Classic NLU):** Matches user utterances against trigger phrases you manually typed in each topic. Fast and predictable, great for simple single-language bots.
- **CLU (Azure AI Conversational Language Understanding):** Uses a custom-trained Azure AI Language model. Choose this when you need **strict deterministic confidence scores**, **custom entity extraction rules**, **multilingual intent recognition with custom training utterances**, or **industry-specific jargon** where generative routing isn't allowed.
- **Generative AI Orchestration (Dynamic Chaining):** The LLM reads the **human-readable `Description`** of every Topic, Action, Connector, MCP tool, and Child Agent, and dynamically plans which tool(s) to call—even chaining three tools together in a single turn!
  - *Crucial Architect Rule:* In Generative AI Orchestration, **the quality of your tool/topic `Description` is everything**! If two tools have vague or overlapping descriptions, the orchestrator will pick the wrong tool.

### Concept E: Small Language Models (SLMs) & Model Routers
- **Frontier Large Language Models (e.g., GPT-4o, GPT-5, o3-mini):** Deep multi-step reasoning, broad world knowledge, complex planning—but higher latency and higher token cost.
- **Small Language Models (SLMs, e.g., Microsoft Phi-4 / Phi-3.5):** Compact models (3B–14B parameters) that are **blazingly fast, 10x–25x cheaper**, can run at the **edge/on-device (NPU)** or in strict low-latency loops, and excel at classification, entity extraction, PII scrubbing, and narrow domain tasks (especially when fine-tuned).
- **Model Router:** An intelligent traffic cop in **Microsoft Foundry** that inspects each incoming prompt's complexity and automatically routes simple queries (70% of traffic, like *"Check order status"*) to a fast, cheap SLM, while routing complex queries (30% of traffic, like *"Analyze three supplier contracts and negotiate a mitigation plan"*) to a frontier reasoning model.

---

## 4. Comprehensive A–Z Glossary for AB-100

| Term | Plain-English Definition & AB-100 Exam Context |
| :--- | :--- |
| **Agent Card (A2A)** | A JSON metadata manifest published by an agent in the Agent2Agent (A2A) protocol that advertises its identity, skills, input/output schemas, and authentication requirements so other agents can discover and invoke it. |
| **Agent Feed** | A unified UI surface in modern business apps (such as Power Apps and Dynamics 365) where users supervise autonomous and task agents, see what agents have completed in the background, and approve/resolve exceptions (Human-in-the-Loop). |
| **Agent Flows** | Deterministic, step-by-step automated workflows built inside Microsoft Copilot Studio that combine structured logic, connectors, and AI prompt actions for repeatable business processes. |
| **AI Builder (AI Hub)** | The low-code AI capability inside Power Platform that provides prebuilt models (invoice processing, receipt scanning, sentiment analysis) and custom Prompt Builder templates usable in Power Apps and Power Automate. |
| **AI Center of Excellence (AI CoE)** | A cross-functional governance and enablement team (executive sponsor, AI architects, security/compliance leads, business champions, platform engineers) that sets standards, reusable prompt libraries, DLP rules, and ROI tracking across the organization. |
| **AI Red Teaming** | Proactive adversarial testing (manual or automated via the **Foundry AI Red Teaming Agent** powered by PyRIT) that probes AI models and agents for jailbreaks, prompt injection, PII leakage, and harmful outputs before production deployment. |
| **Business Terms (Dynamics 365)** | Organization-specific vocabulary, acronyms, and calculation definitions configured in Dynamics 365 Customer Service / Customer Experience so Copilot accurately understands company jargon (e.g., knowing that "Gold Tier VIP" means `AnnualRevenue > $500k`). |
| **Cloud Adoption Framework (CAF) for AI** | Microsoft's structured lifecycle framework for enterprise AI adoption: **Strategy -> Plan -> Ready -> Adopt (Build/Integrate) -> Govern & Secure -> Manage**. |
| **Computer Use (CUA)** | A capability in Microsoft Copilot Studio that allows an agent to visually read screens and click/type on desktop or web applications that lack APIs or connectors, adapting dynamically if UI layouts shift slightly. |
| **Copilot Studio Kit** | An open-source solution from Microsoft Power CAT that adds automated batch testing, KPI dashboards, conversation transcript mining, and AI-graded test assertions (groundedness/similarity) to Copilot Studio. |
| **Cross-Prompt Injection Attack (XPIA)** | Also called **Indirect Prompt Injection**. An attack where malicious instructions are hidden inside external data (an email, a webpage, a PDF resume, or a CRM record) that the agent retrieves during grounding, tricking the agent into executing unauthorized actions. Mitigated with **Azure AI Content Safety Prompt Shields**. |
| **Declarative Agent** | A lightweight extension of **Microsoft 365 Copilot** defined via JSON manifests (`declarativeAgent.json`) that gives M365 Copilot custom instructions, scoped knowledge (SharePoint, OneDrive, Graph Connectors), and custom actions (API plugins) while still using M365 Copilot's built-in orchestrator and foundation model. |
| **DSPM for AI (Microsoft Purview)** | **Data Security Posture Management for AI** in Microsoft Purview. Gives admins visibility into sensitive data exposure in AI prompts/responses, shadow AI usage, oversharing risks in SharePoint grounding data, and one-click DLP/labeling policies. |
| **Fallback Topic** | The safety-net system topic in Copilot Studio that triggers when the agent cannot match a user's intent to any topic or knowledge source. Can be customized to log unrecognized queries, ask the user to rephrase, call a specialized API, or escalate to a human agent. |
| **Groundedness** | An evaluation metric (scored 1–5 in Microsoft Foundry) measuring whether every factual claim in the AI's generated response is directly supported by the retrieved source documents (preventing hallucinations). |
| **Managed Solution vs. Unmanaged Solution** | In Power Platform & Copilot Studio ALM: **Unmanaged solutions** are used *only* in Development environments to add/edit components. **Managed solutions** are locked, immutable packages exported from Dev and imported into **Test/UAT and Production** environments via automated CI/CD pipelines. |
| **Microsoft Entra Agent ID** | Dedicated identity type in Microsoft Entra ID designed specifically for AI agents, allowing security teams to assign least-privilege RBAC, enforce Conditional Access, track agent ownership (sponsors), and audit every action an agent takes independently of human user accounts. |
| **On-Behalf-Of (OBO) Authentication** | Identity flow where an agent accesses backend data (like SharePoint or Dataverse) using the **signed-in user's own identity and permissions**, ensuring the agent can never expose a document the user isn't allowed to read. |
