# Module 08: Monitor, Analyze, and Tune AI Agents

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 3 — Deploy AI-Powered Business Solutions (40–45%)  
> **Official Units Preserved:** All 8 Units (Introduction -> Recommend Process & Tools for Monitoring Agents -> Analyze Backlog & User Feedback -> Apply AI-Based Tools for Issue Identification & Tuning -> Monitor Agent Performance Metrics -> Interpret Telemetry Data for Performance & Model Tuning -> Module Assessment -> Summary)  
> **Associated Hands-On Labs:** [Lab 08: Foundry Agent Evaluation, Red Teaming & Guardrails](../labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/README.md) & [Lab 09: AI Gateway with Azure API Management & Foundry](../labs/Lab-09-AI-Gateway-with-Azure-API-Management-and-Foundry/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Why Launching an Agent on Day 1 Is Only 20% of the Journey

Imagine opening a brand-new restaurant. On Opening Night, you have a menu, a kitchen staff, and recipes. Does a great restaurateur walk away after Opening Night and never check the kitchen again?
Of course not! Every night you check:
- Which dishes did customers send back untouched? (**Thumbs-Down / Abandonment Rate**)
- What did diners ask the waiter for that wasn't on the menu? (**Unmatched Utterances / Backlog Mining**)
- Why is Table 12 waiting 45 minutes for their appetizer? (**Latency & Token Throttling Telemetry**)
- Are the chefs following food safety temperatures? (**Groundedness & Content Safety Guardrail Logs**)

In traditional software, if an API returns `HTTP 200 OK`, the system is "working."
**In Agentic AI, an agent can return `HTTP 200 OK` in 400 milliseconds and still give a completely hallucinated or unhelpful answer!**
That is why **Domain 3 (Deploy)** is weighted at **40–45%** of Exam AB-100. In Module 08, you will master how to monitor, diagnose, and continuously tune agents across **Copilot Studio**, **Microsoft Foundry**, **Microsoft 365**, and **Application Insights**.

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Recommend the Process and Tools Required for Monitoring Agents

On Exam AB-100, you will be given scenarios asking **which monitoring portal or tool** to recommend for a specific observability requirement. Master this **Canonical Monitoring Tool Matrix**:

| Monitoring Tool / Portal | Target Platform | What It Monitors & When to Recommend It |
| :--- | :--- | :--- |
| **Copilot Studio Built-In Analytics** (`copilotstudio.microsoft.com` -> Analytics) | Microsoft Copilot Studio Agents | Out-of-the-box session outcomes (**Resolved**, **Escalated**, **Abandoned**, **Unengaged**), CSAT scores, billing/credit consumption, generative answer citation usage, and autonomous action execution summaries. |
| **Azure Application Insights & Azure Monitor (Log Analytics / KQL)** | Copilot Studio + Microsoft Foundry + Custom Engine Agents | Deep end-to-end **OpenTelemetry distributed tracing**, custom event logging, exception stack traces, P95/P99 latency breakdowns, HTTP 429 throttling alerts, and Kusto Query Language (**KQL**) dashboards across multiple agents! |
| **Microsoft Foundry Control Plane & Observability Dashboard** (`ai.azure.com`) | Microsoft Foundry Models, Agents & Workflows | Continuous online evaluation metrics (**Groundedness, Relevance, Coherence, Fluency**), token consumption (Prompt vs. Completion tokens), latency per step in multi-agent traces, and Content Safety filter hit rates. |
| **Copilot Studio Kit (Power CAT)** | Microsoft Copilot Studio | Conversation transcript mining, aggregated cross-agent KPI dashboards in Power BI, and automated prompt/response quality regression tracking. |
| **Microsoft Copilot Dashboard in Viva Insights** | Microsoft 365 Copilot & M365 Agents | Executive adoption readiness, active usage by department, meeting/email hours saved, and employee sentiment surveys. |
| **Power Platform Admin Center (PPAC)** | Power Platform & Copilot Studio Environments | Tenant/environment capacity consumption (Copilot Credits/Messages), Dataverse storage, DLP policy violations, and connector error rates. |
| **Microsoft Purview (DSPM for AI & Audit Logs)** | Cross-Tenant AI Compliance | Sensitive data exposure in prompts, shadow AI detection, DLP alerts, and immutable compliance audit trails. |

---

### Unit 3 & Unit 4: Analyze Backlog and User Feedback & Apply AI-Based Tools to Identify Issues and Perform Tuning

#### 1. How to Turn User Feedback and Unresolved Queries into an Actionable Tuning Backlog (Unit 3)
Every week, an AI Operations (AIOps) team reviews two streams of user feedback:
- **Explicit Feedback:** Thumbs-up / Thumbs-down reactions, verbatim user comments, and post-chat CSAT survey ratings (1–5 stars).
- **Implicit Behavioral Signals:**
  - **High Abandonment on a Specific Topic:** Users leave mid-conversation because the topic asks too many confusing questions or fails to solve their problem.
  - **High Escalation Rate:** The agent matches the intent, but the user immediately types *"Talk to a human"* because the answer isn't actionable.
  - **Fallback Log (Unrecognized Utterances):** Questions that hit the `Fallback` topic because no Topic or Knowledge Source covered them.

```
+-----------------------------------------------------------------------------------+
|            THE CONTINUOUS AGENT TUNING & BACKLOG FLYWHEEL                         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. COLLECT     ---> Capture Thumbs-Down, CSAT, Fallback transcripts, &           |
|                      Application Insights traces (ConversationTranscript table).  |
|                                                                                   |
|  2. CLUSTER     ---> Use AI-Based Clustering (Dynamics 365 Customer Intent Agent  |
|     & ANALYZE        or Copilot Studio Topic Clustering / Foundry Evaluator)      |
|                      to group 10,000 raw failed queries into top 10 root causes.  |
|                                                                                   |
|  3. PRIORITIZE  ---> Rank backlog by (Volume x Business Impact / CSAT Drop).      |
|                                                                                   |
|  4. TUNE        ---> • Missing Knowledge? -> Add/clean SharePoint doc or KB.      |
|                      • Wrong Tool Picked? -> Refine Tool/Topic Description!       |
|                      • Hallucination?     -> Tighten grounding & lower temp.      |
|                                                                                   |
|  5. VALIDATE    ---> Run golden evaluation test suite before deploying to Prod!   |
+-----------------------------------------------------------------------------------+
```

#### 2. Applying AI-Based Tools to Analyze Issues and Perform Tuning (Unit 4)
Instead of having humans manually read 50,000 chat transcripts, use **AI to diagnose AI**:
- **AI-Assisted Topic & Intent Discovery:** In Copilot Studio and Dynamics 365 (**Customer Intent Agent**), AI clusters unmatched user utterances from historical transcripts and automatically suggests new Topics, trigger phrases, or missing Knowledge Articles (**Customer Knowledge Management Agent**).
- **LLM-as-a-Judge Continuous Evaluators in Microsoft Foundry:** Configure automated sampling (e.g., 10% of live production traces exported to Application Insights) to be scored automatically by Foundry AI Evaluators for **Groundedness**, **Relevance**, and **Retrieval Score**—immediately flagging conversations where Groundedness drops below `3.0` for backlog remediation!
- **Copilot in Azure Monitor / Log Analytics:** Use natural language to generate **KQL (Kusto Query Language)** queries over `customEvents` and `dependencies` tables in Application Insights to pinpoint which backend connector or MCP tool is causing latency spikes.

---

### Unit 5 & Unit 6: Monitor Agent Performance Metrics & Interpret Telemetry Data for Performance and Model Tuning

#### 1. The 4 Conversation Outcome States in Copilot Studio (Know Exact Definitions!)
In Copilot Studio Analytics, every engaged conversation session ends in one of three primary outcome buckets:
1. **Resolved:** The user's intent matched a topic or generative knowledge source, reached the end of the flow (or confirmed resolution in the `End of Conversation` survey), and did **not** escalate to a human. *(Target: Maximize!)*
2. **Escalated:** The session triggered the `Escalate` topic or a `Transfer to Agent` node to hand off to a live human representative. *(Note: Not all escalations are failures—some high-risk scenarios like fraud or bereavement are **designed** to escalate! Separate **Designed Escalation** from **Deflection Failure Escalation**.)*
3. **Abandoned:** An engaged session timed out or the user closed the chat without reaching resolution or escalation. *(Target: Minimize! High abandonment indicates friction, slow responses, or unhelpful answers.)*

#### 2. Diagnostic Guide: How to Interpret Telemetry Symptom Patterns & Tune the Agent (Unit 6)

Memorize this **Architect's Telemetry Troubleshooting Table**—it directly answers some of the hardest scenario questions on Exam AB-100:

| Telemetry / Metric Symptom Observed | Root Cause Diagnosis | Exact Architect Tuning Action |
| :--- | :--- | :--- |
| **High Fallback Rate / Low Topic Match Rate**, even though the knowledge exists in the company. | Either the relevant SharePoint/KB source isn't connected, or topic/tool **Descriptions** in Generative Orchestration don't match the vocabulary users actually type. | 1. Add the missing knowledge source or configure **Business Terms**.<br>2. Update Topic/Tool **`Description`** fields with user-centric synonyms so the Generative Orchestrator matches them. |
| **High Retrieval Score (Azure AI Search finds the right chunks), BUT Low Groundedness Score (Agent still hallucinates facts).** | The search index is working fine, but the **System Prompt / Model Temperature** allows the LLM to extrapolate using pre-trained internet memory instead of sticking strictly to retrieved chunks. | 1. Lower model **`temperature`** (e.g., to `0.0` or `0.1`).<br>2. Strengthen system prompt instructions: *"Answer strictly using the retrieved context; if not present, state that you do not know."*<br>3. Enable **Groundedness Detection guardrail** in Azure AI Content Safety. |
| **Low Retrieval Score AND Low Groundedness Score.** | The RAG search step is failing to pull the right document chunks into the context window! | 1. Fix **Document Chunking** (use Document Intelligence Layout model so tables aren't split).<br>2. Switch Azure AI Search from pure keyword or pure vector to **Hybrid Search + Semantic Ranker**.<br>3. Clean obsolete/noisy documents (**Cleanliness**). |
| **Generative Orchestrator keeps calling `Tool_B` when it should call `Tool_A`.** | Ambiguous or overlapping natural-language **Descriptions** or parameter names between `Tool_A` and `Tool_B`. | Rewrite the `Description` and parameter docstrings of `Tool_A` and `Tool_B` in Copilot Studio / MCP Server to clearly state when to use each tool and when *not* to use it. |
| **Sudden spike in HTTP 429 (`TooManyRequests`) errors and high P99 latency during peak business hours.** | Regional **Tokens-Per-Minute (TPM)** or **Requests-Per-Minute (RPM)** quota exhaustion on the model endpoint. | 1. Implement an **Azure API Management (APIM) AI Gateway** with multi-region load balancing/failover and semantic caching.<br>2. Introduce a **Model Router** to offload simple prompts to an SLM.<br>3. Upgrade critical live workloads to **Provisioned Throughput Units (PTU)**. |
| **High Prompt Token Consumption per turn (rising costs & slower Time-To-First-Token).** | Entire raw conversation history (30+ turns) and 20 huge RAG chunks (1,500 tokens each) are being stuffed into every prompt call. | 1. Summarize older conversation turns (sliding window + summary memory).<br>2. Reduce `top_k` retrieved chunks (e.g., from 20 down to 5 high-precision reranked chunks).<br>3. Fine-tune an SLM to replace massive few-shot system prompts. |

---

## Part 3: Module 08 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 8.1
**Scenario:** Relecloud operates a customer support agent in Microsoft Foundry that uses Azure AI Search for RAG grounding. Continuous evaluation telemetry in the Microsoft Foundry observability dashboard shows that for queries about hardware warranty claims, the **Retrieval Score is consistently high (4.8 / 5.0)**, meaning the correct warranty PDF clauses are being retrieved into the prompt context. However, the **Groundedness Score is low (2.1 / 5.0)** because the agent frequently invents extra warranty terms that are not in the retrieved clauses.

**What should you do to tune the agent?**
- **A.** Rebuild the Azure AI Search vector index from scratch because retrieval is broken.
- **B.** Lower the model temperature toward 0.0, tighten the system prompt to restrict answers strictly to retrieved chunks, and enable Azure AI Content Safety Groundedness Detection.
- **C.** Increase the model temperature to 1.0 to encourage more creative synthesis.
- **D.** Delete the warranty PDFs from Azure Blob Storage.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** A high **Retrieval Score** proves that Azure AI Search is already retrieving the right chunks. A low **Groundedness Score** despite high retrieval means the **generation step** is drifting beyond the retrieved context. Lowering `temperature` (to `0.0–0.1`), enforcing strict grounding constraints in the system prompt, and enabling **Groundedness Detection** directly eliminates ungrounded fabrication.
- **Why A is Incorrect:** Retrieval is already scoring 4.8/5.0; re-indexing will not stop the LLM from extrapolating.
- **Why C & D are Incorrect:** Increasing temperature increases hallucinations, and deleting warranty PDFs removes the source of truth entirely.
</details>

---

### Question 8.2
**Scenario:** Lucerne Publishing has deployed six Microsoft Copilot Studio agents across three departments and two custom Microsoft Foundry microservices. The Chief Information Officer requires a single centralized observability telemetry store where engineers can run Kusto Query Language (KQL) queries to correlate end-to-end latency, custom events, MCP tool failures, and exception stack traces across both the Copilot Studio agents and the Microsoft Foundry microservices.

**What should you recommend?**
- **A.** Configure all Copilot Studio agents and Microsoft Foundry projects to export telemetry to a shared Azure Application Insights (Log Analytics workspace) instance.
- **B.** Rely solely on the individual Copilot Studio in-portal CSV export for each bot.
- **C.** Use Microsoft Viva Insights Copilot Dashboard.
- **D.** Use the SharePoint Admin Center.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Azure Application Insights** (backed by Azure Monitor Log Analytics) natively connects to both **Microsoft Copilot Studio** (via the Application Insights connection string in agent settings) and **Microsoft Foundry**, enabling unified OpenTelemetry distributed tracing and **KQL** querying across the entire multi-agent architecture.
- **Why B is Incorrect:** Manual per-agent CSV exports do not capture Foundry microservice traces or support live KQL correlation and alerting.
- **Why C & D are Incorrect:** Viva Insights measures M365 employee productivity/sentiment, and SharePoint Admin Center manages sites.
</details>

---

### Question 8.3
**Scenario:** Graphic Design Institute uses Generative AI Orchestration in a Microsoft Copilot Studio agent that has two custom connector tools: `GetInvoiceDetails` and `GetBillingSummary`. Telemetry logs show that when users ask for a line-item tax breakdown on a specific invoice, the orchestrator calls `GetBillingSummary` 60% of the time instead of `GetInvoiceDetails`. Upon inspection, both tools have the exact same description: *"Gets billing and invoice information for a customer."*

**What should you do first to resolve the tool selection error?**
- **A.** Rewrite the natural-language `Description` and parameter descriptions of both `GetInvoiceDetails` and `GetBillingSummary` so their purposes, inputs, and outputs are distinct and non-overlapping.
- **B.** Fine-tune a new foundation model in Microsoft Foundry.
- **C.** Switch the agent to Voice Mode.
- **D.** Increase the Azure AI Search partition count.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** In **Generative AI Orchestration**, the LLM orchestrator selects tools based directly on the semantic clarity of each tool's **`Description`** and parameter metadata. Differentiating the descriptions (e.g., specifying that `GetInvoiceDetails` retrieves line-item tax breakdowns for a single `InvoiceID`, whereas `GetBillingSummary` retrieves account-level monthly totals) immediately fixes routing accuracy.
- **Why B, C, and D are Incorrect:** Fine-tuning, Voice Mode, and search partitions do not fix ambiguous tool descriptions in Copilot Studio.
</details>
