# Module 03: Design Overall AI Strategy for Business Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 1 — Plan AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** All 19 Units (CAF AI Adoption -> Agent Strategy -> Multi-Agent Design -> Prebuilt Agents -> Rules & Constraints -> Copilot Studio Knowledge Sources -> Custom vs. Extend M365 Copilot -> Custom AI Models -> Prompt Library -> Small Language Models (SLMs) -> Prompt Engineering -> Business User Roles -> Regional Data Compliance -> AI Center of Excellence -> Multi-D365 App Solutions -> User Prompt Training -> Module Assessment -> Summary)  
> **Associated Hands-On Labs:** [Lab 01: Readiness & ROI Simulator](../labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md) & [Lab 02: SharePoint Embedded & M365 Declarative Agent](../labs/Lab-02-SharePoint-Embedded-and-M365-Declarative-Agent/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Why "Random Acts of AI" Fail in Enterprises

Imagine a city with no urban planning department, no building codes, and no traffic lights. One neighborhood builds a 40-story skyscraper on sand, another builds a bridge that stops halfway across the river, and everyone drives on whichever side of the road they feel like.

That is what happens when an enterprise adopts AI without an **Overall AI Strategy**. Marketing builds a rogue chatbot that accidentally exposes unannounced product pricing; Finance pays $15,000/month for a frontier reasoning LLM just to classify 3-word expense tags; and IT blocks everything out of fear.

In Module 03—the largest strategic module in the entire AB-100 curriculum—you learn how to be the **Chief Urban Planner for Enterprise AI**. You will master:
1. **The Blueprint (Cloud Adoption Framework for AI & AI Center of Excellence):** How to move from chaos to a governed, repeatable factory.
2. **The Architecture Decisions:** When to extend **Microsoft 365 Copilot** vs. build a standalone agent in **Copilot Studio** vs. engineer a custom model/multi-agent system in **Microsoft Foundry**.
3. **The Brains & Prompts:** When to use a tiny, fast **Small Language Model (SLM)** vs. a **Custom Fine-Tuned Model**, and how to standardize **Prompt Engineering & Enterprise Prompt Libraries**.

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Implement the AI Adoption Process from the Cloud Adoption Framework (CAF) for Azure

Microsoft's **Cloud Adoption Framework (CAF) for AI and Agentic Scenarios** divides enterprise transformation into **six structured phases**. On Exam AB-100, you must know what happens in each phase and what happens if a company skips a phase!

```
+-----------------------------------------------------------------------------------+
|       CLOUD ADOPTION FRAMEWORK (CAF) FOR AI & AGENTIC SOLUTIONS LIFECYCLE         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. STRATEGY   --> Define business outcomes, executive sponsorship, & ROI KPIs.   |
|       |                                                                           |
|  2. PLAN       --> Inventory data readiness, assess skills, prioritize use cases, |
|       |            establish the AI Center of Excellence (AI CoE) & roadmap.      |
|  3. READY      --> Provision Azure Landing Zones, Power Platform environments,    |
|       |            Microsoft Foundry hubs/projects, & identity (Entra Agent ID).  |
|  4. ADOPT      --> Build/Extend/Buy agents (M365 Copilot, Copilot Studio,         |
|       |            Foundry), onboard users, & run prompt literacy training.       |
|  5. GOVERN     --> Enforce Responsible AI, Purview DLP, Content Safety guardrails,|
|       & SECURE     data residency, cost quotas, and AI Red Teaming.               |
|       |                                                                           |
|  6. MANAGE     --> Continuous telemetry (App Insights, Viva Insights), drift      |
|                    detection, evaluation loops, and backlog optimization.         |
+-----------------------------------------------------------------------------------+
```

> **Exam Trap Alert:** Notice that **Govern & Secure** and **Manage** are not one-time final steps—they wrap around **Ready** and **Adopt**. In CAF for AI, you establish **Landing Zones and Baseline Governance (DLP, Entra ID, Purview)** *before* scaling agent development to business units.

---

### Unit 3 & Unit 4: Design the Strategy for Building AI & Multi-Agent Solutions Across Platforms

As problems grow complex, a **single monolith agent** starts to fail. Why?
- If you give one single agent **60 different tools**, **15 SharePoint sites**, and **a 4,000-word instruction prompt**, its accuracy drops sharply (context window pollution, tool selection confusion, higher token cost, and impossible security scoping).

#### The Solution: Multi-Agent Architecture across M365 Copilot, Copilot Studio, and Microsoft Foundry

In a multi-agent system, you split responsibilities across **specialized agents** coordinated by an **Orchestrator**:

```
                      [ Employee in Microsoft Teams / M365 Copilot ]
                                            |
                                            v
                   +-------------------------------------------------+
                   |        FRONT-DOOR ORCHESTRATOR AGENT            |
                   |   (Microsoft 365 Copilot / Copilot Studio)      |
                   +-------------------------------------------------+
                      /                     |                      \
     (Child Agent / A2A)           (Connector / MCP)         (A2A / Foundry Endpoint)
                    /                       |                        \
                   v                        v                         v
    +--------------------------+  +--------------------+  +--------------------------+
    |  HR & Policy Specialist  |  | CRM Order Agent    |  | Deep Risk & Quant Agent  |
    |  (Copilot Studio Agent   |  | (Dynamics 365      |  | (Microsoft Foundry Agent |
    |   grounded in SharePoint)|  |  Sales / Service)  |  |  using Fine-Tuned SLM    |
    +--------------------------+  +--------------------+  |  + Code Interpreter)     |
                                                          +--------------------------+
```

#### Core Multi-Agent Orchestration Patterns (Know When to Pick Each!)

| Multi-Agent Pattern | How It Works | Best Business Use Case | Pros & Trade-Offs |
| :--- | :--- | :--- | :--- |
| **1. Orchestrator-Specialist (Supervisor / Hub-and-Spoke)** | A central **Orchestrator Agent** receives the user request, decomposes the goal into sub-tasks, delegates to domain **Specialist Agents** (via Child Agents or **A2A protocol**), and synthesizes their outputs. | Enterprise Concierge spanning HR, IT, Legal, and Finance where each department owns and governs its own specialist agent. | **Pro:** Clear security boundaries and modular ownership.<br>**Con:** Central orchestrator is a single point of routing logic. |
| **2. Sequential Chaining (Pipeline / Assembly Line)** | Agent A completes Step 1 and passes its structured output to Agent B for Step 2, which passes to Agent C for Step 3. | **Contract Review Pipeline:** Document Extraction Agent -> Clause Risk Analysis Agent -> Legal Summary & Redline Drafting Agent. | **Pro:** Deterministic, easy to audit and debug.<br>**Con:** Total latency is the sum of all steps (`Latency = T1 + T2 + T3`). |
| **3. Parallel Fan-Out / Fan-In (Concurrent Execution)** | An orchestrator sends the same context to 3 specialist agents **simultaneously** (e.g., Technical Feasibility Agent, Financial Pricing Agent, Legal Compliance Agent) and aggregates their responses. | **RFP (Request for Proposal) Response Generation** or **360-Degree Customer Onboarding Triage**. | **Pro:** Minimizes wall-clock latency (`Latency = max(T1, T2, T3)`).<br>**Con:** Higher peak token consumption (TPM). |
| **4. Maker-Checker (Generator-Critic / Reflection Loop)** | Agent A (**Generator**) drafts a response, code snippet, or SQL query. Agent B (**Critic/Evaluator**) checks it against strict compliance rules or schemas and either approves it or sends it back to Agent A with feedback. | **Regulated Financial Advice Auditing**, **Automated Code Generation**, or **Medical Claim Denial Letters**. | **Pro:** Dramatically reduces hallucinations and policy violations.<br>**Con:** Doubles token usage per turn. |
| **5. Handoff / Swarm Routing** | Agent A handles initial triage and then transfers full control of the conversation session to Specialist Agent B (or a live human agent in Dynamics 365 Contact Center). | **Contact Center Escalation:** General Reception Agent transfers a billing dispute directly to the Fraud Specialist Agent. | **Pro:** Low latency after handoff.<br>**Con:** Requires passing conversation transcript/context summary cleanly during transfer. |

---

### Unit 5 & Unit 6: Prebuilt Agent Use Cases & Defining Solution Rules and Constraints

When building AI components across **Copilot Studio**, **Microsoft Foundry**, and **Microsoft Foundry Tools**, an architect must explicitly document **Solution Rules and Constraints**:
1. **Operational Boundaries (What the Agent Must NEVER Do):**
   - Example: *"The agent may answer questions about mortgage interest rates, but must never provide personalized investment advice or approve loans over $25,000 without a human loan officer's digital signature."*
2. **Latency & Throughput Constraints:**
   - Voice agents in **Dynamics 365 Contact Center** require sub-2-second response latency (favoring streaming endpoints, Provisioned Throughput Units [PTUs], or low-latency models).
   - Asynchronous background agents (like nightly invoice reconciliation) can tolerate 30–60 seconds of deep reasoning (`o3-mini` / `GPT-5` reasoning models).
3. **Authentication & Authorization Constraints:**
   - Must the agent act under the **User's Identity (On-Behalf-Of / OBO)** so it respects row-level security in Dataverse/SharePoint, or under a **Service Identity (Microsoft Entra Agent ID / Managed Identity)** for background autonomous tasks?
4. **Licensing & Quota Constraints:**
   - Copilot Studio message pack consumption rates (e.g., classic answer vs. generative answer vs. autonomous agent flow actions) and Azure OpenAI Tokens-Per-Minute (TPM) regional quotas.

---

### Unit 7: Determine Generative AI Knowledge Sources for Agents Built in Copilot Studio

When you open **Microsoft Copilot Studio** and add a **Knowledge Source** to an agent, what are your options, what are their limits, and how does security work?

| Copilot Studio Knowledge Source | Authentication / Security Model | Best Use Case & Architect Notes |
| :--- | :--- | :--- |
| **Public Websites** | None (Public anonymous web crawl via Bing index) | Adding up to public domain URLs (e.g., `contoso.com/support`) for external customer-facing FAQs. Never use for internal data! |
| **SharePoint & OneDrive for Business** | **User's Identity (OBO)** by default | Grounding on internal Word, PDF, PowerPoint, and Excel files. **Automatically enforces SharePoint user permissions**—if User1 cannot open `Executive_Bonus.pdf` in SharePoint, the agent will not use it to answer User1. |
| **Microsoft Dataverse** | **User's Identity (OBO)** or configured maker credentials | Grounding on structured business tables (Accounts, Cases, Orders, Custom Tables). Supports natural language to structured table retrieval with Dataverse row/column security. |
| **Uploaded Documents (Direct File Upload)** | **Shared / Public to all users of the agent!** (Stored in Dataverse file storage) | **CRITICAL EXAM TRAP:** Files uploaded directly into the agent's Knowledge tab do **NOT** have per-user ACL security trimming! Every user who can talk to the agent can get answers from uploaded files. Use only for policies applicable to *all* users of that agent. |
| **Azure AI Search (Foundry IQ)** | API Key, Managed Identity, or Entra ID integrated ACLs | Enterprise-scale vector/hybrid search over millions of custom-chunked documents in Azure Blob Storage / OneLake. |
| **Microsoft Graph Connectors (Copilot Connectors)** | Entra ID / External ACL mapping | Enterprise knowledge synced into Microsoft Graph from ServiceNow, Confluence, Jira, Salesforce, or on-premises file shares. |
| **Real-Time Enterprise Data via Connectors / MCP** | OBO or Service Principal | Live queries to SQL Server, SAP, Zendesk, or custom MCP servers. |

---

### Unit 8: Determine When to Build Custom Agents or Extend Microsoft 365 Copilot

This is one of the most frequently tested architectural judgment calls on Exam AB-100. Look at the three main options and their exact decision criteria:

```
+-----------------------------------------------------------------------------------+
|   DECISION TREE: EXTEND M365 COPILOT vs. COPILOT STUDIO vs. MICROSOFT FOUNDRY     |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Q1: Are users already licensed for M365 Copilot and working inside               |
|      Teams / Outlook / Word / BizChat, needing scoped instructions +              |
|      SharePoint/Graph knowledge + simple REST API actions?                        |
|      ├── YES ---> Build a DECLARATIVE AGENT (in M365 Copilot / Agent Builder      |
|      |            or Copilot Studio / Microsoft 365 Agents Toolkit).              |
|      |            (Uses M365 Copilot's built-in orchestrator & foundation model!) |
|      └── NO  ---> Go to Q2.                                                       |
|                                                                                   |
|  Q2: Do you need custom conversational dialog flows (Topics), Autonomous          |
|      event triggers, Computer Use, multi-channel publishing (external website,    |
|      WhatsApp, D365 Contact Center, Teams without per-user M365 Copilot license), |
|      or low-code Agent Flows?                                                     |
|      ├── YES ---> Build a CUSTOM AGENT in MICROSOFT COPILOT STUDIO.               |
|      └── NO  ---> Go to Q3.                                                       |
|                                                                                   |
|  Q3: Do you need a custom orchestrator, non-default/fine-tuned models (Phi,       |
|      Llama, Mistral), Model Router, custom Python/C# code-first agent loops,      |
|      or embedding inside a custom line-of-business web/mobile app?                |
|      └── YES ---> Build a CUSTOM ENGINE AGENT in MICROSOFT FOUNDRY                |
|                   (optionally published back to M365/Teams via M365 Agents SDK!). |
+-----------------------------------------------------------------------------------+
```

---

### Unit 9 & Unit 11: Custom AI Models vs. Customized Small Language Models (SLMs)

#### When Should You Create or Fine-Tune a Custom AI Model?
Do **NOT** create or fine-tune a custom model just to teach an agent your company's latest product catalog! Use **RAG (Grounding)** for factual knowledge.
**DO create or fine-tune a custom AI model when:**
1. **Domain-Specific Language, Jargon, or Taxonomy:** The model must interpret highly specialized medical codes (ICD-10), legal clauses, semiconductor telemetry, or chemical formulas that general models misinterpret.
2. **Consistent Complex Formatting & Style:** You need the model to output a strict, complex proprietary JSON/XML schema or match a very specific brand voice 99.9% of the time without needing a 3,000-token few-shot prompt on every request (saving huge input token costs!).
3. **Distillation into a Small Language Model (SLM):** You use outputs from a large frontier teacher model (like GPT-4o / GPT-5) to fine-tune a compact student **SLM (like Microsoft Phi-4)** so it achieves frontier-level accuracy on one narrow task at **1/20th the cost and 1/5th the latency**!
4. **Specialized Predictive / Vision / Document Tasks:** Training a custom **Azure AI Document Intelligence** model for proprietary shipping manifests, or a custom **Azure AI Vision** model to detect manufacturing defects on an assembly line.

#### High-Value Use Cases for Small Language Models (SLMs — e.g., Microsoft Phi Family)
- **Edge & On-Device Execution (Offline / Low Connectivity):** Running on factory floors, retail scanners, field service tablets, or Windows Copilot+ PCs with local NPUs where internet connectivity is intermittent or data cannot leave the device.
- **High-Volume, Low-Latency Gatekeepers & Classifiers:** Triage routing, PII scrubbing, intent classification, sentiment scoring, or extracting 5 fields from 1 million daily emails where paying frontier LLM prices would destroy the ROI.
- **Strict Cost & Energy Efficiency Targets:** Sustainable AI initiatives and high-throughput microservices.

---

### Unit 10, Unit 12 & Unit 17: Prompt Engineering Guidelines, Prompt Libraries & User Prompt Training

#### 1. The 4 Elements of an Effective Enterprise Prompt (GCSE Framework)
Microsoft teaches users and makers to structure prompts using four building blocks:
- **G — Goal:** What clearly stated output do you want? (*"Draft a 3-paragraph executive risk summary..."*)
- **C — Context:** Why do you need it, who is the audience, and what are the constraints? (*"...for the Audit Committee, focusing on supply chain delays exceeding 14 days..."*)
- **S — Source:** Which files, tables, or grounding data should it use? (*"...based strictly on the Q3 Supplier Performance table and `Logistics_Report_Oct.docx`..."*)
- **E — Expectations:** How should it be formatted and toned? (*"...formatted as a markdown table with Severity [High/Medium/Low], Owner, and Mitigation Action, using a formal objective tone."*)

#### 2. Advanced Architect Prompt Engineering Techniques
- **System Prompt Architecture:** Explicitly separate **Identity & Tone**, **Scope & Guardrail Boundaries**, **Tool Mandates** (when to call which tool), **Citation Rules**, and **Output Schema**.
- **Few-Shot Prompting:** Include 2–5 concrete `Input -> Expected Output` examples inside the prompt to anchor formatting and edge-case handling.
- **Chain-of-Thought (CoT) / Reasoning Directives:** Instruct the model to evaluate criteria step by step before emitting the final recommendation.
- **Delimiter Separation (Defense Against Prompt Injection):** Wrap untrusted user input or retrieved external text in clear XML tags (e.g., `<untrusted_customer_email>...</untrusted_customer_email>`) and instruct the system prompt never to follow instructions found inside those tags.

#### 3. Guidelines for Creating an Enterprise Prompt Library
An architect doesn't let 5,000 employees reinvent prompts from scratch every morning. Through the **AI Center of Excellence (AI CoE)**, you establish an **Enterprise Prompt Library** (hosted in **Microsoft Copilot Prompt Gallery** and/or shared **Power Platform AI Builder Prompt Templates**):
1. **Categorize by Role and Business Process:** Organize prompts by persona (Sales, Finance, HR, Legal, Customer Service, Software Engineering).
2. **Version Control & Peer Review:** Treat high-impact prompts like code! Store shared system prompts in Git, test them against golden datasets before publishing, and assign an owner and review date.
3. **Parameterize Variables:** Use dynamic input variables (e.g., `{{CustomerName}}`, `{{ContractText}}`, `{{Jurisdiction}}`) so business users simply fill in blanks rather than editing core guardrail instructions.
4. **Include "Before & After" Examples & Warnings:** Show users what a good output looks like and remind them to verify factual citations.

#### 4. Designing User Prompt Training for AI Solution Adoption (Unit 17)
Technology alone never delivers ROI if users don't know how to interact with it. Your adoption strategy must include:
- **Role-Based Hands-On Workshops ("Prompt-a-thons"):** Tailored to real daily tasks of Finance, Sales, or Support teams—not generic AI theory.
- **Champion Networks ("Copilot Champions"):** Peer power-users embedded in each department who share wins and coach colleagues in Teams channels.
- **Habit-Building Nudges & Viva Insights Tracking:** Using the **Microsoft Copilot Dashboard in Viva Insights** to identify low-adoption cohorts and send targeted micro-learning tips.

---

### Unit 13, Unit 14 & Unit 15: Business User Roles, Regional Compliance & The Microsoft AI Center of Excellence (AI CoE)

#### Key Personas & Roles in an Enterprise AI Workload (Unit 13)
| Role | Primary Responsibility in the AI Lifecycle |
| :--- | :--- |
| **Executive Sponsor** | Secures budget, defines strategic business KPIs, removes organizational roadblocks, and chairs the AI steering committee. |
| **AI Solution Architect (You!)** | Translates business requirements into secure, scalable multi-platform architectures across M365 Copilot, Copilot Studio, Foundry, and Dynamics 365. |
| **AI Center of Excellence (AI CoE) Lead** | Governs environment strategy, reusable components, prompt libraries, maker onboarding, and ROI measurement across business units. |
| **Domain Subject Matter Expert (SME) / Business Owner** | Defines business terms, curates clean grounding knowledge, validates golden test datasets, and performs User Acceptance Testing (UAT). |
| **Security, Risk & Compliance Officer** | Defines Purview sensitivity labels, DLP connector classifications, regional data residency rules (GDPR / EU Data Boundary), and Responsible AI sign-off gates. |
| **Citizen Maker vs. Pro Developer** | **Citizen Makers** build low-code Copilot Studio topics and Power Platform flows within governed guardrails; **Pro Developers** build custom Foundry models, MCP servers, and API plugins. |

#### Regional and Local AI Data Regulation Compliance (Unit 14)
When designing global AI solutions (e.g., an enterprise with offices in Frankfurt, Tokyo, and New York):
1. **Data Residency vs. Cross-Region Model Inferencing:**
   - Verify that your **Power Platform environment region**, **Dataverse storage**, and **Microsoft Foundry / Azure OpenAI deployment region** align with local sovereignty laws (e.g., **EU Data Boundary**).
   - Be careful with **Global Standard** vs. **Data Zone Standard (EU / US)** vs. **Regional** model deployments in Microsoft Foundry! If strict country-level data residency is mandated for both storage *and* inferencing processing, select a **Regional** or **Data Zone** deployment rather than Global routing.
2. **Sector & Regional AI Regulations (e.g., EU AI Act, GDPR, HIPAA):**
   - Classify AI workloads by risk tier (e.g., under the EU AI Act, using AI for **HR recruitment/CV screening** or **credit scoring** is classified as **High-Risk**, requiring strict human oversight, bias auditing, technical documentation, and audit logs).

#### Essential Elements of a Microsoft AI Center of Excellence (AI CoE) (Unit 15)
An **AI CoE** is not an ivory-tower bureaucracy that says "No" to everything—it is an **enablement and governance engine** composed of five core pillars:
1. **Intake & Prioritization Funnel:** A standardized scoring rubric to evaluate proposed AI ideas by Business Value vs. Technical/Data Feasibility vs. Risk.
2. **Architecture & Reusable Asset Catalog:** Approved reference architectures, shared MCP servers, vetted Power Platform custom connectors, and the Enterprise Prompt Library.
3. **Environment & Guardrail Governance:** Automated provisioning of Developer, Sandbox, and Production environments with baseline **DLP policies**, **Microsoft Entra Agent ID**, and **Purview DSPM for AI**.
4. **Quality, Testing & Responsible AI Review Board:** Mandatory pre-production checklists (groundedness thresholds, AI Red Teaming pass rates, HITL design review).
5. **Adoption, Skilling & Value Realization:** Tracking active usage, time saved, and actual vs. projected ROI across the portfolio.

---

### Unit 16: Design AI Solutions That Use Multiple Dynamics 365 Apps

Enterprises rarely run a single business application in isolation. A single customer journey often spans **CRM (Customer Engagement)** and **ERP (Finance & Operations)**:
- **Scenario Example ("Quote-to-Cash & Service-to-Resolution"):**
  1. A seller in **Dynamics 365 Sales** uses **Microsoft 365 Copilot for Sales** to prepare for a client renewal meeting.
  2. However, the client is furious about two delayed shipments (tracked in **Dynamics 365 Supply Chain Management**), an unpaid disputed invoice (tracked in **Dynamics 365 Finance**), and an open high-severity support ticket (tracked in **Dynamics 365 Customer Service**).
- **How to Architect Cross-Dynamics 365 AI Solutions:**
  - **Dual-Write & Virtual Tables in Microsoft Dataverse:** Expose Dynamics 365 Finance & Supply Chain Management (F&O) tables inside **Microsoft Dataverse** via **Virtual Tables (zero-copy real-time lookup)** or **Dual-Write (near-real-time bidirectional sync)** so a single Copilot Studio agent or Dynamics 365 Copilot can reason across CRM Cases, Sales Opportunities, ERP Invoices, and Inventory on one unified data plane!
  - **Multi-Agent Federation:** Allow the **Dynamics 365 Customer Service Copilot** to invoke a specialist **Copilot Studio / Finance & Operations Agent** (or MCP server) to check live warehouse stock and initiate an RMA (Return Merchandise Authorization) without forcing the support rep to alt-tab between three ERP/CRM screens.

---

## Part 3: Module 03 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 3.1
**Scenario:** Fabrikam, Inc. has 4,000 employees licensed for Microsoft 365 Copilot. The Human Resources team wants employees to be able to ask Microsoft 365 Copilot questions about Fabrikam's internal travel reimbursement rules (stored in a dedicated SharePoint site) and submit travel pre-approval requests via an existing internal REST API. The HR team does not need custom conversational dialog trees, autonomous background triggers, or external website publishing. You need to recommend the simplest, most cost-effective architecture.

**What should you recommend?**
- **A.** Build a custom engine agent in Microsoft Foundry using Python and Semantic Kernel.
- **B.** Create a declarative agent for Microsoft 365 Copilot configured with the SharePoint site as a knowledge source and an API plugin for the travel REST API.
- **C.** Fine-tune a GPT-4o model in Microsoft Foundry on the travel reimbursement PDFs.
- **D.** Build an autonomous agent in Microsoft Copilot Studio using Computer Use.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** Because employees already use Microsoft 365 Copilot and the requirements only need custom instructions, scoped SharePoint knowledge, and a REST API action, extending M365 Copilot with a **Declarative Agent + API Plugin** is the fastest, lowest-maintenance architecture. It reuses M365 Copilot's orchestrator and license.
- **Why A is Incorrect:** A pro-code Custom Engine Agent in Foundry is unnecessary overhead when M365 Copilot's built-in orchestrator handles this natively.
- **Why C is Incorrect:** Fine-tuning is wrong for factual policy retrieval and cannot invoke a REST API to submit travel requests.
- **Why D is Incorrect:** Neither autonomous background triggers nor UI screen automation (Computer Use) is needed when a REST API already exists and interactions are user-initiated inside M365 Copilot.
</details>

---

### Question 3.2
**Scenario:** Contoso Pharmaceuticals is building a Microsoft Copilot Studio agent to help R&D scientists search non-confidential lab equipment manuals. However, a junior maker directly uploaded a sensitive PDF named `2026_Executive_Compensation_Plan.pdf` into the agent's **Uploaded files** knowledge section, assuming that Copilot Studio would automatically check each user's SharePoint permissions before answering questions from that PDF.

**What happens when a regular lab technician asks the agent about executive compensation, and how should you fix the architecture?**
- **A.** The agent blocks the answer automatically because uploaded files enforce SharePoint ACLs; no change is needed.
- **B.** The agent will expose the sensitive compensation data to any user who has access to the agent; you should delete the uploaded file from the agent and store it in a restricted SharePoint site connected as a SharePoint knowledge source with user authentication (OBO).
- **C.** The agent will crash with an HTTP 403 error for all users; you should move the file to a public website.
- **D.** You should keep the file uploaded directly in the agent and add a sentence in the system prompt saying "Please do not tell lab technicians about executive pay."

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** Files uploaded directly into a Copilot Studio agent's Knowledge tab are stored in Dataverse and used to ground answers for **all users of that agent** without per-user ACL security trimming! To enforce document-level permissions, the file must live in a permissioned repository like **SharePoint Online** and be accessed via **On-Behalf-Of (OBO)** user authentication.
- **Why A is Incorrect:** Direct file uploads do not inherit or check SharePoint ACLs.
- **Why C is Incorrect:** It will not return a 403 error; it will gladly answer from the uploaded file.
- **Why D is Incorrect:** System prompt instructions are **not a security boundary** and can be bypassed via prompt injection. Access control must be enforced at the data/identity layer.
</details>

---

### Question 3.3
**Scenario:** Northwind Electric Cars manufactures smart charging stations. They need an AI model that runs locally on an embedded processor inside each charging station (which frequently loses cellular connectivity in underground parking garages) to classify diagnostic fault codes and generate short technician troubleshooting steps in under 150 milliseconds.

**What should you recommend?**
- **A.** A fine-tuned Small Language Model (SLM) such as Microsoft Phi-4 deployed to the edge device.
- **B.** A Global Standard deployment of GPT-5 in Microsoft Foundry called over REST.
- **C.** A Microsoft 365 Copilot Declarative Agent.
- **D.** A SharePoint Embedded Agent.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Small Language Models (SLMs)** like the Microsoft **Phi** family are specifically designed for compact memory footprints, sub-second low latency, narrow domain specialization (via fine-tuning), and **offline/edge execution** where cloud connectivity is unavailable.
- **Why B, C, and D are Incorrect:** All three require active cloud internet connectivity and incur higher network/inference latency.
</details>
