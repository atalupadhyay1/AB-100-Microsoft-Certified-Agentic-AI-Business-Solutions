# Domain 2 Practice Quiz & Enterprise Case Studies: Design AI-Powered Business Solutions (25–30%)

This assessment covers all objectives in **Domain 2 (Modules 05–07)**:
- Subdomain 2.1: Design AI and agents for business solutions
- Subdomain 2.2: Design extensibility of AI solutions
- Subdomain 2.3: Orchestrate configuration for prebuilt agents and apps

---

## Part 1: Domain 2 Scenario Questions (With Complete Solutions)

### D2-Q1
**Scenario:** Northwind Electric Cars uses **Dynamics 365 Customer Service**. Support representatives frequently ask the embedded Copilot questions using internal engineering codes such as *"Which open cases involve a **Level-3 Inverter Thermal Fault**?"* In Microsoft Dataverse, that condition corresponds to `incident.nw_faultcategory == 100000003 AND incident.nw_subsystem == 'Inverter'`. What should you configure so Copilot in Dynamics 365 Customer Service interprets this phrase accurately?
- **A.** Configure a Business Term in Dynamics 365 Customer Service mapped to the `incident` table columns and filter values.
- **B.** Configure Azure AI Vision Spatial Analysis.
- **C.** Export the solution as unmanaged and delete the `incident` table.
- **D.** Enable DTMF keypad entry in Voice Mode.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** **Business Terms** in Dynamics 365 Customer Experience and Service map organization-specific terminology and acronyms directly to Dataverse tables, columns, and filter rules.
</details>

---

### D2-Q2
**Scenario:** Blue Yonder Airlines is integrating a **Microsoft Copilot Studio** agent with **Dynamics 365 Contact Center** to handle both inbound telephone voice calls and WhatsApp text messages. When a caller on the voice channel cannot resolve their baggage claim after two attempts, the agent must transfer the call to the **Lost Baggage Human Specialist Queue** and automatically display the customer's SkyMiles Number, detected intent, and an AI summary of the call to the human representative. What should you configure?
- **A.** Configure the Copilot Studio agent on the Contact Center Voice and WhatsApp workstreams, pass `va_` context variables (`SkyMilesNumber`, `DetectedIntent`) on the `Transfer to agent (Escalate)` node to Unified Routing, and enable Copilot Conversation Summary for human representatives.
- **B.** Tell the caller to hang up and send a fax.
- **C.** Use a SharePoint embedded agent with no Contact Center channel.
- **D.** Disable the `Escalate` system topic in Copilot Studio.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** Connecting the Copilot Studio agent to Dynamics 365 Contact Center workstreams, passing context variables to **Unified Routing** on escalation, and enabling **Copilot Conversation Summaries** ensures seamless omnichannel handoff.
</details>

---

### D2-Q3
**Scenario:** Litware, Inc. is building a multi-step **Order Refund Approval** capability inside a Microsoft Copilot Studio agent. Business rules mandate that every refund execution must strictly perform four steps in exact order without skipping any step:
1. Query the SQL ERP database for the original payment transaction ID,
2. Calculate the restocking fee using a deterministic formula,
3. Create an audit record in Microsoft Dataverse, and
4. Send a confirmation receipt via Office 365 Outlook.

**Which Copilot Studio component should you design to guarantee this exact deterministic step sequence?**
- **A.** An Agent Flow invoked as an action by the Copilot Studio agent.
- **B.** A high-temperature (`1.0`) free-form prompt with no structured steps.
- **C.** Public website knowledge search.
- **D.** Azure AI Speech Custom Neural Voice.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** **Agent Flows** in Microsoft Copilot Studio enforce deterministic, repeatable execution sequences for multi-step transactional logic while remaining callable as a tool by the agent's generative orchestrator.
</details>

---

### D2-Q4
**Scenario:** First Up Consultants has built an internal **Model Context Protocol (MCP) Server** that exposes 12 project-staffing tools and 4 resource URIs. They also have two independent specialist agents built by different teams: a **Legal Contract Agent** in **Microsoft Foundry** and an **HR Onboarding Agent** in **Microsoft Copilot Studio**. Which combination of open protocols should you use so that:
1. The HR Onboarding Agent can invoke tools on the MCP Server, and
2. The HR Onboarding Agent can delegate a contract review sub-task to the Legal Contract Agent?
- **A.** Model Context Protocol (MCP) for Agent-to-Tool connection (#1), and Agent2Agent (A2A) protocol for Agent-to-Agent delegation (#2).
- **B.** FTP for #1 and SMTP for #2.
- **C.** Computer Use for both #1 and #2.
- **D.** Direct file upload for both #1 and #2.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** **MCP (Model Context Protocol)** standardizes **Agent-to-Tool / Agent-to-Resource** connectivity, while **A2A (Agent2Agent)** standardizes horizontal **Agent-to-Agent** task delegation across platforms.
</details>

---

### D2-Q5
**Scenario:** An enterprise is extending **Dynamics 365 Finance** and **Dynamics 365 Supply Chain Management** so that when users ask questions in the in-app Copilot sidecar chat, the agent can retrieve answers from both **custom internal accounting SOPs stored in SharePoint Online** AND **open customer dispute cases stored in Dynamics 365 Customer Service (Dataverse)**. Where and how should you configure this?
- **A.** In the linked Power Platform environment, open the **Copilot for finance and operations apps** agent in Microsoft Copilot Studio, add the SharePoint Online site and the Dataverse `Incident (Case)` table as Knowledge Sources with On-Behalf-Of (OBO) user authentication, and publish via a Managed Solution.
- **B.** Edit the Windows Registry on every accountant's laptop.
- **C.** Disable the Power Platform environment link in Lifecycle Services.
- **D.** Use Azure AI Vision Object Detection.

<details><summary><strong>Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Rationale:** Extending the **`Copilot for finance and operations apps`** agent in Copilot Studio within the linked Power Platform environment enables both custom in-app help knowledge sources (SharePoint) and cross-app CRM/ERP Dataverse interoperability.
</details>

---

## Part 2: Enterprise Architecture Case Study 2 — Adventure Works Cycles Global Dealer & Manufacturing Agentic Platform

### Case Study Background
**Adventure Works Cycles** (`adventure-works.com`) manufactures high-end carbon-fiber bicycles and sells through 1,800 global dealers.
- **Current Environment:**
  - Dealer orders and warranty cases run on **Dynamics 365 Sales** and **Dynamics 365 Customer Service**.
  - Manufacturing and procurement run on **Dynamics 365 Supply Chain Management**.
  - Quality engineers use a **Power Apps Canvas App** on factory floor tablets.
  - A third-party customs clearance government web portal (`legacy-customs-gov.example`) has **no API or webhook** and changes its HTML layout every few months.
- **Design Requirements:**
  1. **Factory Floor Tablet Defect & Warranty Triage:** When a quality engineer takes a photo of a damaged bicycle frame and enters inspection notes in the Power Apps Canvas App, the app must classify the defect image and extract structured JSON (`DefectSeverity`, `PartNumber`, `RecommendedAction`) into Dataverse columns.
  2. **Legacy Customs Portal Automation:** An agent must log into the `legacy-customs-gov.example` web portal, dismiss seasonal pop-up notices, look up tariff hold codes, and write the status back to Dataverse.
  3. **Supervisor Exception Review:** Because 4 autonomous agents run overnight processing vendor PO delays and warranty claims, plant supervisors need a single unified stream inside their Power App where they can see completed autonomous actions and approve high-value ($10,000+) warranty replacements.

---

### Case Study Question CS2-1
**Which combination of Power Platform AI Hub (AI Builder) components should you embed in the Power Apps Canvas App for Requirement 1?**
- **A.** An AI Builder Custom Object Detection / Vision model for the frame photo and a Custom Prompt Action configured with **JSON output format** invoked via Power Fx `Predict()`.
- **B.** Azure AI Speech Text-to-Speech and a Fallback topic.
- **C.** Microsoft Viva Insights Copilot Dashboard.
- **D.** Unmanaged solution deletion.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **A** — AI Builder Vision/Object Detection analyzes the physical frame defect image, and a **JSON-formatted Custom Prompt Action** invoked via Power Fx extracts strongly typed fields (`DefectSeverity`, `PartNumber`, `RecommendedAction`) for `Patch()` into Dataverse.
</details>

### Case Study Question CS2-2
**Which capability should you design to automate Requirement 2 (the `legacy-customs-gov.example` portal that has no API and frequently shifts its HTML layout)?**
- **A.** Computer Use in Microsoft Copilot Studio with natural-language task instructions and domain allowlisting.
- **B.** A hardcoded XPath selector script that fails whenever HTML changes.
- **C.** A Microsoft Graph Connector.
- **D.** A SharePoint site agent.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **A** — **Computer Use** in Copilot Studio uses visual screen reasoning to navigate web/desktop UIs that lack APIs and adapts dynamically to layout shifts and pop-up banners.
</details>

### Case Study Question CS2-3
**Which application architecture pattern should you propose for Requirement 3 (allowing plant supervisors to monitor autonomous background agents and approve $10,000+ exceptions)?**
- **A.** Configure an **Agent Feed** (and Code-First Generative Pages) in the Power Apps / Dynamics 365 application surfacing autonomous agent activity and Human-in-the-Loop approval cards.
- **B.** Ask supervisors to read raw Azure firewall syslog text files.
- **C.** Disable all autonomous agents.
- **D.** Remove human approval gates on $10,000+ warranty claims.

<details><summary><strong>Reveal Solution</strong></summary>

- **Correct Answer:** **A** — The **Agent Feed** is purpose-built for human-agent supervision, organizing completed autonomous tasks and pending HITL exception approvals in one actionable feed.
</details>
