# Lab 07: Dynamics 365 Business Terms, Sales Connectors, Contact Center Channels & Finance and Supply Chain Knowledge Interoperability

> **AB-100 Exam Alignment:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Modules Covered:** Module 05 & Module 07  
> **Estimated Time:** 35 minutes  
> **Level:** Intermediate to Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Wide World Importers** operates across both **Dynamics 365 Customer Engagement (CRM)** (`Dynamics 365 Sales`, `Dynamics 365 Customer Service`, `Dynamics 365 Contact Center`) and **Dynamics 365 Finance & Supply Chain Management (ERP / F&O)**.

As the Lead Solution Architect, you must configure four cross-application AI capabilities:
1. **Task 1 — Configure Business Terms & Custom Case Summaries in Dynamics 365 Customer Service:** Teach Copilot what internal terms like *"Platinum Cold-Chain SLA"* and *"Priority Customs Hold"* mean in Dataverse schema terms, and add custom fields (`ContainerTemperatureC`, `CustomsBrokerRef`) to the Copilot Case Summary card.
2. **Task 2 — Configure Custom Connectors for Microsoft 365 Copilot for Sales:** Extend Copilot for Sales in Outlook/Teams with a connector to Wide World Importers' external credit-rating and freight-quote service.
3. **Task 3 — Integrate a Copilot Studio Agent with Dynamics 365 Contact Center Channels (Voice & Digital Chat):** Configure omnichannel workstream routing, Voice Mode (barge-in + DTMF), and context variable handoff (`AuthenticatedAccountId`, `IntentCategory`, `ConversationSummary`) to human queues.
4. **Task 4 — Add Custom SharePoint Knowledge Sources & Interoperability to Dynamics 365 Finance & Supply Chain In-App Help:** Extend the **`Copilot for finance and operations apps`** agent in the linked Power Platform environment so warehouse and finance users can query internal SharePoint SOPs and CRM case statuses directly from the F&O sidecar chat!

---

## 2. Step-by-Step Hands-On Instructions

### Task 1: Configure Business Terms & Case Summary Fields in Dynamics 365 Customer Service
1. Open the **Customer Service Admin Center** (`https://<org>.crm.dynamics.com/main.aspx?pagetype=apps`) -> Navigate to **Agent Experience -> Productivity -> Summaries** (and **Knowledge / Business Terms**):
   - Under **Case summary -> Manage data**, map custom Dataverse columns so Copilot includes them in every generated summary:
     - `wwi_containertemperaturec` (*Container Temperature °C*)
     - `wwi_customsbrokerreference` (*Customs Broker Reference*)
     - `prioritycode` (*Priority*)
   - Under **Business Terms / Glossary Configuration** (in Copilot Studio / Dataverse table metadata):
     - Define term **`Platinum Cold-Chain SLA`** -> Mapped to `incident.prioritycode == 1 AND account.wwi_slatier == 'Platinum-ColdChain'`.
     - Define term **`Priority Customs Hold`** -> Mapped to `incident.wwi_customsholdstatus == 100000002`.

---

### Task 2: Extend Microsoft 365 Copilot for Sales with a Custom Connector
1. Sign in to **Microsoft Copilot Studio** -> Select the environment where **Microsoft 365 Copilot for Sales** is installed.
2. Open **Agents -> Microsoft 365 Copilot for Sales -> Actions -> + Add an action**.
3. Select the certified or custom connector **`WWI Freight & Credit Bureau API`** (`GetAccountCreditAndFreightQuote`):
   - Verify **Authentication** is set to **End user credentials (OAuth 2.0 / Entra ID OBO)** so sellers only see credit limits for accounts permitted by their Dynamics 365 Sales security role.
   - Write a precise **Action Description** so the Copilot for Sales orchestrator invokes this action automatically when preparing a meeting brief or drafting a quote email in Outlook.

---

### Task 3: Configure Dynamics 365 Contact Center Channel Integration & Context Handoff
1. In **Microsoft Copilot Studio**, open your **`WWI Omnichannel Support Agent`**:
   - Navigate to **Channels -> Dynamics 365 Customer Service / Contact Center** and connect the agent to your environment.
   - Enable **Voice capabilities** (Barge-in enabled, DTMF fallback enabled for 10-digit Bill of Lading numbers).
2. In **Customer Service / Contact Center Admin Center -> Channels -> Workstreams**:
   - Open `WWI Voice and Live Chat Workstream` -> **Add AI Agent** -> Select `WWI Omnichannel Support Agent`.
   - Under **Context variables**, define `va_CustomerAccountId`, `va_DetectedIntent`, and `va_SentimentTier` so that when the agent executes a **Transfer to agent (`Escalate`)** action, Unified Routing routes `va_DetectedIntent == 'ColdChainEmergency'` directly to the **24/7 Perishable Freight Escalation Queue** with full AI conversation summary!

---

### Task 4: Add SharePoint Knowledge Sources & CRM Interoperability to Dynamics 365 Finance & Supply Chain In-App Help
1. Confirm in **Power Platform Admin Center (`admin.powerplatform.microsoft.com`)** that the **Dynamics 365 Finance and Supply Chain Management** environment is linked to the Dataverse environment with **Virtual Tables** and **Dual-Write** enabled.
2. Open **Microsoft Copilot Studio** (`copilotstudio.microsoft.com`) in that linked environment and select the **`Copilot for finance and operations apps`** agent.
3. Go to **Knowledge -> + Add knowledge -> SharePoint**:
   - Enter `https://wideworldimporters.sharepoint.com/sites/WarehouseAndFinanceSOPs`.
   - Ensure **Authenticate with Microsoft (OBO)** is active so warehouse clerks and controllers only receive answers from SharePoint SOPs they have permission to read.
4. Go to **Knowledge -> + Add knowledge -> Dataverse** and add the CRM `Incident (Case)` and `Account` tables so a Finance collections coordinator chatting inside **Dynamics 365 Finance** can ask: *"Does this customer have any open cold-chain damage cases in Dynamics 365 Customer Service before I send a collection notice?"*
5. Select **Publish** (and package the extension inside a **Managed Solution** for UAT/Production promotion).

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/d365-business-terms-and-connectors.json`](./solution/d365-business-terms-and-connectors.json) — Complete configuration manifest for Dynamics 365 Business Terms, Case Summary field mappings, Copilot for Sales connector plugin, and Contact Center context variables.
- [`solution/fno-knowledge-interoperability.yaml`](./solution/fno-knowledge-interoperability.yaml) — Complete Copilot Studio extension manifest for **`Copilot for finance and operations apps`** integrating SharePoint SOPs and cross-app CRM/ERP Dataverse tables.
