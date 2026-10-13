# Lab 02: Creating a SharePoint Site Embedded Agent & Extending M365 Copilot with a Declarative Agent

> **AB-100 Exam Alignment:** Domain 1 (Plan) & Domain 2 (Design Extensibility)  
> **Modules Covered:** Module 01, Module 03, Module 06  
> **Estimated Time:** 35 minutes  
> **Level:** Beginner to Intermediate

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Tailspin Toys** has two urgent requirements for employees who already hold **Microsoft 365 Copilot** licenses:

1. **Part A — SharePoint Site Embedded Agent:** The Legal & Compliance department stores 40 approved vendor onboarding PDFs and Word documents inside a SharePoint Online site (`https://tailspintoys.sharepoint.com/sites/LegalCompliance`). They need an embedded agent directly inside that SharePoint site (and accessible in Microsoft Teams) that answers employee questions strictly from the `Approved_Policies` library, automatically enforces **On-Behalf-Of (OBO)** SharePoint permissions, and displays **published inline citations**.
2. **Part B — Microsoft 365 Copilot Declarative Agent with API Plugin:** Customer Support Managers working in Microsoft 365 Copilot Chat want a specialized **Tailspin Service Concierge Declarative Agent** that combines SharePoint knowledge with a real-time **API Plugin** (`openapi-service-cases.yaml`) to look up and update live service cases in Microsoft Dataverse / Dynamics 365 Customer Service.

---

## 2. Step-by-Step Hands-On Instructions

### Part A: Build and Publish a SharePoint Site Embedded Agent

1. **Prepare Clean Grounding Data in SharePoint Online:**
   - Open your SharePoint site (`https://<your-tenant>.sharepoint.com/sites/LegalCompliance`).
   - Create a dedicated document library named **`Approved_Policies`** and upload your clean, final PDFs and `.docx` files. *(Remember Module 02: Never leave obsolete `v1_DRAFT.pdf` files in the grounded folder!)*
2. **Create the Scoped SharePoint Agent:**
   - Inside the **`Approved_Policies`** document library, select the specific policy PDFs and Word documents (up to 20 files/folders per custom SharePoint agent selection), and select **Create an agent** from the command bar (or open the Copilot icon in the top-right corner of SharePoint and select **Create an agent**).
3. **Customize Identity, Instructions, and Starter Prompts:**
   - Select **Edit** on the newly created agent card:
     - **Name:** `Tailspin Legal & Vendor Policy Agent`
     - **Description:** `Answers employee questions strictly using approved Tailspin Toys vendor onboarding and legal compliance documents with mandatory source citations.`
     - **Instructions:**
       ```text
       You are the Tailspin Toys Legal & Vendor Compliance Assistant.
       1. Answer questions strictly using the grounded SharePoint documents in the Approved_Policies library.
       2. Always include clickable inline citations pointing to the exact source PDF or Word document.
       3. If a policy question is not covered in the grounded files, explicitly state that you do not have that information and direct the user to legal@tailspintoys.com. Never guess or fabricate legal terms.
       ```
     - **Starter Prompts:** Add 3 helpful starter prompts (e.g., *"What are the insurance requirements for Tier-1 suppliers?"*, *"Summarize the NDA escalation checklist"*).
4. **Verify On-Behalf-Of (OBO) Authorization & Citations (Advanced Customization in Copilot Studio):**
   - Select **Advanced -> Open in Copilot Studio** if you need to add custom topics or inspect authentication:
     - Under **Settings -> Security -> Authentication**, verify **Authenticate with Microsoft** (Entra ID On-Behalf-Of flow) is active. This guarantees that if `User2` does not have Read permission on `Executive_M&A_Addendum.pdf`, the agent will **never** surface content from that file to `User2`.
   - Select **Save and Share**, then copy the link to share in **Microsoft Teams** (where admins can also pin or approve the `.agent` file in the SharePoint site's `Site Assets -> Copilots` folder).

---

### Part B: Build a Microsoft 365 Copilot Declarative Agent with an OpenAPI Plugin

When you need a Declarative Agent packaged for enterprise ALM (via **Microsoft 365 Agents Toolkit** in VS Code or **Copilot Studio**), the agent consists of three core files (all provided in `solution/`):

1. **`declarativeAgent.json` (The Brain, Instructions & Scoped Knowledge):**
   - Defines the schema (`v1.2`), name, description, `instructions`, `conversation_starters`, `capabilities` (`OneDriveAndSharePoint`, `GraphConnectors`, `WebSearch` disabled for strict internal grounding!), and `actions` pointing to `ai-plugin.json`.
2. **`ai-plugin.json` (The Tool & Guardrail Manifest):**
   - Maps functions (`getOpenServiceCases`, `proposeCaseNextAction`) to the OpenAPI specification, defines **OAuth 2.0 / Entra ID OBO authentication**, and configures **Confirmation Prompts (Human-in-the-Loop)** before any write operation executes!
3. **`openapi-service-cases.yaml` (The REST API Contract):**
   - Defines the exact endpoints, HTTP methods (`GET`, `POST`), parameter types, and rich descriptions that M365 Copilot's orchestrator uses to invoke the tool.

---

## 3. Complete Solution Artifacts in `solution/`

Inspect the complete, production-ready solution files in this lab folder:
- [`solution/declarativeAgent.json`](./solution/declarativeAgent.json)
- [`solution/ai-plugin.json`](./solution/ai-plugin.json)
- [`solution/openapi-service-cases.yaml`](./solution/openapi-service-cases.yaml)
