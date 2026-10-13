# Module 05: Design AI Agents for Business Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** All 21 Units (Responsible AI Tenets -> D365 Business Terms -> D365 Copilot Customizations -> D365 Sales Connectors -> D365 Contact Center Channels -> Task Agents -> Autonomous Agents -> Prompt/Response Agents -> Microsoft Foundry Tools -> Code-First Generative Pages & Agent Feed -> Copilot Studio Topics & Fallback -> Data Processing for Grounded AI -> AI in Power Apps Canvas Apps -> Power Platform Well-Architected Framework -> Standard NLP vs. CLU vs. Generative Orchestration -> Agent Flows -> Prompt Actions -> Success Criteria -> Module Assessment -> Summary)  
> **Associated Hands-On Labs:** [Lab 03: Copilot Studio Topics, Fallback & Autonomous Flows](../labs/Lab-03-Copilot-Studio-Topics-Fallback-and-Agent-Flows/README.md), [Lab 04: Dataverse & AI Builder Sentiment Flow](../labs/Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/README.md), [Lab 06: Foundry Tools & Agents](../labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/README.md), [Lab 07: Dynamics 365 Copilot Customization](../labs/Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Moving from "What Should We Build?" to "How Do We Engineer It?"

In Domain 1 (Modules 01–04), you wore your **Strategist Hat**—deciding *why* to use AI, checking if data is clean, and calculating ROI.
Now in **Domain 2 (Module 05)**, you put on your **Chief Designer & Blueprint Architect Hat**.

Imagine you are designing a modern smart hospital:
- You need a **Receptionist** who answers patient visitor questions immediately (**Prompt-and-Response Agent**).
- You need a **Scheduling Nurse** who books MRI rooms, checks insurance APIs, and sends prep instructions when a doctor asks (**Task Agent**).
- You need an **ICU Vital-Signs Monitor** that watches patient sensors 24/7 without anyone typing a prompt, automatically paging the trauma team if oxygen drops (**Autonomous Agent**).
- And on the hospital's central nurse station tablet, you don't want nurses typing 50-word chat prompts all day—you want an **Agent Feed** that shows everything the background agents already prepared so the nurse can click `[Approve]` in one second!

Let's walk through all 21 official units of Module 05 so you can design every one of these components across **Dynamics 365**, **Microsoft Copilot Studio**, **Power Apps**, and **Microsoft Foundry Tools**.

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Core Tenets of Responsible AI Guidelines in Agent Design

Every agent design starts with **Microsoft's Six Responsible AI Principles**:
1. **Fairness:** Ensure AI systems treat all demographic groups equitably (e.g., loan triage or resume screening doesn't penalize protected attributes).
2. **Reliability & Safety:** Ensure agents perform consistently under expected and adversarial conditions, with deterministic fallbacks and **Human-in-the-Loop (HITL)** gates for high-stakes actions.
3. **Privacy & Security:** Enforce least-privilege access (**On-Behalf-Of [OBO]** authentication, **Microsoft Entra Agent ID**, PII redaction, and encryption).
4. **Inclusiveness:** Support accessibility standards (voice mode, screen readers, multilingual translation).
5. **Transparency:** Always disclose when a user is interacting with AI, provide **clickable inline citations** to grounding documents, and explain *why* an agent recommended a decision.
6. **Accountability:** Assign a human sponsor/owner to every agent and maintain immutable **audit trails** of prompts, tool calls, and model versions.

---

### Unit 3, Unit 4, Unit 5 & Unit 6: Designing Copilot & Agents in Dynamics 365 (Customer Service, Sales, and Contact Center)

#### 1. Design Business Terms for Copilot in Dynamics 365 Customer Experience & Service (Unit 3)
Every company has its own secret language. If a support rep asks Dynamics 365 Copilot: *"Show me all open **Red-Alert VIP** tickets for **Project Phoenix**,"* a standard LLM has no idea what "Red-Alert VIP" means in your database schema.
- **How Business Terms Work:**
  - Administrators and architects configure **Business Terms (Glossary / Synonyms / Data Mappings)** in Dynamics 365 Customer Service / Customer Insights / Dataverse.
  - You map the natural-language business term (`"Red-Alert VIP"`) to the exact table, column, and filter condition (`msdyn_priority = 1 AND account.customertypecode = 'Platinum'`).
  - **Architect Best Practice:** Curate business terms with domain SMEs, keep definitions unambiguous, avoid overlapping synonyms, and test natural language queries after publishing.

#### 2. Design Customizations of Copilot in Dynamics 365 Apps for Customer Experience & Service (Unit 4)
Out of the box, Copilot in **Dynamics 365 Customer Service** summarizes cases, drafts emails, and answers questions from internal KB articles. How can an architect customize it?
- **Custom Case & Conversation Summary Fields:** Customize exactly which Dataverse columns (e.g., `Product Serial Number`, `SLA Tier`, `Root Cause Category`, `Escalation History`) Copilot uses to generate the structured Case Summary card.
- **External Knowledge Sources & Plugins:** Extend the agent pane in Dynamics 365 Customer Service using **Microsoft Copilot Studio** to add third-party knowledge bases (SharePoint, Confluence, Azure AI Search) or custom action plugins (e.g., calling an external warranty database).
- **Custom Prompt Plugins:** Embed custom **AI Builder Prompt Actions** directly into the Customer Service workspace so reps can trigger company-specific workflows (e.g., *"Generate Regulatory Root-Cause Report"*).

#### 3. Design Connectors for Copilot in Dynamics 365 Sales (Unit 5)
**Microsoft 365 Copilot for Sales** and **Copilot in Dynamics 365 Sales** live where sellers work (Outlook, Teams, and D365 Sales). To make them truly valuable, you extend them with **Connectors**:
- **Power Platform Connectors (Certified & Custom Connectors):**
  - Connect Copilot for Sales to external CPQ (Configure-Price-Quote) systems, ERP inventory/order status APIs, credit-check bureaus (Dun & Bradstreet), or contract lifecycle management (DocuSign / Ironclad).
- **Design Requirements for Sales Connectors:**
  1. Write crystal-clear **Action Descriptions** and parameter descriptions in the OpenAPI definition so the Copilot orchestrator knows *when* to invoke the connector (e.g., *"Retrieves real-time credit limit and overdue invoice balance for a customer account by Account ID"*).
  2. Use **OAuth 2.0 / Entra ID On-Behalf-Of (OBO)** authentication so a seller only sees pricing and commission data permitted by their security role.

#### 4. Design Agents for Integration with Dynamics 365 Contact Center Channels (Unit 6)
**Dynamics 365 Contact Center** is an omnichannel platform supporting **Voice (Telephony / IVR)**, **Live Web Chat**, **SMS**, **WhatsApp**, **Facebook Messenger**, and **Microsoft Teams**.
When integrating a **Microsoft Copilot Studio agent** into Contact Center channels, an architect must design for:
1. **Channel-Specific Modalities (Voice vs. Digital Text):**
   - **Voice Channel (Interactive Voice Response):** Users cannot click hyperlinks or read 500-word markdown tables over the phone! Configure **Voice Mode behaviors** in Copilot Studio: concise spoken responses, **SSML (Speech Synthesis Markup Language)** prosody/pronunciation tuning, **DTMF (keypad tone)** fallback for entering credit card or account numbers, and **Barge-In (interruption handling)** so the caller can interrupt the bot mid-sentence.
   - **Digital Messaging Channels (Web Chat, WhatsApp, Teams):** Use rich **Adaptive Cards**, quick-reply buttons, and clickable citations.
2. **Seamless Omnichannel Escalation & Context Transfer:**
   - Configure the Copilot Studio agent as a smart front-line representative assigned to a Contact Center **Workstream**.
   - When the agent triggers the **Escalate (Transfer to Agent)** node, pass **Context Variables** (e.g., `AuthenticatedCustomerID`, `IntentCategory`, `SentimentScore`, and full conversation transcript) to **Unified Routing**, which routes the call/chat to the right human queue (e.g., Spanish Billing Queue) and displays an AI-generated **Conversation Summary** to the human rep so the customer never has to repeat themselves!

---

### Unit 7, Unit 8 & Unit 9: Designing Task Agents, Autonomous Agents, and Prompt-and-Response Agents

On Exam AB-100, you will frequently compare the **three core agent archetypes** in Microsoft Copilot Studio and Microsoft Foundry:

```
+-----------------------------------------------------------------------------------+
|                THE 3 AGENT ARCHETYPES IN MICROSOFT COPILOT STUDIO                 |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. PROMPT-AND-RESPONSE AGENT                                                     |
|     [User Question] ---> [Knowledge Grounding (RAG)] ---> [Cited Answer]          |
|     • Stateless or single-turn/multi-turn Q&A over trusted knowledge sources.     |
|                                                                                   |
|  2. TASK AGENT                                                                    |
|     [User Goal] ---> [Orchestrator] ---> [Calls Tool / API / Agent Flow]          |
|                                     ---> [Confirms Action to User]                |
|     • User-initiated, action-oriented; executes discrete business transactions.   |
|                                                                                   |
|  3. AUTONOMOUS AGENT                                                              |
|     [System Event Trigger] ---> [Perceive & Reason] ---> [Multi-Step Plan]        |
|     (Dataverse / Email /        ---> [Execute Tools & Flows]                      |
|      Schedule / Event Grid)     ---> [Log to Agent Feed / Request HITL if needed] |
|     • Event-initiated (no human chat required to start!); runs asynchronously.    |
+-----------------------------------------------------------------------------------+
```

#### Architect's Design Checklist for Autonomous Agents (Unit 8)
Because an **Autonomous Agent** wakes up on an event trigger without a human watching the screen:
1. **Event Trigger Selection:** Define the exact trigger (e.g., *When a row is added or modified in Dataverse*, *When a new email arrives in a shared mailbox*, *On a recurring schedule*).
2. **Explicit Goal & Termination Conditions:** Set a maximum number of reasoning steps/retries so the agent never enters an infinite loop burning thousands of dollars in Copilot Credits.
3. **Maker / Service Credentials vs. User Context:** Since no interactive user is signed in at 3:00 AM, autonomous triggers execute under **configured connection credentials / Microsoft Entra Agent ID**—apply strict **Principle of Least Privilege (PoLP)**!
4. **Exception Handling & Human-in-the-Loop Escalation:** Define clear confidence and financial thresholds. When an exception occurs, write a state record to the **Agent Feed** or send an **Approval Adaptive Card in Teams** and pause until a human responds.

---

### Unit 10: Propose Microsoft Foundry Tools for a Given Requirement

Remember from our terminology guide: **Microsoft Foundry Tools** is the official AB-100 name for Azure's prebuilt and customizable domain AI services (formerly Azure AI Services / Cognitive Services). Memorize which tool solves which requirement:

| Business Requirement Clue | Correct Microsoft Foundry Tool | Key Architectural Capabilities |
| :--- | :--- | :--- |
| Extract structured fields, tables, checkboxes, and key-value pairs from invoices, receipts, tax forms, contracts, or scanned PDFs. | **Azure AI Document Intelligence** | Prebuilt models (Invoices, Receipts, IDs, W-2s), **Layout model** (for RAG table-aware markdown chunking!), and Custom Extraction models. |
| Convert live call center audio to text, synthesize natural lifelike agent voices, or translate live spoken audio. | **Azure AI Speech** | Speech-to-Text (STT), Text-to-Speech (TTS), Custom Neural Voice, Batch Transcription, and Real-time Speech Translation. |
| Detect PII/PHI in text, extract named entities (NER), analyze sentiment, classify custom intents, or summarize documents. | **Azure AI Language** | **PII Detection & Redaction**, Conversational Language Understanding (**CLU**), Custom Question Answering, Entity Linking, Key Phrase Extraction. |
| Analyze images/video for product defects, read text in natural scenes (OCR), or count inventory on shelves. | **Azure AI Vision** | Optical Character Recognition (OCR), Image Analysis, Spatial Analysis, Custom Vision object detection/classification. |
| Translate documents or text payloads across 100+ languages while preserving custom corporate brand terminology. | **Azure AI Translator** | Text Translation, Document Translation (preserves Word/PDF layout), and **Custom Translator** (custom glossaries/dictionaries). |
| Block jailbreaks, indirect prompt injections, hate/violence/sexual/self-harm content, and competitor names. | **Azure AI Content Safety** | **Prompt Shields** (User Prompt Injection + Indirect Document XPIA detection), Severity Filters (0–7), **Groundedness Detection**, Protected Material Detection, and Custom **Blocklists**. |
| Index millions of documents for hybrid keyword + vector search with semantic reranking and document-level security trimming. | **Azure AI Search (Foundry IQ)** | Integrated vectorization, hybrid RRF (Reciprocal Rank Fusion), Semantic Ranker, and ACL security filters. |

---

### Unit 11: Propose Code-First Generative Pages and the Use of an Agent Feed for Apps

Modern agentic business applications (in **Power Apps** and **Dynamics 365**) are moving beyond static forms and tiny corner chat widgets:
1. **Code-First Generative Pages (Dynamic Generative UI):**
   - Instead of forcing a user to click through 8 static screens to compare three delayed manufacturing plants, a **Code-First Generative Page** dynamically assembles and renders interactive UI components (React/PCF controls, charts, comparison grids, action cards) tailored on the fly to the user's natural language goal and current context!
   - Makers and pro-developers can generate and refine full canvas/model-driven pages using natural language + React/TypeScript code components that bind directly to Dataverse and agent outputs.
2. **The Agent Feed (Human-Agent Collaboration Surface):**
   - When an organization runs 5 or 10 **Autonomous Agents** in the background (triaging leads, reconciling invoices, matching POs), users shouldn't have to ask *"Hey bot, what did you do today?"*
   - The **Agent Feed** is a dedicated activity stream inside the business app (Power Apps / Dynamics 365) that categorizes agent work into:
     - **Needs Your Attention / Pending Approval:** Items where an autonomous agent paused for Human-in-the-Loop review (with one-click `[Approve]`, `[Edit]`, or `[Dismiss]` actions).
     - **Completed Autonomously:** Full transparent audit log of tasks the agents finished on their own, with links to the underlying Dataverse records.

---

### Unit 12, Unit 16, Unit 17 & Unit 18: Copilot Studio Topics, Fallback, NLP/CLU/Generative Orchestration, Agent Flows & Prompt Actions

#### 1. Designing Topics and the Custom Fallback Topic in Copilot Studio (Unit 12)
In Copilot Studio, **Topics** are modular conversation paths. Every agent has two types of topics:
- **Custom Topics:** Created by makers for specific business workflows (e.g., *Check Order Status*, *Submit Warranty Claim*, *Request Equipment*).
- **System Topics:** Built-in lifecycle handlers (`Conversation Start`, `Greeting`, `Multiple Topics Matched`, `On Error`, `Escalate`, `End of Conversation`, and **`Fallback`**).
- **How to Architect the `Fallback` Topic:**
  - The **Fallback** topic triggers when a user's utterance doesn't match any topic and cannot be answered by configured **Knowledge Sources** (Conversational Boosting).
  - **Best-Practice Fallback Design Pattern:**
    1. **Track a Fallback Counter (`Global.FallbackCount`):** On the 1st unmatched message, politely ask the user to rephrase or offer quick-reply category buttons.
    2. **Log Unrecognized Utterance:** Write `Activity.Text` to **Application Insights** or a Dataverse backlog table so the AI CoE can discover missing topics/knowledge!
    3. **Escalate on Repeated Failure:** If `Global.FallbackCount >= 2`, automatically redirect to the **Escalate** topic to hand off the conversation (with transcript summary) to a live human agent.

#### 2. Standard NLP vs. CLU vs. Generative AI Orchestration (Unit 16)
How should your Copilot Studio agent route user intents?

| Routing Mode | How It Works | When to Choose It on Exam AB-100 |
| :--- | :--- | :--- |
| **Standard NLP (Classic NLU)** | Matches user utterances against the 5–20 trigger phrases saved inside each Topic. | Simple, highly predictable single-intent agents where dynamic tool chaining is not desired. |
| **Conversational Language Understanding (Azure AI CLU)** | Calls a custom-trained **Azure AI Language CLU** model for intent classification and custom entity extraction. | Strict deterministic routing requirements, **industry-specific jargon/acronyms**, custom confidence score thresholds, or complex multilingual utterance training sets. |
| **Generative AI Orchestration (Dynamic Chaining)** | An LLM inspects the user's message and dynamically selects and chains **Topics, Connectors, MCP Tools, Agent Flows, and Child Agents** based on their natural-language **`Description`**. | Multi-intent queries (*"Check my vacation balance and book a flight to Seattle"*), tool-heavy task agents, and autonomous agents. **Requires high-quality, non-overlapping descriptions on all topics and actions!** |

#### 3. Agent Flows vs. Prompt Actions in Copilot Studio (Unit 17 & Unit 18)
- **Agent Flows (Deterministic Multi-Step Execution):**
  - When a process must follow a **strict, repeatable sequence** every single time (e.g., *Step 1: Validate tax ID format -> Step 2: Query ERP -> Step 3: Write audit row to Dataverse -> Step 4: Send email*), do NOT leave the step order to probabilistic LLM guessing! Build an **Agent Flow** (which combines deterministic workflow actions with embedded AI steps) and expose it as a tool to the agent.
- **Prompt Actions (Custom AI Builder Prompts):**
  - Reusable, structured prompt templates created in **Prompt Builder** (inside Copilot Studio or Power Platform AI Hub).
  - You define **Input Variables** (text, documents, images), **Dataverse Grounding tables**, **Model choice** (e.g., GPT-4o-mini vs. GPT-4o), and **Output Format** (**Text**, **JSON**, or **Document**).
  - **Why Architects Love JSON Output in Prompt Actions:** Setting a Prompt Action's output format to **JSON** guarantees that the LLM returns a strongly typed object (e.g., `{"sentiment": "Negative", "urgencyScore": 9, "category": "Billing", "summary": "..."}`) that downstream Agent Flows, Power Apps, or Dataverse columns can parse reliably without regex failures!

---

### Unit 13, Unit 14 & Unit 15: Data Processing for Grounding, AI in Power Apps Canvas Apps & Power Platform Well-Architected Framework

#### 1. Designing Data Processing Workflows for Grounded AI (Unit 13)
Before unstructured documents (PDFs, scanned contracts, manuals) reach a vector index in **Azure AI Search**, design a **5-stage Data Processing Pipeline**:
1. **Ingestion:** Pull raw files from SharePoint, OneLake, or Azure Blob Storage via change-tracking connectors.
2. **Parsing & Crack (Document Intelligence):** Use **Azure AI Document Intelligence (Layout model)** to extract text while preserving table rows/columns and section headers as clean Markdown.
3. **Data Sanitization & PII Redaction:** Run **Azure AI Language PII Detection** to mask SSNs, credit cards, or patient names before indexing if the index is shared.
4. **Intelligent Chunking:** Split documents by semantic headers/sections (e.g., 500–1,000 tokens with 10%–15% overlap) so tables and clauses aren't sliced in half.
5. **Embedding & Indexing with Security Metadata:** Generate vector embeddings (e.g., `text-embedding-3-large`) and store each chunk alongside its **Source URL, Page Number, Timestamp, and Entra ID Security Group ACLs**.

#### 2. Designing Business Processes with AI in Power Apps Canvas Apps (Unit 14)
How do you embed AI directly into a **Power Apps Canvas App** for frontline workers (e.g., a field technician inspecting wind turbines on an iPad)?
1. **Copilot Control in Canvas Apps:** Add the native Copilot chat control bound to a Dataverse table or custom Copilot Studio agent so users can ask natural language questions about the app's data.
2. **AI Builder Component Controls:** Drag-and-drop prebuilt canvas controls such as **Business Card Reader**, **Receipt Processor**, **Form Processor**, **Object Detector**, or **Text Recognizer** directly onto a screen.
3. **Direct Power Fx Calls to AI Builder Prompts:** Invoke custom Prompt Actions directly inside a button's `OnSelect` formula using Power Fx!
   - Example Power Fx:
     ```powerfx
     Set(varAnalysis, 'Analyze Customer Feedback Prompt'.Predict(txtCustomerNotes.Text));
     Patch(CustomerReviews, Defaults(CustomerReviews), {
         ReviewText: txtCustomerNotes.Text,
         Sentiment: varAnalysis.StructuredOutput.sentiment,
         Urgency: varAnalysis.StructuredOutput.urgencyScore
     });
     ```

#### 3. Applying the Microsoft Power Platform Well-Architected Framework to Intelligent Workloads (Unit 15)
The **Power Platform Well-Architected Framework** has **five pillars** (memorize all five and how they apply to AI agents!):

| Well-Architected Pillar | What It Means for Agentic & Intelligent Workloads |
| :--- | :--- |
| **1. Reliability** | Ensure the agent handles model throttling (HTTP 429), connector timeouts, and malformed JSON gracefully using retry policies, fallback topics, and multi-region/PTU capacity. |
| **2. Security** | Enforce least-privilege access (OBO user auth, Entra Agent ID), Power Platform **DLP policies**, Purview sensitivity labels, and Content Safety prompt injection shields. |
| **3. Operational Excellence** | Automate ALM with **Managed Solutions**, **Environment Variables**, **Connection References**, **Power Platform Pipelines**, **Application Insights telemetry**, and **Copilot Studio Kit** automated testing. |
| **4. Performance Efficiency** | Optimize response latency by selecting right-sized models (SLMs/mini models for simple tasks), caching frequent static lookups, scoping RAG search indexes tightly, and offloading long-running tasks to asynchronous Agent Flows. |
| **5. Experience Optimization** | Design human-centric experiences: clear AI disclosure, clickable source citations, rich Adaptive Cards, voice barge-in support, and **Agent Feeds** that reduce cognitive load. |

---

### Unit 19: Define Success Criteria and Adoption Goals for AI Business Solutions
Every design specification must conclude with **SMART Success Criteria** across three dimensions:
- **Technical Quality Metrics:** Groundedness score $\ge 4.5 / 5.0$, Intent Resolution Rate $\ge 80\%$, P95 Latency $< 2.5\text{ seconds}$, Escalation/Abandonment Rate $< 15\%$.
- **Business Outcome KPIs:** Support ticket deflection rate, Average Handle Time (AHT) reduction, Sales cycle velocity, Cost per transaction.
- **User Adoption & Sentiment Metrics:** Monthly Active Users (MAU), Retention/Repeat usage rate, Thumbs-Up/Thumbs-Down CSAT score, Viva Insights time-saved survey score.

---

## Part 3: Module 05 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 5.1
**Scenario:** Proseware, Inc. uses Microsoft Dynamics 365 Customer Service. Support agents frequently ask the embedded Copilot questions such as *"Which open cases are breaching our **Gold-Shield SLA**?"* or *"Is this customer eligible for a **Fast-Track Swap**?"* Currently, Copilot fails to answer accurately because "Gold-Shield SLA" and "Fast-Track Swap" are internal Proseware terms that map to custom columns and option-set values in Dataverse. You need to ensure Copilot in Dynamics 365 Customer Service understands these internal expressions without writing custom pro-code plugins.

**What should you configure?**
- **A.** Business terms in Dynamics 365 Customer Service mapped to the corresponding Dataverse tables, columns, and conditions.
- **B.** Computer Use in Microsoft Copilot Studio.
- **C.** Azure AI Vision Spatial Analysis.
- **D.** An unmanaged solution export in Power Platform CLI.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** Configuring **Business Terms** in Dynamics 365 apps for customer experience and service teaches Copilot organization-specific vocabulary, acronyms, and exact mappings to underlying Dataverse fields and rules.
- **Why B, C, and D are Incorrect:** Computer Use automates legacy UIs without APIs; Azure AI Vision analyzes camera feeds; exporting an unmanaged solution is an ALM packaging step.
</details>

---

### Question 5.2
**Scenario:** Consolidated Messenger is designing an agent in Microsoft Copilot Studio that must automatically wake up whenever a new customs hold record is created in Microsoft Dataverse, check three external shipping APIs, calculate whether the delay exceeds 48 hours, and either automatically update the delivery schedule or post an exception item to the logistics supervisor's Agent Feed in Power Apps. No human user initiates a chat session to start this process.

**Which combination of agent type and workflow components should you design?**
- **A.** A prompt-and-response agent triggered by a user typing in Microsoft Teams.
- **B.** An autonomous agent in Copilot Studio configured with a Dataverse event trigger, generative orchestration, and deterministic Agent Flows that log exceptions to the Agent Feed.
- **C.** A SharePoint embedded agent with anonymous public web search enabled.
- **D.** A static FAQ topic using Standard NLP trigger phrases.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** Because the process is initiated by a system event (*When a row is created in Dataverse*) rather than a human chat prompt, and executes background reasoning plus structured actions with supervisor exception review in the **Agent Feed**, it is the textbook definition of an **Autonomous Agent** with **Agent Flows**.
- **Why A, C, and D are Incorrect:** All three require a human user to manually start a chat conversation and cannot wake up autonomously on Dataverse database events.
</details>

---

### Question 5.3
**Scenario:** Lamna Healthcare Company is building a Power Apps canvas app for clinic receptionists. When a receptionist pastes a patient's unstructured referral note into a text box and selects a **Classify Referral** button, the app must invoke a custom AI Builder Prompt Action and immediately populate three separate Dataverse columns (`SpecialtyDepartment`, `UrgencyLevel`, and `SummaryNotes`) without parsing errors.

**How should you configure the Prompt Action in AI Builder / Copilot Studio?**
- **A.** Set the Prompt Action output format to **JSON** with a defined schema for `SpecialtyDepartment`, `UrgencyLevel`, and `SummaryNotes`.
- **B.** Set the Prompt Action output format to free-form poetic text and use 15 nested `Mid()` string functions in Power Fx.
- **C.** Use Azure AI Speech Text-to-Speech.
- **D.** Configure a Fallback topic with a 3-turn retry counter.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** Configuring a **Prompt Action** with a **JSON output format** enforces structured output generation, allowing Power Fx in a Canvas App (or an Agent Flow) to directly reference strongly typed properties like `.StructuredOutput.SpecialtyDepartment` and `.StructuredOutput.UrgencyLevel` reliably.
- **Why B is Incorrect:** Free-form text parsed with string functions is brittle and breaks whenever the LLM slightly varies its phrasing.
- **Why C & D are Incorrect:** Speech synthesis and conversational fallback topics are unrelated to structured field extraction in a Canvas App.
</details>
