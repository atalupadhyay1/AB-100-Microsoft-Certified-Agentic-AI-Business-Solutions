# Module 07: Orchestrate Configuration of Prebuilt Agents and Apps

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Official Units Preserved:** All 10 Units (Introduction -> Orchestrate AI in D365 Finance & Supply Chain -> Design AI for D365 Customer Service -> Propose M365 Agents for Business Scenarios -> Configure M365 Copilot for Sales & Service -> Propose Power Platform AI Hub Features -> Interoperability of Finance & Operations Agent Chats -> Adding Knowledge Sources to In-App Help in D365 Finance & Supply Chain -> Module Assessment -> Summary)  
> **Associated Hands-On Labs:** [Lab 04: Power Platform Dataverse & AI Builder](../labs/Lab-04-Power-Platform-Dataverse-AI-Builder-Sentiment-Flow/README.md) & [Lab 07: Dynamics 365 Copilot Customization & ERP/CRM Orchestration](../labs/Lab-07-Dynamics-365-Copilot-Customization-and-ERP-CRM-Orchestration/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Why Orchestrating Prebuilt Apps Is Like Conducting a Symphony Orchestra

Imagine you are hired to lead music at a concert hall. You walk in and discover you already have world-class violinists (**Microsoft 365 Copilot**), cellists (**Dynamics 365 Sales & Customer Service**), brass players (**Dynamics 365 Finance & Supply Chain Management**), and percussionists (**Power Platform AI Hub / AI Builder**).

You don't need to build a violin out of raw wood! Instead, your job as the **Conductor (Solution Architect)** is to:
1. Make sure the violinists (Outlook/Teams) and the cellists (CRM) are reading the **same sheet music** (via **Microsoft 365 Copilot for Sales** and **Microsoft 365 Copilot for Service**).
2. Teach the brass section (**Dynamics 365 Finance & Supply Chain Management** sidecar chat) how to read your company's internal accounting & warehouse SOP binders (via **Copilot Studio extensibility & custom knowledge sources for in-app help**).
3. Plug in the right percussion instruments (**AI Builder prebuilt and custom models in Power Platform AI Hub**) so invoices, receipts, and customer reviews get processed automatically.

Even if you have never administered a Dynamics 365 ERP system before, this module breaks down every single prebuilt app and configuration pattern so you will score 100% on these exam questions!

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Orchestrate AI Features in Dynamics 365 Apps for Finance and Supply Chain

Microsoft Dynamics 365 **Finance**, **Supply Chain Management (SCM)**, and **Project Operations** (collectively called **Finance and Operations [F&O] apps**) run on a unified architecture connected to **Microsoft Dataverse** via the **Power Platform Integration / Dual-Write / Virtual Entity** layer.

#### Key Built-In Copilot & Agentic Capabilities in Dynamics 365 Finance & Supply Chain Management

| Dynamics 365 App | Built-In AI / Agent Capability | What Business Problem It Solves |
| :--- | :--- | :--- |
| **Dynamics 365 Finance** | **Copilot in Collections Coordinator Workspace** | Summarizes customer payment history, credit risk, and overdue invoices; drafts tailored payment reminder emails with one click. |
| **Dynamics 365 Finance** | **Account Reconciliation Agent** | Autonomous agent that monitors subledger-to-general-ledger variances, identifies root causes of discrepancies, and suggests clearing entries to accelerate financial period close. |
| **Dynamics 365 Finance** | **Cash Flow Forecasting & Finance Insights** | Uses predictive AI (Azure ML / AI Builder) to forecast cash inflows/outflows, predict when customers will pay invoices late, and build intelligent budget proposals. |
| **Dynamics 365 Supply Chain Management** | **Supplier Communications Agent** | Autonomous agent that monitors procurement mailboxes, parses vendor emails for PO confirmations/delays, updates purchase orders in D365 SCM, and follows up with unresponsive suppliers. |
| **Dynamics 365 Supply Chain Management** | **Confirmed Purchase Orders with Changes Workspace (Downstream Impact Analysis)** | Uses Copilot to analyze how a vendor's delayed delivery affects downstream production orders, sales orders, and warehouse work, and drafts mitigation notifications to impacted buyers/planners. |
| **Dynamics 365 Supply Chain Management** | **Demand Planning Copilot** | Uses natural language and predictive forecasting models to explain seasonal demand shifts, detect forecast outliers, and compare forecast accuracy across regions. |
| **Dynamics 365 Project Operations** | **Time and Expense Agent + Project Copilot** | Generates project task plans, risk assessments, and status reports; autonomously processes consultant timesheets and expense receipts. |

---

### Unit 3: Orchestrate AI Features in Dynamics 365 Apps for Customer Experience and Service

Across the CRM (**Customer Engagement**) suite—**Dynamics 365 Sales**, **Customer Service**, **Contact Center**, **Field Service**, and **Customer Insights**—know how to orchestrate these prebuilt AI capabilities:

1. **Dynamics 365 Customer Service & Contact Center:**
   - **Copilot Case & Conversation Summaries:** Automatically condenses long multi-turn email threads and chat transcripts into structured Problem / Context / Resolution summaries.
   - **Ask a Question & Draft an Email / Chat Response:** Grounded in internal Dynamics 365 Knowledge Articles and trusted external websites/SharePoint sites.
   - **Customer Intent Agent & Customer Knowledge Management Agent:** Autonomously discovers new support intents from live transcripts and generates draft KB articles from closed cases.
2. **Dynamics 365 Field Service:**
   - **Work Order Summarization & Scheduling Optimization (RSO):** Summarizes asset maintenance history and parts needed for frontline technicians; recommends optimal technician dispatch based on skills, travel time, and SLA priority.
3. **Dynamics 365 Customer Insights (Data & Journeys):**
   - **Copilot Segment & Journey Creation:** Marketers describe a target audience in plain English (*"Customers in Seattle who bought winter skis in the last 2 years and have high churn risk"*) and Copilot builds the query segment and multi-channel marketing journey, complete with AI-generated email copy and **Content Ideas**.

---

### Unit 4: Propose Microsoft 365 Agents for Business Scenarios

When mapping business scenarios to the **Microsoft 365 Agent ecosystem**, use this structured decision guide:

| Business Scenario | Recommended Microsoft 365 Agent Solution |
| :--- | :--- |
| **Scenario 1: Team Collaboration & Live Meeting Productivity** | **Facilitator Agent** in Microsoft Teams (captures live notes, action items, and agenda timekeeping) + **Interpreter Agent** (real-time multilingual speech translation). |
| **Scenario 2: Project Task Breakdown & Execution** | **Project Manager Agent** in Microsoft Planner / Teams (creates plans from documents, assigns tasks, tracks status, and drafts task deliverables). |
| **Scenario 3: Department Knowledge Base inside SharePoint** | **SharePoint Agent** scoped to specific document libraries/folders (zero-code setup, instant OBO permission enforcement). |
| **Scenario 4: Deep Multi-Source Research vs. Quantitative Data Analysis** | **Researcher Agent** (deep reasoning across Work IQ + Web for strategy briefs) vs. **Analyst Agent** (chain-of-thought Python data analysis over Excel/CSV datasets). |
| **Scenario 5: Cross-System HR & IT Employee Helpdesk** | **Employee Self-Service Agent** in M365 Business Chat (prebuilt integration with Workday, ServiceNow, SAP SuccessFactors, and HR SharePoint sites). |

---

### Unit 5: Orchestrate the Configuration of Microsoft 365 Copilot for Sales and Microsoft 365 Copilot for Service

#### Why Do M365 Copilot for Sales and M365 Copilot for Service Exist?
Think about how a salesperson or support escalation manager spends their day:
- They spend **70% of their day inside Microsoft Outlook and Microsoft Teams** (reading customer emails, joining Teams calls, writing proposals in Word),
- Yet all the official customer records live inside a **CRM system** (**Microsoft Dynamics 365** or **Salesforce**)!

Without **M365 Copilot for Sales / Service**, users constantly copy-paste email text into CRM fields and switch browser tabs.

```
+-----------------------------------------------------------------------------------+
|       HOW M365 COPILOT FOR SALES / SERVICE BRIDGES M365 AND CRM SYSTEMS           |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   [ Microsoft 365 Graph (Work IQ) ]         [ CRM Platform (D365 or Salesforce) ] |
|   • Outlook Emails & Calendar               • Accounts, Contacts, Leads           |
|   • Teams Meeting Recordings/Transcripts    • Opportunities, Quotes, Cases        |
|   • Word, Excel, PowerPoint, SharePoint     • Custom CRM Tables & Fields          |
|                     \                                     /                       |
|                      v                                   v                        |
|            +-------------------------------------------------------+              |
|            |    MICROSOFT 365 COPILOT FOR SALES / FOR SERVICE      |              |
|            |  • Sidecar pane in Outlook & Teams                    |              |
|            |  • Enriches M365 Copilot Chat with live CRM context   |              |
|            |  • One-click save email/meeting summary back to CRM   |              |
|            |  • Extensible via Copilot Studio & Power Platform!    |              |
|            +-------------------------------------------------------+              |
+-----------------------------------------------------------------------------------+
```

#### Architect's End-to-End Configuration Checklist for M365 Copilot for Sales / Service:
1. **License & Prerequisite Check:** Assign **Microsoft 365 Copilot** + **Copilot for Sales / Service** licenses (included in unified enterprise Copilot SKUs) and verify CRM user permissions.
2. **Deploy the Integrated App in M365 Admin Center:** Deploy the **Copilot for Sales** (or **Copilot for Service**) add-in for Outlook and app for Microsoft Teams via `admin.microsoft.com`, enabling **Teams Meeting Transcription** so post-meeting action items and BANT (Budget, Authority, Need, Timeline) analysis work automatically.
3. **Configure CRM Forms, Fields & Record Creation Rules:** In the Copilot for Sales/Service administrator settings, customize which **CRM fields (standard or custom)** are visible and editable inside the Outlook sidecar pane, and whether sellers can create new Contacts/Opportunities directly from Outlook.
4. **Extend via Microsoft Copilot Studio:** Both Copilot for Sales and Copilot for Service show up as **extensible agents inside Microsoft Copilot Studio**! You can add custom **Power Platform Connectors**, **Prompt Actions**, or **Knowledge Sources** to enrich the Sales/Service meeting preparation card with data from an external ERP or pricing system.

---

### Unit 6: Propose Microsoft Power Platform AI Features, Including AI Hub (AI Builder)

Inside the **Power Apps / Power Automate Maker Portal**, the **AI Hub (AI Builder)** offers low-code AI capabilities divided into **Prebuilt Models** (zero training needed) and **Custom Models** (bring your own training data or custom prompt):

| AI Hub (AI Builder) Model | Type | When to Propose It on Exam AB-100 |
| :--- | :--- | :--- |
| **Custom Prompt (Prompt Builder)** | Generative AI | Creating reusable GPT-powered prompts (summarization, classification, drafting, JSON data extraction) grounded in **Dataverse tables** for use in Power Automate, Power Apps, and Copilot Studio. |
| **Document Processing (Custom)** | Custom Document AI | Extracting fields and tables from proprietary non-standard forms (e.g., custom manufacturing packing slips or inspection checklists). |
| **Invoice Processing / Receipt Processing / ID Reader** | Prebuilt Document AI | Immediately extracting vendor name, line items, tax, and totals from standard invoices, receipts, or passports/driver's licenses without training a model. |
| **Sentiment Analysis / Category Classification / Entity Extraction / Key Phrase Extraction** | Prebuilt & Custom Language AI | Analyzing customer feedback rows in Dataverse, routing negative emails to a priority queue, or extracting custom product codes from text. |
| **Prediction Model** | Custom Tabular ML | Predicting binary or multi-class historical outcomes directly on Dataverse tables (e.g., *"Will this shipment arrive late? Yes/No"* or *"Likelihood of membership renewal"*). |
| **Object Detection** | Custom Vision AI | Counting retail shelf stock or identifying industrial parts from photos taken in a Power Apps Canvas App. |

---

### Unit 7 & Unit 8: Interoperability of Finance & Operations Agent Chats and Adding Knowledge Sources to In-App Help

Pay special attention to Units 7 and 8—they are **verbatim objectives** on the October 2026 AB-100 study guide!

#### 1. How Copilot in Dynamics 365 Finance & Operations (F&O) Works Under the Hood
When a user opens the **Copilot sidecar chat** inside **Dynamics 365 Finance** or **Dynamics 365 Supply Chain Management**, what is actually running behind that chat pane?
- It is powered by a **Microsoft Copilot Studio agent** named **"Copilot for finance and operations apps"** living inside the linked **Microsoft Dataverse / Power Platform environment**!
- Because it is natively backed by Copilot Studio and connected through the **Power Platform Environment link**, you can extend and interoperate with it just like any Copilot Studio agent.

#### 2. Recommend the Exact Process of Adding Knowledge Sources to In-App Help and Guidance for Dynamics 365 Finance or Supply Chain Management (Unit 8)
Out of the box, when an accountant or warehouse clerk asks the in-app Copilot *"How do I post a vendor invoice journal?"*, Copilot searches public **Microsoft Learn documentation** for Dynamics 365 F&O.
**But what if your company customized its F&O approval workflow and stores its own custom Standard Operating Procedures (SOPs) and training guides in SharePoint Online?**

Here is the **exact 4-step architectural process** to add custom knowledge sources to Dynamics 365 F&O In-App Help:
1. **Verify Environment Linkage & Prerequisites:** Ensure the **Dynamics 365 Finance and Operations environment** is linked to a **Power Platform / Dataverse environment** (via Lifecycle Services [LCS] or Unified Admin Experience in Power Platform Admin Center) and that the **Copilot in Finance and Operations** feature is enabled.
2. **Open the "Copilot for finance and operations apps" Agent in Microsoft Copilot Studio:** Sign into `copilotstudio.microsoft.com`, select the linked Power Platform environment, and open the extensible **Copilot for finance and operations apps** agent (or create a solution extension).
3. **Add the Custom Knowledge Source:** Navigate to the **Knowledge** page in Copilot Studio and add your organization's authoritative source—such as a **SharePoint Online site/document library** containing your custom F&O SOPs, a **Microsoft Graph Connector**, or an **Azure AI Search** index—ensuring **User Authentication (OBO)** is configured so users only retrieve help documents they have permission to view.
4. **Configure Generative Orchestration / Conversational Boosting & Publish via Managed Solution:** Verify that **Generative Answers (Conversational Boosting)** is enabled to search both Microsoft Learn documentation and your newly added SharePoint knowledge source, test the citations in the Copilot Studio test pane, and **Publish** the agent (deploying to Test/Prod via a **Power Platform Managed Solution**).

#### 3. Design Interoperability of Finance & Operations Agent Chats to Use Additional Knowledge Sources and Cross-App Agents (Unit 7)
What if a user chatting inside **Dynamics 365 Finance** needs to ask a question that spans **CRM (Dynamics 365 Sales)**, **external 3PL logistics APIs**, or an **enterprise data lake in Microsoft Fabric**?
- **Extend the F&O Agent Chat in Copilot Studio with:**
  1. **Additional Knowledge Sources:** SharePoint, Dataverse CRM tables (Accounts, Opportunities, Cases), Fabric Data Agents, and Graph Connectors.
  2. **Connector Actions & MCP Servers:** Add Power Platform connectors or MCP tools so the user can query or trigger external systems directly from the F&O chat pane.
  3. **Multi-Agent / Child Agent Federation (A2A):** Connect the F&O Copilot Studio agent to specialist agents (e.g., a Microsoft Foundry Supply Chain Risk Agent or a D365 Customer Service Agent) so queries are seamlessly delegated and answered in one unified chat experience!

---

## Part 3: Module 07 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 7.1
**Scenario:** VanArsdel, Ltd. uses Microsoft Dynamics 365 Supply Chain Management. The company recently documented 150 custom warehouse receiving procedures as Word and PDF files stored in an internal SharePoint Online site. Warehouse clerks using the in-app Copilot chat pane inside Dynamics 365 Supply Chain Management report that Copilot only answers using generic Microsoft Learn documentation and does not know VanArsdel, Ltd.'s custom receiving procedures. You need to recommend the supported process to include the SharePoint site in the Dynamics 365 Supply Chain Management in-app help experience while respecting SharePoint permissions.

**What should you recommend?**
- **A.** Open the linked Power Platform environment in Microsoft Copilot Studio, add the SharePoint Online site as a knowledge source to the Copilot for finance and operations apps agent with user authentication, and publish the update.
- **B.** Modify the C++ kernel source code of Dynamics 365 Supply Chain Management.
- **C.** Ask every warehouse clerk to copy and paste the 150 PDF files into the chat window every morning.
- **D.** Deploy Azure AI Vision Spatial Analysis on the warehouse cameras.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** In-app help and guidance in Dynamics 365 Finance and Supply Chain Management is powered by the **Copilot for finance and operations apps** agent in **Microsoft Copilot Studio** within the linked Power Platform environment. Adding the SharePoint site as a Knowledge Source in Copilot Studio extends in-app help with company-specific SOPs while honoring On-Behalf-Of (OBO) SharePoint permissions.
- **Why B, C, and D are Incorrect:** The F&O kernel cannot be modified, manual daily pasting is unscalable and exceeds prompt limits, and Vision Spatial Analysis is unrelated to in-app text documentation help.
</details>

---

### Question 7.2
**Scenario:** Account executives at A. Datum Corporation spend most of their workday in Microsoft Outlook and Microsoft Teams, while their customer opportunities and quotes are stored in Salesforce CRM. The executives want an AI assistant inside Outlook and Teams that automatically summarizes customer email threads, prepares pre-meeting briefs combining Microsoft Graph emails with live Salesforce opportunity data, and updates Salesforce opportunity stages directly from the Teams/Outlook sidecar pane.

**What should you recommend?**
- **A.** Deploy and configure Microsoft 365 Copilot for Sales connected to Salesforce CRM.
- **B.** Deploy the Account Reconciliation Agent in Dynamics 365 Finance.
- **C.** Migrate all emails out of Exchange Online into a local CSV file.
- **D.** Build a custom vision model in AI Hub.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Microsoft 365 Copilot for Sales** connects natively to both **Microsoft Dynamics 365 Sales** and **Salesforce CRM**, bringing live CRM context, email summarization, meeting preparation briefs, and one-click CRM record updates directly into Microsoft Outlook and Microsoft Teams.
- **Why B, C, and D are Incorrect:** Account Reconciliation is for D365 Finance ledgers; exporting emails to CSV breaks live collaboration; Vision models are for image processing.
</details>

---

### Question 7.3
**Scenario:** Fourth Coffee receives 5,000 standard supplier invoices per week as PDF attachments in a shared mailbox. All invoices follow standard commercial invoice layouts (Vendor Name, Invoice Number, Invoice Date, Line Items, Tax, Total Amount). A Power Platform maker wants to extract these fields inside a Power Automate cloud flow and write them to Microsoft Dataverse with zero time spent labeling sample documents or training a custom model.

**Which AI Hub (AI Builder) capability should you propose?**
- **A.** Prebuilt Invoice Processing model in AI Builder.
- **B.** Custom Object Detection model in AI Builder.
- **C.** Prediction model in AI Builder.
- **D.** Azure AI Speech Custom Neural Voice.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** AI Builder's **prebuilt Invoice Processing model** is ready out of the box to extract standard header fields (vendor, date, invoice number, totals) and line-item tables from standard invoices without labeling or training custom documents. (If the documents were proprietary non-standard forms, you would choose Custom Document Processing instead.)
- **Why B, C, and D are Incorrect:** Object Detection is for identifying physical objects in images; Prediction models forecast outcomes on Dataverse tables; Speech synthesizes voice audio.
</details>
