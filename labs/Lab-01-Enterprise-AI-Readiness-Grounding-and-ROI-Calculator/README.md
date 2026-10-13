# Lab 01: Enterprise AI Readiness, 5-Dimension Grounding Audit & ROI / Model Router Simulator

> **AB-100 Exam Alignment:** Domain 1 — Plan AI-Powered Business Solutions (25–30%)  
> **Modules Covered:** Module 01, Module 02, Module 03, Module 04  
> **Estimated Time:** 30 minutes  
> **Level:** Beginner to Intermediate (Builds into Architect-Grade Financial & Data Modeling)

---

## 1. Lab Scenario & Business Objective (Humanized Context)

You have just been hired as the **Lead Agentic AI Business Solutions Architect** for **Northwind Traders**, a global wholesale distribution enterprise.
Two urgent problems are sitting on your desk on Day 1:

1. **The Grounding Data Quality Crisis:** The Warehouse & Returns team wants to connect their SharePoint document library and product inventory feed to a new Microsoft Copilot Studio agent. However, when they tested a quick prototype, the agent gave contradictory refund rules and quoted inventory numbers from yesterday! You need to run a structured **5-Dimension Grounding Data Quality Audit** (**Accuracy, Relevance, Timeliness, Cleanliness, Availability**) to diagnose every defect and output an actionable remediation plan.
2. **The CFO's ROI & Model Router Challenge:** Northwind's CFO is skeptical about spending $145,000 upfront to build a multi-agent customer operations solution handling **120,000 enquiries per month**. Furthermore, a developer wants to send all 120,000 enquiries to a high-cost frontier reasoning model (`GPT-5 / o3`), which would cost a fortune. You need to build a **3-Year TCO & ROI Calculator** and prove how adding a **Microsoft Foundry Model Router** (routing simple tasks to `Phi-4 / GPT-4o-mini` and complex tasks to `GPT-5`) slashes monthly inference costs while accelerating the Payback Period.

---

## 2. Step-by-Step Hands-On Tasks

### Task 1: Audit Enterprise Data Across the 5 Grounding Dimensions
In this task, you evaluate a candidate enterprise knowledge repository against the official AB-100 grounding rubric:
1. **Cleanliness Check:** Detect duplicate or unarchived draft files (e.g., `Return_Policy_2021_DRAFT.pdf` sitting alongside `Return_Policy_2026_APPROVED.pdf`), missing metadata headers, and raw HTML/OCR noise.
2. **Timeliness (Freshness) Check:** Compare the data source sync interval against the business volatility requirement (e.g., a 24-hour batch CSV export cannot ground a real-time *"Is this SKU in stock right now?"* query—it requires a live MCP/Connector API call!).
3. **Relevance Check:** Flag out-of-scope documents (e.g., `Cafeteria_Lunch_Menu.pdf` stored inside the `Customer_Warranty_SOP` SharePoint folder).
4. **Accuracy Check:** Verify whether authoritative ERP validation rules are enforced (`Unit_Price > 0`, valid currency codes).
5. **Availability Check:** Identify un-OCR'd scanned image PDFs (`has_text_layer == False`) or blocked network gateways.

#### Run the Complete Solution Script for Task 1:
Open your terminal and run:
```bash
python3 labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/grounding_data_quality_audit.py
```

---

### Task 2: Model 3-Year TCO, ROI %, Payback Period & Model Router Savings
In this task, you model the financial business case for Northwind Traders:
1. **Calculate Full TCO (CapEx + OpEx):**
   - Upfront CapEx: Data cleaning ($35,000) + Agent & Connector Engineering ($75,000) + Security/Red Teaming ($15,000) + Champion/User Prompt Training ($20,000) = **$145,000**.
   - Monthly Recurring OpEx: Model/Credit consumption + Azure AI Search + Application Insights + CoE maintenance.
2. **Compare Single-Model (Frontier Only) vs. Microsoft Foundry Model Router:**
   - **75% of traffic (90,000 queries/mo)** are Tier-1 simple intents (Order Status, FAQ, Address Update) -> Routed by **Model Router** to **Phi-4 / GPT-4o-mini**.
   - **25% of traffic (30,000 queries/mo)** are Tier-2 complex intents (Multi-contract dispute analysis, customs rerouting) -> Routed by **Model Router** to **GPT-5 / Frontier Reasoning**.

#### Run the Complete Solution Script for Task 2:
Open your terminal and run:
```bash
python3 labs/Lab-01-Enterprise-AI-Readiness-Grounding-and-ROI-Calculator/solution/roi_and_model_router_simulator.py
```

---

## 3. Complete Solution Walkthrough & Expected Output Interpretation

When you execute both solution scripts in `solution/`, review these key architectural takeaways for Exam AB-100:

| Observed Finding in Lab 01 | AB-100 Exam Rule Reinforced |
| :--- | :--- |
| `Return_Policy_2021_DRAFT.pdf` conflicts with `Return_Policy_2026_APPROVED.pdf` | **Cleanliness** failure -> Deduplicate & move drafts out of the indexed SharePoint folder. |
| `Live_Inventory_Snapshot.csv` is refreshed every 24 hours, causing oversold orders | **Timeliness** failure -> Replace static file indexing with a real-time **Power Platform Connector** or **MCP Server tool** for volatile transactional data. |
| `Legacy_Warehouse_Scan_1999.pdf` has `has_ocr_text_layer = False` | **Availability** failure -> Pre-process scanned PDFs through **Azure AI Document Intelligence (Layout model)** before indexing. |
| Implementing **Model Router** reduces monthly token inference spend by **~68%** and cuts average latency from **2,400 ms to 765 ms** | **Model Router** is the primary architectural pattern in Microsoft Foundry to optimize the Cost vs. Quality vs. Latency triangle! |
