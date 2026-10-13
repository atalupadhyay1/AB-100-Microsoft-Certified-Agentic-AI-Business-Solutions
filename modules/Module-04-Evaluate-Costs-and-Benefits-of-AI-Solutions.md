# Module 04: Evaluate Costs and Benefits of AI Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 1 — Plan AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** All 7 Units (Introduction -> Evaluate ROI Criteria & TCO -> Create ROI Analysis -> Build, Buy, or Extend Analysis -> Implement a Model Router -> Module Assessment -> Summary)  
> **Associated Hands-On Lab:** [Lab 01: Enterprise AI Readiness, Grounding Audit & ROI/Model Router Simulator](../labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### The "Sticker Price vs. Iceberg Cost" Trap

Imagine buying a luxury sports car for $80,000. If you tell your spouse *"This car only costs $80,000!"*, you are forgetting premium insurance, specialized tires, high-octane fuel, garage rental, and annual maintenance. Over 3 years, the **Total Cost of Ownership (TCO)** is actually $135,000.

Now imagine the reverse in enterprise AI:
A team says, *"Building our own agent in Python using open-source code is FREE because we don't have to buy a $30/user/month license!"*
Then six months later, the CFO gets a bill for:
- $18,000/month in unoptimized frontier LLM tokens,
- $6,000/month in vector database hosting,
- 1,200 hours of senior AI engineer salaries ($180,000) building custom connectors and security patches that Microsoft Copilot Studio already included out of the box!

As an **AB-100 Solution Architect**, you must speak the language of the **CFO (Chief Financial Officer)** just as fluently as you speak the language of the **CTO**. In Module 04, you will learn:
1. How to calculate true **Total Cost of Ownership (TCO)** and **Return on Investment (ROI)** for any AI initiative.
2. How Microsoft licenses and meters **M365 Copilot**, **Copilot Studio**, and **Microsoft Foundry** (Pay-As-You-Go vs. Provisioned Throughput Units [PTU]).
3. How to evaluate **Build vs. Buy vs. Extend** economically.
4. How to cut inference costs by **50%–80%** without sacrificing quality by implementing a **Model Router**.

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Evaluate ROI Criteria for AI-Powered Solutions, Including Total Cost of Ownership (TCO)

#### 1. The Complete TCO Equation for Agentic AI
When an exam question asks which costs must be included in a **Total Cost of Ownership (TCO)** analysis for an AI solution, remember that TCO includes **both CapEx/One-Time Implementation Costs AND OpEx/Recurring Run Costs**:

```
+-----------------------------------------------------------------------------------+
|                TOTAL COST OF OWNERSHIP (TCO) = CAPEX + OPEX                       |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  A. ONE-TIME / UPFRONT IMPLEMENTATION COSTS (Design & Build)                      |
|     1. Data Readiness & Remediation (cleaning SharePoint, building ETL pipelines) |
|     2. Architecture, Pro-Code / Low-Code Development & Integration engineering    |
|     3. Initial Model Fine-Tuning / Custom Model Training compute                  |
|     4. Security Review, AI Red Teaming & Compliance Attestation                   |
|     5. Change Management, Champion Onboarding & User Prompt Training              |
|                                                                                   |
|  B. RECURRING OPERATIONAL COSTS (Run, Govern & Maintain)                          |
|     1. Licensing & Consumption:                                                   |
|        - Per-user SaaS licenses (e.g., M365 Copilot $30/user/mo)                  |
|        - Copilot Studio Message Packs / Pay-As-You-Go Copilot Credits             |
|        - Microsoft Foundry Input/Output Token consumption or PTU reservations     |
|     2. Data & Search Infrastructure:                                              |
|        - Azure AI Search index tiers, Dataverse storage capacity, Fabric CU       |
|     3. Observability & Security:                                                  |
|        - Application Insights log ingestion, Azure AI Content Safety guardrails   |
|     4. Ongoing Operations (AIOps / MLOps):                                        |
|        - Continuous evaluation runs, prompt tuning, model version migration,      |
|          and human-in-the-loop exception review labor!                            |
+-----------------------------------------------------------------------------------+
```

#### 2. Quantifying AI Benefits: Hard (Direct) vs. Soft (Indirect) Benefits
A credible business case separates **Hard Financial Savings** from **Strategic / Experience Gains**:
- **Direct / Hard Quantifiable Benefits:**
  - **Labor Time Saved / Deflection:** `(Tickets Deflected per Month) x (Cost per Human-Handled Ticket)` or `(Hours Saved per Employee per Week) x (Loaded Hourly Wage) x (% Redeployed to Productive Work)`.
  - **Error & Penalty Reduction:** Lower SLA breach fines, fewer duplicate vendor payments, reduced compliance audit penalties.
  - **Revenue Acceleration:** Higher lead-to-opportunity conversion rate via **Sales Qualification Agent**, faster quote turnaround, higher average order value.
- **Indirect / Strategic Benefits:**
  - **Customer Satisfaction (CSAT / NPS):** Faster 24/7 response times (<5 seconds vs. 4-hour email queue).
  - **Employee Retention & Sentiment:** Less burnout among contact center reps and analysts (measured via **Microsoft Viva Insights**).

---

### Unit 3: Create an ROI Analysis for a Proposed AI Solution for a Business Process

#### The 4 Essential Formulas Every AB-100 Architect Must Know

1. **Annual Net Benefit:**
   $$\text{Annual Net Benefit} = \text{Total Annual Quantified Benefits} - \text{Annual Recurring OpEx}$$

2. **Total Cost of Ownership (over $N$ years):**
   $$\text{TCO}_N = \text{Upfront Implementation Cost} + \sum_{t=1}^{N} \text{Annual OpEx}_t$$

3. **Return on Investment (ROI %):**
   $$\text{ROI (\%)} = \left( \frac{\text{Total Benefits}_N - \text{TCO}_N}{\text{TCO}_N} \right) \times 100$$

4. **Payback Period (Break-Even Time in Months):**
   $$\text{Payback Period (Months)} = \frac{\text{Upfront Implementation Cost}}{\text{Monthly Net Benefit}}$$

#### Worked Enterprise Example (Walk Through This Step-by-Step!)
**Scenario:** Tailspin Toys receives **50,000 customer support inquiries per month**.
- Currently, human agents handle all inquiries at an average cost of **$8.00 per ticket** ($400,000/month = **$4,800,000/year**).
- You propose a **Microsoft Copilot Studio Autonomous & Conversational Agent** integrated with Dynamics 365 Customer Service:
  - **Upfront Build + Data Cleaning + Training Cost:** **$120,000**
  - **Expected Autonomous Deflection Rate:** **40%** of tickets (20,000 tickets/month resolved autonomously) + **15% faster handle time** on the remaining 30,000 human tickets.
  - **Gross Monthly Labor Savings:**
    - Deflected tickets: $20,000 \times \$8.00 = \$160,000/\text{month}$
    - Assisted tickets time savings: $30,000 \times \$8.00 \times 15\% = \$36,000/\text{month}$
    - **Total Gross Benefit:** $\$196,000/\text{month} = \mathbf{\$2,352,000/\text{year}}$.
  - **Recurring Monthly AI OpEx (Copilot Studio messages + Azure AI Search + App Insights + CoE maintenance):** **$26,000/month** ($312,000/year).
- **Let's Calculate the Architect Metrics (Year 1):**
  - **Year 1 TCO:** $\$120,000\text{ (Upfront)} + \$312,000\text{ (Year 1 OpEx)} = \mathbf{\$432,000}$
  - **Monthly Net Benefit:** $\$196,000 - \$26,000 = \mathbf{\$170,000/\text{month}}$
  - **Payback Period:** $\$120,000 / \$170,000 = \mathbf{0.71\text{ months (\~21 days!)}}$
  - **Year 1 ROI (%):** $\frac{\$2,352,000 - \$432,000}{\$432,000} \times 100 = \mathbf{444.4\%}$

#### Understanding Microsoft AI Licensing & Consumption Economics
To estimate OpEx accurately on the exam, know the three consumption models:
1. **Per-User Monthly Subscription (Predictable Fixed Cost):**
   - Example: **Microsoft 365 Copilot** ($30/user/month). Includes unlimited daily user prompts in Word, Excel, PowerPoint, Outlook, Teams, M365 Copilot Chat, and **included usage of Declarative Agents and standard Copilot Studio agents inside M365** for licensed users!
2. **Consumption / Message / Credit Metering (Copilot Studio):**
   - For external customers (web chat) or employees *without* an M365 Copilot license, **Copilot Studio** bills by **Copilot Credits / Messages** (either via prepaid monthly capacity packs or Pay-As-You-Go meter linked to an Azure subscription).
   - Different actions consume different credit weights (e.g., classic static answers cost less than generative answers, autonomous triggers, and Agent Flow actions).
3. **Token Consumption vs. Provisioned Throughput in Microsoft Foundry:**
   - **Standard (Pay-As-You-Go per 1M Input/Output Tokens):** Best for variable traffic, PoCs, pilots, and spiky workloads. You pay strictly for tokens processed.
   - **Provisioned Throughput Units (PTU):** Reserved model processing capacity billed hourly/monthly with a commitment discount. **Choose PTU when:** you have **high, steady, predictable volume** and require **guaranteed latency and guaranteed throughput (no noisy-neighbor 429 throttling)** for mission-critical workloads (like a live Contact Center voice agent).
   - **Batch API (50% Discount):** Asynchronous processing with a 24-hour completion target. **Choose Batch API when:** running non-urgent nightly jobs (e.g., summarizing 500,000 archived legal contracts or nightly warehouse review tagging) to cut token costs in half!

---

### Unit 4: Analyze Whether to Build, Buy, or Extend AI Components for Business Solutions

Use this **Architect's Economic & Technical Trade-Off Matrix** whenever an exam scenario asks you to justify **Buy (Adopt) vs. Extend vs. Build**:

| Evaluation Criterion | 1. BUY (Adopt Prebuilt SaaS Agent) | 2. EXTEND (Declarative Agent / Copilot Studio) | 3. BUILD (Custom Pro-Code in Microsoft Foundry) |
| :--- | :--- | :--- | :--- |
| **Time to Market** | **Days to Weeks** (Fastest) | **Weeks (2–6 weeks)** | **Months (2–6+ months)** |
| **Upfront CapEx Cost** | **Lowest** (Configuration & training only) | **Low to Medium** | **Highest** (Requires specialized AI engineers, custom UI, custom RAG & DevOps) |
| **Customization & Model Control** | Low (Microsoft chooses the model and system prompt) | Medium-High (Custom topics, instructions, MCP tools, connectors, Agent Flows) | **Maximum** (Any model from Model Catalog, fine-tuning, custom chunking, custom code) |
| **Maintenance & Upgrade Burden** | **Microsoft-Managed** (Zero code debt) | **Shared** (Microsoft manages platform; customer manages topics/connectors) | **Customer-Managed** (Customer owns model upgrades, SDK patches, scaling, guardrails) |
| **When to Select on Exam AB-100** | Commodity horizontal or CRM/ERP processes (e.g., Meeting facilitation, D365 Sales lead qualification, D365 Supplier emails). | Connecting M365/D365 to internal APIs, SharePoint libraries, or custom multi-step business workflows. | Differentiating core IP, strict latency/cost requirements needing SLMs or Model Routers, or custom customer-facing apps. |

---

### Unit 5: Implement a Model Router to Intelligently Route Requests to the Most Suitable Model

#### Why Single-Model Architecture Wastes Money
In a typical enterprise agent, **70% to 80% of incoming requests are simple**:
- *"What are your store hours?"*
- *"Classify this email as Billing, Technical, or Sales."*
- *"Extract the invoice number and date from this receipt."*

Only **20% to 30% of requests are genuinely complex**:
- *"Compare these three 40-page supplier contracts against our EU liability guidelines and draft a redline negotiation strategy."*

If you send **100% of traffic to a frontier reasoning model** (like GPT-5 or o3), you pay **15x–30x more per token** and suffer **3x–5x higher latency** on the 80% of simple queries!

#### How a Model Router Works in Microsoft Foundry

```
                                   +-----------------------------------+
                                   |  Tier 1: Fast / Cheap SLM         |
                                   |  (e.g., Phi-4-mini / GPT-4o-mini) |
                                   |  • Cost: ~$0.15 / 1M tokens       |
                                   |  • Latency: ~200 ms               |
                                   +-----------------------------------+
                                     ^
                                     | (Simple Intent: FAQ, Extraction,
                                     |  Classification — ~75% of traffic)
                                     |
[ Incoming User / Agent Prompt ] ---> [ MICROSOFT FOUNDRY MODEL ROUTER ]
                                     |  (Lightweight Classifier assesses
                                     |   task complexity, token length,
                                     |   & reasoning depth required)
                                     |
                                     | (Complex Intent: Multi-Step Planning,
                                     |  Deep Reasoning, Ambiguous Synthesis
                                     |  — ~25% of traffic)
                                     v
                                   +-----------------------------------+
                                   |  Tier 2: Frontier Reasoning Model |
                                   |  (e.g., GPT-5 / GPT-4o / o3-mini) |
                                   |  • Cost: ~$5.00–$15.00 / 1M tok   |
                                   |  • Latency: ~1.5–4.0 sec          |
                                   +-----------------------------------+
```

#### Two Architectural Ways to Implement Model Routing:
1. **Built-In Model Router in Microsoft Foundry:**
   - Microsoft Foundry provides a deployable **Model Router** endpoint that automatically evaluates each incoming chat completion prompt in real time and routes it to the optimal underlying sub-model (balancing quality, latency, and cost) behind a **single unified endpoint URL and API key**.
2. **Custom Orchestrator / Gateway Routing (Azure API Management + Classifier):**
   - For domain-specific routing rules (e.g., *"Route all German legal queries to our fine-tuned Mistral model in Germany West Central, route simple English FAQs to Phi-4, and route complex financial reconciliations to o3-mini"*), an architect places an intent/complexity classifier or **Azure API Management (APIM) AI Gateway policy** in front of the model pool, with automatic **fallback routing** if a regional endpoint hits HTTP 429 throttling!

> **Hands-On Connection:** In **[Lab 01](../labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/README.md)**, you will run a Python simulation of both an enterprise ROI/TCO calculator and a dynamic **Model Router** to see the exact cost and latency savings in action!

---

## Part 3: Module 04 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 4.1
**Scenario:** Humongous Insurance is processing 2 million customer claim enquiries per month through a custom agent hosted in Microsoft Foundry. An audit of telemetry logs shows that 80% of enquiries are simple status checks or address updates, while 20% require complex multi-document policy coverage reasoning. Currently, all 2 million enquiries are sent to a single frontier reasoning model deployment, causing high monthly token bills and slow 4-second response times on simple status checks. You need to reduce token costs by at least 60% and reduce latency on simple requests without degrading accuracy on complex policy coverage questions.

**What should you recommend?**
- **A.** Replace the frontier model entirely with a basic rule-based regex script for all 2 million enquiries.
- **B.** Implement a Model Router in Microsoft Foundry to dynamically route simple requests to a compact model (such as GPT-4o-mini or Phi-4) and complex reasoning requests to the frontier model.
- **C.** Increase the `temperature` parameter of the frontier model from 0.0 to 1.0.
- **D.** Switch the frontier model from Data Zone Standard to Global Standard without changing the model.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** A **Model Router** inspects incoming prompt complexity and routes the 80% of simple tasks to a fast, low-cost Small/Mini model while reserving the expensive frontier model for the 20% of complex multi-document policy reasoning requests—dramatically cutting both cost and latency while preserving quality.
- **Why A is Incorrect:** A regex script cannot handle the 20% of complex multi-document policy coverage reasoning enquiries.
- **Why C is Incorrect:** Increasing temperature makes outputs more random/creative; it does not reduce token cost or latency.
- **Why D is Incorrect:** Changing deployment geography/SKU does not avoid running an oversized frontier model on 80% trivial status checks.
</details>

---

### Question 4.2
**Scenario:** Blue Yonder Airlines is deploying a real-time voice agent in Dynamics 365 Contact Center backed by an Azure OpenAI model in Microsoft Foundry. During peak storm disruptions, call volume spikes simultaneously and every voice turn must begin streaming a response within 800 milliseconds without encountering HTTP 429 rate-limit throttling. In addition, the airline has a separate nightly job that summarizes 100,000 completed call transcripts for next-day executive analytics.

**Which deployment pricing/capacity models should you recommend for the two workloads?**
- **A.** Batch API for the live voice agent; Provisioned Throughput Units (PTU) for the nightly transcript job.
- **B.** Provisioned Throughput Units (PTU) for the live voice agent; Batch API (or Standard Pay-As-You-Go) for the nightly transcript job.
- **C.** Free Trial tier for both workloads.
- **D.** Copilot Studio direct file upload for both workloads.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** Live Contact Center voice agents require deterministic sub-second latency and guaranteed capacity without HTTP 429 throttling—the exact use case for **Provisioned Throughput Units (PTU)**. The non-urgent nightly transcript summarization job can tolerate asynchronous completion (up to 24 hours), making the **Batch API** ideal at a 50% token cost discount.
- **Why A is Incorrect:** It reverses the two models—Batch API has up to 24-hour turnaround and cannot power a live voice call!
- **Why C & D are Incorrect:** Free tiers have strict throttling limits unsuitable for production, and file uploads are not an inference capacity model.
</details>

---

### Question 4.3
**Scenario:** First Up Consultants is preparing a 3-year Total Cost of Ownership (TCO) and ROI business case for an enterprise multi-agent solution. The project manager only included the monthly Microsoft Copilot Studio message pack fees in the cost spreadsheet. As the Lead Solution Architect, which omitted cost categories should you add to ensure an accurate TCO?

- **A.** Upfront data remediation/cleaning costs, integration development labor, Azure AI Search/Dataverse storage costs, Application Insights telemetry ingestion, and ongoing evaluation/maintenance operations.
- **B.** Only the cost of replacing all employee laptops with gaming PCs.
- **C.** Only the salary of the Chief Executive Officer.
- **D.** None; licensing fees are the only cost in a TCO analysis.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** A complete **TCO analysis** must account for both **upfront implementation CapEx** (data preparation, engineering, security review, user training) and **full recurring OpEx** (licensing/consumption, search/storage infrastructure, monitoring/telemetry, and ongoing AIOps/evaluation maintenance).
- **Why B, C, and D are Incorrect:** Cloud-hosted Copilot Studio agents do not require gaming PCs, CEO salary is not an incremental project cost, and ignoring implementation, data, and operations costs severely understates TCO.
</details>
