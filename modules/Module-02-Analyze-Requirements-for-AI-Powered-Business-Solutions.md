# Module 02: Analyze Requirements for AI-Powered Business Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 1 — Plan AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** 6 Units (Introduction -> Assess Agents in Task Automation, Data Analytics, and Decision-Making -> Review Data for Grounding -> Organize Business Solution Data for AI Systems -> Module Assessment -> Summary)  
> **Associated Hands-On Lab:** [Lab 01: Enterprise AI Readiness, Grounding Audit & ROI Simulator](../labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### The "Garbage In, Confident Hallucination Out" Problem

Imagine hiring a brilliant new VP of Operations on Monday morning. At 9:05 AM, you lock them in a room with:
- Three conflicting versions of the 2019, 2022, and 2026 Employee Refund Policy PDFs (none of which have dates in the filename),
- An Excel spreadsheet where half the revenue numbers are in USD and half are in EUR without a currency column, and
- A locked filing cabinet they don't have a key to.

Then you ask: *"Should we approve this $50,000 refund for Customer X?"*
Even the smartest human in the world will either guess wrong, quote the 2019 expired policy, or freeze.

**AI agents work the exact same way.** When an AI agent gives a wrong answer in production, **90% of the time it is NOT a model intelligence problem—it is a Requirements Analysis or Data Grounding problem.**

In Module 02, you learn how an AB-100 Solution Architect analyzes two things before writing a single prompt:
1. **What kind of work are we asking the agent to do?** (Task Automation vs. Data Analytics vs. Decision-Making)
2. **Is our enterprise data actually ready to ground the agent?** (The 5 Dimensions of Grounding Data Quality + Data Architecture for AI consumption)

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Assess the Use of Agents in Task Automation, Data Analytics, and Decision-Making

When a business unit brings you a process to "AI-enable," you must classify every requirement into one (or a combination) of **three primary functional pillars**:

```
+-----------------------------------------------------------------------------------+
|            THE 3 FUNCTIONAL PILLARS OF AGENTIC WORKLOAD ASSESSMENT                |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  PILLAR 1: TASK AUTOMATION        PILLAR 2: DATA ANALYTICS   PILLAR 3: DECISION-  |
|  ("Doing the repetitive work")    ("Finding the patterns")   MAKING ("Choosing    |
|                                                              the next best move") |
|  • Data entry & extraction        • Natural-language         • Credit/Risk triage |
|  • Ticket triage & routing          queries over ERP/CRM     • Dynamic re-routing |
|  • Invoice/PO matching            • Anomaly detection          of supply chains   |
|  • Password resets & bookings     • Customer sentiment &     • Next-best-action   |
|                                     churn trend mining         recommendations    |
+-----------------------------------------------------------------------------------+
```

#### Deep Comparison Matrix: How to Architect Each Pillar

| Dimension | 1. Task Automation Agents | 2. Data Analytics Agents | 3. Decision-Making Agents |
| :--- | :--- | :--- | :--- |
| **Core Objective** | Eliminate manual, repetitive operational steps across systems. | Transform raw structured/unstructured data into actionable insights, charts, and forecasts. | Evaluate multiple variables, constraints, and policies to recommend or execute optimal choices. |
| **Human Involvement Pattern** | **Human-on-the-Loop** (autonomous execution for standard tasks; human exception handling). | **Human-in-the-Loop** (interactive exploration; human asks follow-up "why" questions). | **Tiered Autonomy**: Autonomous for low-risk decisions (<$500 refund); **Mandatory Human-in-the-Loop Approval** for high-risk/high-value/regulated decisions. |
| **Primary Microsoft Technologies** | • **Copilot Studio** (Agent Flows, Power Platform Connectors, **Computer Use**)<br>• **Power Automate**<br>• **AI Builder** (Document Processing) | • **M365 Copilot Analyst Agent**<br>• **Microsoft Fabric Data Agents** (OneLake / Fabric IQ)<br>• **Foundry Code Interpreter** | • **Foundry Agent Service** (Reasoning models like `o3-mini` / `GPT-5`)<br>• **Copilot Studio Generative Orchestration**<br>• **D365 Sales Qualification / Case Agents** |
| **Key Risk to Mitigate** | Unintended bulk modifications or infinite loops in target transactional systems (mitigate via rate limits & scoped RBAC). | Hallucinated math or misjoined tables (mitigate by generating SQL/DAX/Python via Code Interpreter or Fabric semantic models rather than asking an LLM to do raw mental math!). | Bias, unexplainable black-box denials, regulatory non-compliance (mitigate via **audit trails, citation mandates, and human approval gates**). |

> **Critical Exam Insight:** Never use a generative LLM to perform raw arithmetic on thousands of rows inside a text prompt! For **Data Analytics**, the agent should translate the user's natural language question into a deterministic query (**SQL, KQL, DAX, or Python via Code Interpreter / Microsoft Fabric Data Agent**) and then summarize the verified result.

---

### Unit 3: Review Data for Grounding — Accuracy, Relevance, Timeliness, Cleanliness, and Availability

On Exam AB-100, you will almost certainly face scenario questions testing the **Five Dimensions of Grounding Data Quality**. When an agent retrieves enterprise data (RAG / Grounding) to answer a prompt or make a decision, which specific dimension is failing, and how do you fix it?

#### The 5 Dimensions of Grounding Data Quality (Memorize This Framework!)

| Dimension | What It Means (Plain English) | Real-World Failure Symptom | Architect's Remediation Strategy |
| :--- | :--- | :--- | :--- |
| **1. Accuracy** | Is the data factually correct and reflective of reality? | The CRM says a customer owns "Product Plan A," when they actually upgraded to "Plan C" last month because a sync job broke. | Enforce **Single Source of Truth (SSOT)** validation rules at ingestion, fix upstream sync pipelines, and ground against authoritative transactional databases (Dataverse/ERP) rather than manual spreadsheets. |
| **2. Relevance** | Does the retrieved data actually pertain to the user's specific intent, role, and context? | A user asks *"How do I submit an expense report in Germany?"* and the agent retrieves 50 pages of US Cafeteria Menus and 2018 Marketing slides because the search scope is too broad. | Scope knowledge sources tightly (specific SharePoint folders/sites instead of the whole tenant), add **metadata tags** (Region, Department, Document Type), tune **hybrid search (keyword + vector + semantic ranker)** in Azure AI Search / Foundry IQ. |
| **3. Timeliness (Freshness)** | Is the data up-to-date fast enough for the business decision? | A customer asks *"Is item #402 in stock right now?"* and the agent says *"Yes, 12 units!"* based on a nightly batch index from 24 hours ago, even though it sold out at noon. | Match the grounding mechanism to latency needs: use **real-time API / Connector / MCP tool calls** for highly volatile data (inventory, live order status, stock price) and **indexed RAG** for slower-changing documents (HR policies, manuals). |
| **4. Cleanliness** | Is the data free of duplicates, conflicting obsolete versions, broken formatting, HTML/OCR noise, and unstandardized schemas? | SharePoint contains `Refund_Policy_v1.pdf`, `Refund_Policy_FINAL.docx`, and `Refund_Policy_FINAL_v2_old.pdf`. The agent blends rules from all three and contradicts itself! | Deduplicate repositories, archive/move deprecated documents out of indexed SharePoint libraries, standardize date/currency formats, and use **Azure AI Document Intelligence** layout parsing to cleanly chunk complex tables and PDFs. |
| **5. Availability (Accessibility)** | Can the agent (and the user via OBO) reliably reach and read the data when needed, with proper permissions and acceptable latency? | The data sits on an on-premises SQL server behind a firewall with no gateway, or inside scanned image-only PDFs with no OCR text layer, or permissions block the service account. | Deploy **On-Premises Data Gateway** / **Virtual Network (VNet) integration**, run OCR via Document Intelligence, configure **On-Behalf-Of (OBO)** or **Microsoft Entra Agent ID** RBAC permissions, and verify service SLA/throttling limits. |

```
+-------------------------------------------------------------------------------+
|         QUICK DIAGNOSTIC CHEAT SHEET FOR AB-100 DATA QUALITY QUESTIONS        |
+-------------------------------------------------------------------------------+
|  • Contradictory answers from v1_draft.pdf and v2_final.pdf? -> CLEANLINESS   |
|  • Inventory count is 12 hours old and causes overselling?   -> TIMELINESS    |
|  • Search pulls 100 unrelated HR docs for an IT query?       -> RELEVANCE     |
|  • Source ERP record has wrong phone number/wrong balance?   -> ACCURACY      |
|  • Firewall blocks agent or PDF is an unindexed scan image?  -> AVAILABILITY  |
+-------------------------------------------------------------------------------+
```

---

### Unit 4: Organize Business Solution Data to Be Available for Other AI Systems

In a modern enterprise, you don't build just *one* isolated agent. You have Microsoft 365 Copilot, Copilot Studio agents, Dynamics 365 agents, and custom Microsoft Foundry agents. How do you organize your enterprise data so **all AI systems can consume it securely without duplicating data 15 times**?

#### 1. Zero-Copy & Unified Data Foundation with Microsoft Fabric OneLake and Dataverse
- **Microsoft Dataverse:** The transactional, low-code business data platform backing Dynamics 365 and Power Platform. It provides built-in relational schema, rich metadata, row-level and column-level security, and native **Link to Microsoft Fabric** (zero-copy shortcuts into OneLake).
- **Microsoft Fabric & OneLake:** The unified enterprise data lake. Using **Medallion Architecture** (**Bronze** raw -> **Silver** cleaned/deduplicated/PII-masked -> **Gold** business-ready semantic models & governed data products), data engineers publish **Gold-layer data products** once.
  - **Fabric Data Agents (Fabric IQ):** Expose governed Gold-layer Lakehouses/Warehouses/Semantic Models directly to **Microsoft Copilot Studio** and **Microsoft Foundry**!

#### 2. Choosing the Right Data Integration Pattern for AI Consumption

| Data Source & Scenario | Recommended Integration Mechanism | Why This Pattern Wins |
| :--- | :--- | :--- |
| **External Non-Microsoft Content** (Confluence wikis, Jira tickets, intranet web pages, file shares) needed inside **Microsoft 365 Copilot** search & grounding | **Microsoft Graph Connectors** (Copilot Connectors) | Ingests external metadata and content into the **Microsoft Graph** index with ACL (Access Control List) security trimming so M365 Copilot can reason over it alongside SharePoint/OneDrive. |
| **Live Transactional Queries / Updates** (Checking live SAP order status, creating a ServiceNow ticket, querying a REST API) | **Model Context Protocol (MCP) Server** or **Power Platform Custom Connectors / API Plugins** | Avoids stale data! Queries the source system in real time when the user asks, rather than syncing millions of ephemeral rows into a search index. |
| **Cross-Platform Enterprise Analytical Data** (Historical sales, IoT telemetry, supply chain lakehouse) | **Microsoft Fabric OneLake Shortcuts + Fabric Data Agent** | Zero-copy architecture; preserves governance and semantic definitions (measures, KPIs) across Power BI, Copilot Studio, and Foundry. |
| **Large Unstructured Document Repositories** requiring custom chunking, vector embeddings, and hybrid semantic ranking | **Azure AI Search (Foundry IQ)** with Integrated Vectorization | Automatically chunks documents from Blob Storage/OneLake, generates embeddings via Azure OpenAI, refreshes incrementally on change, and enforces document-level security filters. |

#### 3. Metadata Enrichment & Schema Design for AI Readability
AI agents don't just read raw values—they read **schema names and descriptions**!
- **Bad Column Name in Dataverse / SQL:** `col_fl_09_x` with no description. (An AI agent generating a query has no idea what `col_fl_09_x` means.)
- **Architect-Grade AI-Ready Schema:** Column display name `Customer Lifetime Value (USD)`, logical name `cr_customerlifetimevalueusd`, with an explicit metadata description: *"Total net revenue generated by the account over the past 36 months in USD, excluding taxes and refunds."*
- This practice—enriching column descriptions, table synonyms, and **Business Terms**—dramatically boosts the accuracy of both Dynamics 365 Copilot and Fabric/Dataverse agents.

---

## Part 3: Advanced Architect Trade-Offs & Real-World Patterns

### RAG (Indexed Knowledge) vs. Real-Time Tool Call (API / MCP): The Architect's Litmus Test
When designing data access for an agent, ask three questions:
1. **How fast does the data change?**
   - Sub-minute / transactional (e.g., bank account balance, flight seat availability) -> **Real-time API / Connector / MCP Tool**.
   - Daily / weekly / monthly (e.g., employee handbook, product specifications, legal templates) -> **Indexed Knowledge Source (SharePoint / Graph Connector / Azure AI Search)**.
2. **Does the query require semantic search across long unstructured text, or exact key lookup?**
   - *"What does our policy say about remote work in France?"* -> **Indexed Semantic Search (RAG)**.
   - *"What is the status of Order #ORD-99281?"* -> **Real-time API / Dataverse / MCP Tool Lookup**.
3. **What are the rate limits and cost implications of the backend system?**
   - If a legacy mainframe charges per API call or throttles at 10 requests/second, do not let an autonomous agent hammer it with broad analytical scans—sync read-only analytical snapshots to **Dataverse / Fabric OneLake** and reserve real-time calls for final transactional writes.

---

## Part 4: Module 02 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 2.1
**Scenario:** Coho Winery deployed a Microsoft Copilot Studio agent grounded in a SharePoint Online document library containing standard operating procedures (SOPs) for warehouse safety. Warehouse supervisors report that when they ask the agent about forklift battery charging rules, the agent gives conflicting instructions—sometimes quoting a 15-minute cooldown period from a 2021 draft document and sometimes quoting a 45-minute cooldown period from the 2025 approved policy, both of which sit in the same SharePoint folder.

**Which grounding data quality dimension should you address first?**
- **A.** Availability
- **B.** Timeliness
- **C.** Cleanliness
- **D.** Accuracy of the underlying foundation model

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **C**
- **Why C is Correct:** Having duplicate, obsolete, or unarchived draft versions (`2021 draft` alongside `2025 approved`) in the same grounding repository is a classic **Cleanliness** problem. Deduplicating the library and moving deprecated/draft documents out of the indexed SharePoint folder resolves the contradiction.
- **Why A is Incorrect:** Availability refers to whether the agent can reach and read the data source (e.g., network/permissions/OCR). Here, the agent can read both files just fine.
- **Why B is Incorrect:** Timeliness refers to how quickly live/recent data is refreshed or synced from a source system. The 2025 policy is already in the folder; the problem is that the uncleaned 2021 draft is still sitting beside it.
- **Why D is Incorrect:** The foundation model is faithfully summarizing the conflicting documents provided in its grounding context; changing or tuning the model will not fix dirty source documents.
</details>

---

### Question 2.2
**Scenario:** Wide World Importers wants to build an AI solution that monitors cold-chain temperature sensors on refrigerated shipping containers. When a container's temperature rises above 4°C for more than 10 minutes, the system must automatically evaluate the cargo value, check the nearest port repair facilities, and either automatically reroute the truck (if the reroute cost is under $1,000) or send an urgent approval card with recommended options to the logistics manager in Microsoft Teams (if the reroute cost is $1,000 or more).

**How should you classify this workload and its human oversight model?**
- **A.** Prompt-and-response data analytics with no human oversight.
- **B.** Event-driven autonomous decision-making and task automation with tiered Human-in-the-Loop (HITL) governance.
- **C.** Static rule-based Robotic Process Automation (RPA) using Computer Use.
- **D.** Document grounding via Microsoft Graph Connectors.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** The workload is triggered by an IoT telemetry event (autonomous), evaluates multiple variables and constraints to choose an optimal course of action (decision-making), executes the reroute (task automation), and enforces a financial threshold ($1,000) for mandatory **Human-in-the-Loop (HITL)** approval.
- **Why A is Incorrect:** It is triggered autonomously by sensor events rather than a human prompt, and it requires HITL governance above $1,000.
- **Why C is Incorrect:** Computer Use is for automating legacy GUI screens without APIs, not reasoning over multi-variable logistics decisions.
- **Why D is Incorrect:** Microsoft Graph Connectors index external enterprise documents for search, which does not solve real-time IoT event-driven logistics decision-making.
</details>

---

### Question 2.3
**Scenario:** Woodgrove Bank stores 15,000 internal technical troubleshooting articles in an on-premises Atlassian Confluence wiki. The bank wants employees using Microsoft 365 Copilot Chat to be able to ask troubleshooting questions and receive answers cited from those Confluence articles, while strictly preserving Confluence's user-level access control lists (ACLs).

**What should you recommend to organize and expose this data to Microsoft 365 Copilot?**
- **A.** Fine-tune an Azure OpenAI GPT-4o model on an exported CSV of all 15,000 Confluence articles.
- **B.** Configure a Microsoft Graph Connector for Confluence with external ACL mapping enabled.
- **C.** Copy all 15,000 articles into the system prompt of a Declarative Agent.
- **D.** Use Computer Use in Copilot Studio to open a browser and search Confluence for every user prompt.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** **Microsoft Graph Connectors** (Copilot Connectors) ingest external unstructured content (like Confluence, Jira, ServiceNow) into the Microsoft Graph index while preserving item-level **Access Control Lists (ACLs)** so Microsoft 365 Copilot can ground responses with security trimming.
- **Why A is Incorrect:** Fine-tuning bakes data into model weights, which cannot enforce per-user ACL security trimming and immediately becomes stale when articles change.
- **Why C is Incorrect:** System prompts have strict token limits and cannot hold 15,000 articles or enforce per-document ACLs.
- **Why D is Incorrect:** Computer Use UI automation is slow (tens of seconds per click) and unsuitable for high-scale knowledge retrieval across 15,000 articles.
</details>
