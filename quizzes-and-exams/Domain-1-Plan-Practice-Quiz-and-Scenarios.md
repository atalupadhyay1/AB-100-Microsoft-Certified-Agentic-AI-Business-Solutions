# Domain 1 Practice Quiz & Enterprise Case Studies: Plan AI-Powered Business Solutions (25–30%)

This assessment covers all objectives in **Domain 1 (Modules 01–04)**:
- Subdomain 1.1: Analyze requirements for AI-powered business solutions
- Subdomain 1.2: Design overall AI strategy for business solutions
- Subdomain 1.3: Evaluate the costs and benefits of an AI-powered business solution

---

## Part 1: Domain 1 Scenario Questions (With Complete Solutions)

### D1-Q1
**Scenario:** Munson's Pickles and Preserves Farm wants to deploy an AI solution to help regional sales managers analyze 5 years of distributor sales history stored in a Microsoft Fabric Lakehouse, identify seasonal demand anomalies, and recommend promotional discounts for underperforming territories. How should you classify the primary functional roles of this agentic workload?
- **A.** Data analytics and decision-making
- **B.** Legacy GUI screen scraping only
- **C.** Real-time telephony voice synthesis only
- **D.** Hardware driver compilation

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** Exploring 5 years of lakehouse history to detect seasonal anomalies is **Data Analytics**, and evaluating discount options to recommend territory promotions is **Decision-Making**.
</details>

---

### D1-Q2
**Scenario:** Southridge Video is reviewing its SharePoint Online libraries before connecting them as grounding sources for a new Microsoft Copilot Studio employee agent. You discover that when an employee searches for *"Parental Leave Policy"*, the search returns 400 unrelated HR orientation slide decks from 2016 through 2025, burying the actual 2-page parental leave policy at result #38. Which grounding data quality dimension is primarily impacted, and what should you recommend?
- **A.** Relevance; scope the agent's knowledge source to the specific authoritative folder/library, archive obsolete slide decks (**Cleanliness**), and enrich SharePoint document metadata columns.
- **B.** Availability; open firewall port 3389.
- **C.** Timeliness; replace SharePoint with a real-time stock ticker API.
- **D.** Fluency; switch the agent language to Latin.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** Returning hundreds of unrelated documents that dilute the context window is a **Relevance** (and **Cleanliness**) failure. Tightly scoping the SharePoint library path, archiving outdated decks, and adding metadata tags directly fixes retrieval precision.
</details>

---

### D1-Q3
**Scenario:** Liberty's Delightful Bakery & Cafe has 800 corporate employees licensed for Microsoft 365 Copilot and 4,500 seasonal frontline bakery staff who do **not** have Microsoft 365 Copilot licenses. The company wants to build an internal shift-swapping and recipe lookup agent accessible to **all 5,300 employees** via Microsoft Teams and a mobile web portal, with custom multi-step dialog flows and autonomous shift-coverage triggers. Which platform strategy should you recommend?
- **A.** Build a standalone custom agent in Microsoft Copilot Studio (using Copilot Studio capacity packs / Pay-As-You-Go meter for the 4,500 unlicensed frontline staff and included M365 Copilot rights for the 800 licensed corporate users).
- **B.** Build only a M365 Copilot Declarative Agent (which requires every user to hold an M365 Copilot license and cannot run autonomous triggers).
- **C.** Train a foundational LLM from scratch on 10,000 GPUs.
- **D.** Use Microsoft Security Copilot.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** A **Declarative Agent** inside M365 Copilot requires users to have M365 Copilot licenses and does not support standalone web portal publishing or autonomous triggers. A **Microsoft Copilot Studio standalone agent** can be published to Teams and custom web portals for all 5,300 users (using metered Copilot Credits for the 4,500 non-M365-Copilot users and zero-extra-cost included usage for the 800 M365 Copilot users).
</details>

---

### D1-Q4
**Scenario:** Nod Publishers wants to classify incoming book manuscripts into 85 proprietary publisher sub-genres and output a strict internal MARC-XML metadata header. The classification runs 500,000 times per day, must complete in under 200 ms, and must cost less than $0.20 per 1,000 requests. Standard zero-shot prompts on a general model fail to use Nod Publishers' proprietary 85 sub-genre taxonomy unless a 6,000-token instruction manual is included in every prompt (which makes it too slow and expensive). What should you recommend?
- **A.** Fine-tune a Small Language Model (SLM) such as Microsoft Phi-4 (or GPT-4o-mini) in Microsoft Foundry on labeled examples of Nod Publishers' 85 sub-genres and MARC-XML outputs.
- **B.** Send all 500,000 daily requests with a 6,000-token prompt to the largest frontier reasoning model (`o3`).
- **C.** Use Computer Use in Copilot Studio.
- **D.** Use a SharePoint embedded agent.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** This is the textbook exam scenario for **Fine-Tuning a Small Language Model (SLM)**: high volume (500k/day), strict latency (<200 ms), strict proprietary taxonomy/output format (MARC-XML), and eliminating a massive 6,000-token few-shot system prompt on every call!
</details>

---

### D1-Q5
**Scenario:** During a Cloud Adoption Framework (CAF) for AI workshop at School of Fine Art, three departments independently propose building their own separate ServiceNow ticket-creation connectors and their own separate GDPR PII-redaction prompts. Which organizational governance body should you establish to centralize reusable AI assets, prompt libraries, MCP servers, and intake prioritization?
- **A.** Microsoft AI Center of Excellence (AI CoE)
- **B.** Facilities Maintenance Desk
- **C.** External Public Relations Agency
- **D.** Print Server Queue

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** The **Microsoft AI Center of Excellence (AI CoE)** prevents duplicate departmental silos by maintaining a shared catalog of vetted connectors, MCP servers, reusable prompt libraries, and governance standards.
</details>

---

## Part 2: Enterprise Architecture Case Study 1 — Woodgrove Bank Multi-Agent Wealth & Retail Transformation

### Case Study Background
**Woodgrove Bank** (`woodgrovebank.com`) is a multinational retail and wealth management bank with 12,000 employees across **New York (US)**, **Frankfurt (Germany)**, and **Singapore**.
- **Current Environment:**
  - All 3,000 wealth advisors and corporate staff hold **Microsoft 365 Copilot** licenses.
  - Retail banking customer support uses **Dynamics 365 Customer Service** and **Dynamics 365 Contact Center**.
  - Commercial loan accounting uses **Dynamics 365 Finance**.
  - Enterprise analytical data is consolidated in **Microsoft Fabric OneLake**.
- **Business Requirements:**
  1. **Wealth Advisor Meeting Prep:** Wealth advisors working in Outlook and Teams need an assistant that combines email/calendar context with client portfolio data in Dynamics 365 Sales and generates compliant pre-meeting briefs.
  2. **German Retail Banking Compliance:** Due to strict German financial regulations, all prompts, completions, and grounding data for Frankfurt retail banking customers must be stored and processed strictly within the **European Union** boundary.
  3. **Cost Optimization on 3 Million Monthly Retail Chat Queries:** 75% of customer chat queries are simple routing/FAQ checks, while 25% require complex multi-product mortgage comparison reasoning. Leadership requires cutting projected LLM token spend by at least 60%.

---

### Case Study Question CS1-1
**Which solution should you recommend for Requirement 1 (Wealth Advisor Meeting Prep in Outlook and Teams)?**
- **A.** Configure and extend Microsoft 365 Copilot for Sales connected to Dynamics 365 Sales.
- **B.** Build a custom C++ desktop app from scratch.
- **C.** Deploy the Supplier Communications Agent in Dynamics 365 Supply Chain Management.
- **D.** Use Computer Use to read Outlook emails.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **A** — **Microsoft 365 Copilot for Sales** natively bridges Outlook/Teams (Microsoft Graph) with Dynamics 365 Sales records to generate pre-meeting preparation briefs.
</details>

### Case Study Question CS1-2
**Which model deployment configuration in Microsoft Foundry should you mandate for Requirement 2 (German Retail Banking Compliance)?**
- **A.** `Global Standard` deployment in `East US`.
- **B.** `Data Zone Standard (EU)` or `Germany West Central Regional` deployment in Microsoft Foundry, paired with an EU-hosted Power Platform / Dataverse environment with cross-geo AI data movement disabled.
- **C.** Public anonymous Bing Web Search grounding enabled on all customer PII prompts.
- **D.** Direct file upload to a US-hosted default environment.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **B** — Selecting an **EU Data Zone Standard** or **Germany West Central Regional** deployment guarantees that both data at rest and model inference processing remain inside the EU boundary.
</details>

### Case Study Question CS1-3
**What should you implement to satisfy Requirement 3 (Cost Optimization across the 3 million monthly retail queries)?**
- **A.** Deploy a Model Router in Microsoft Foundry that routes the 75% simple queries to a compact SLM (such as Phi-4 or GPT-4o-mini) and the 25% complex queries to a frontier reasoning model.
- **B.** Route 100% of queries to the most expensive reasoning model and disable caching.
- **C.** Block 75% of customers from logging in.
- **D.** Replace all models with Azure AI Speech.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **A** — A **Model Router** dynamically matches prompt complexity to model tier, achieving 60%–75% token cost reduction without sacrificing reasoning quality on complex mortgage comparisons.
</details>
