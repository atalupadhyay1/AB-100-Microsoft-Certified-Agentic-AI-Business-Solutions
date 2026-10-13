# Module 10: Design ALM Process for AI-Powered Business Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 3 — Deploy AI-Powered Business Solutions (40–45%)  
> **Official Units Preserved:** All 9 Units (Introduction -> ALM for Data Used in AI Models & Agents -> ALM for Copilot Studio Agents, Connectors & Actions -> ALM for Microsoft Foundry Agents -> ALM for Custom AI Models -> ALM for AI in Dynamics 365 Finance & Supply Chain -> ALM for AI in Dynamics 365 Customer Experience & Service -> Module Assessment -> Summary)  
> **Associated Hands-On Lab:** [Lab 10: Power Platform Managed Solutions & Agentic ALM CI/CD Pipelines](../labs/Lab-10-Power-Platform-Managed-Solutions-and-Agentic-ALM-Pipelines/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Why Editing an AI Agent Directly in Production Is Like Performing Surgery on a Running Marathon Runner

Imagine a software developer logging straight into your bank's live Production website at 2:00 PM on a Tuesday, editing a few lines of code without saving a backup, and hoping nothing breaks. Every experienced engineer shudders at that thought!

Yet in many organizations, well-meaning makers open **Microsoft Copilot Studio** or **Microsoft Foundry** in the live **Production environment**, tweak a system prompt, change a SharePoint URL, or edit an Agent Flow—and accidentally break the live customer service bot for 50,000 customers!

**Application Lifecycle Management (ALM)**—combined with **DataOps**, **AgentOps**, and **MLOps / GenAIOps**—is the disciplined engineering process that ensures:
1. Makers build and experiment safely in an isolated **Development (Dev)** environment.
2. Every component—agent topics, YAML definitions, system prompts, connectors, environment variables, grounding index schemas, and model versions—is stored in **Git source control** (`GitHub` or `Azure DevOps`).
3. Automated **CI/CD Pipelines** run **Solution Checker**, **AI Quality Evaluators**, and **AI Red Teaming** in a **Test / UAT** environment.
4. Only verified, immutable packages (**Managed Solutions** in Power Platform and versioned **Bicep / Container / Agent Manifests** in Microsoft Foundry) are promoted to **Production**, with instant 1-click rollback if anything goes wrong!

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Design an ALM Process for Data Used in AI Models and Agents (DataOps for AI)

Most people think ALM only applies to code. On Exam AB-100, you must also design **ALM for the Data** that grounds your agents and tunes your models!

#### The 4 Pillars of Data ALM for AI Models and Agents

| Data Asset Type | How to Version & Promote Across Dev -> Test -> Prod | Critical Architect Safeguards |
| :--- | :--- | :--- |
| **1. Grounding Knowledge Repositories (SharePoint, Blob Storage, Azure AI Search Indexes)** | • Maintain environment-specific SharePoint sites or Azure AI Search indexes (`idx-kb-dev`, `idx-kb-uat`, `idx-kb-prod`).<br>• Version the **Azure AI Search index schema JSON**, skillset definitions, and chunking parameters in Git.<br>• Point the agent to the right regional/environment index using **Environment Variables**! | Never point a **Dev** agent at a live **Production** transactional database with write permissions! Use sanitized/anonymized data in Dev/Test. |
| **2. Fine-Tuning & Training Datasets (`.jsonl` / OneLake Tables)** | • Store training, validation, and **Golden Evaluation Datasets** as immutable, versioned dataset assets in **Microsoft Foundry Data Assets** or **Microsoft Fabric OneLake / Azure Machine Learning Data Assets** (e.g., `customer-support-sft-v3`).<br>• Record dataset cryptographic hashes (`SHA-256`) for lineage auditing. | Run automated **PII Redaction** and **Data Quality Drift** checks before any dataset version is approved for model fine-tuning. |
| **3. Dataverse Configuration & Reference Data (Business Terms, Prompt Config Rows, Routing Rules)** | • Schema changes (tables/columns) travel inside **Power Platform Solutions**.<br>• Reference/configuration records (such as **Business Terms**, AI routing thresholds, or KB articles) are migrated across Dev -> Test -> Prod using the **Configuration Migration Tool (CMT)**, **Power Platform CLI (`pac data export` / `pac data import`)**, or **Dataflows**! | Preserve **Record GUIDs** when migrating reference records across environments so lookup relationships inside flows and agents do not break. |
| **4. Vector Embeddings Model Upgrades** | • If you upgrade your embedding model (e.g., from `text-embedding-ada-002` to `text-embedding-3-large`), old vectors and new vectors live in incompatible mathematical spaces! | Use **Blue-Green Index Promotion**: build a brand-new index (`idx-kb-prod-v2`), re-embed all chunks into `v2`, validate retrieval quality, and swap the Environment Variable pointer with zero downtime. |

---

### Unit 3: Design an ALM Process for Copilot Studio Agents, Connectors, and Actions

This is one of the highest-yield topics on the entire AB-100 exam. Memorize every piece of **Power Platform & Copilot Studio ALM**!

```
+-----------------------------------------------------------------------------------+
|       END-TO-END ALM PIPELINE FOR MICROSOFT COPILOT STUDIO SOLUTIONS              |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ DEVELOPMENT ENVIRONMENT ] (Unmanaged Solution: `ContosoCustomerAgent_Dev`)     |
|   ├── Copilot Studio Agent (Topics, Knowledge pointers, Instructions)             |
|   ├── Agent Flows & Custom Prompt Actions (AI Builder)                            |
|   ├── Custom Connectors & MCP Server Connectors                                   |
|   ├── CONNECTION REFERENCES (Abstracts auth away from hardcoded user accounts!)   |
|   └── ENVIRONMENT VARIABLES (Abstracts URLs, SharePoint sites, Foundry endpoints!)|
|            |                                                                      |
|            | 1. Export & Unpack via PAC CLI (`pac solution export` + `unpack`)    |
|            v                                                                      |
|  [ GIT REPOSITORY (GitHub / Azure Repos) ]                                        |
|   • Stores human-readable `.mcs.yml` YAML topics, flow JSONs, & schema XML        |
|   • Pull Request triggers Solution Checker + Automated Lint                       |
|            |                                                                      |
|            | 2. Pack as MANAGED Solution & Import to UAT (`pac solution import`)  |
|            |    + Apply `deployment-settings.json` (binds UAT URLs & Connections) |
|            v                                                                      |
|  [ TEST / UAT ENVIRONMENT ] (Managed Solution: Locked against direct ad-hoc edits)|
|   • Run Copilot Studio Kit Automated Test Suite (Groundedness, Intent Accuracy)   |
|   • Business SME User Acceptance Testing (UAT) & Approval Gate                    |
|            |                                                                      |
|            | 3. Promote Verified Managed Solution Artifact to Production          |
|            v                                                                      |
|  [ PRODUCTION ENVIRONMENT ] (Managed Solution + Application Insights Monitoring)  |
+-----------------------------------------------------------------------------------+
```

#### The 4 Golden Rules of Copilot Studio ALM (Never Miss These on the Exam!):

1. **Always Build Inside a Custom Power Platform Solution (Never in the Default Solution!):**
   - Create a dedicated **Unmanaged Solution** in your **Development** environment with a custom **Publisher and Prefix** (e.g., ` nw_` for Northwind).
   - Export as **Unmanaged** to commit/unpack to Git (`pac solution unpack`), and export/pack as **Managed** to deploy into **Test/UAT and Production**.
   - **Why Managed in Test & Prod?** Because **Managed Solutions** prevent makers from making untracked "cowboy edits" directly in Production, and allow clean layered upgrades or full uninstall/rollback!

2. **Use Environment Variables for All Environment-Specific Endpoints and Knowledge Sources:**
   - In Dev, your agent grounds on `https://contoso.sharepoint.com/sites/HR-Dev` and calls `https://foundry-dev.openai.azure.com`.
   - In Prod, it must ground on `https://contoso.sharepoint.com/sites/HR-Prod` and call `https://foundry-prod.openai.azure.com`.
   - **Never manually edit the agent in Prod to change URLs!** Store SharePoint site URLs, Dataverse environment URLs, Azure AI Search index names, and Foundry endpoints in **Power Platform Environment Variables**, and pass environment-specific values during CI/CD deployment via a **`deployment-settings.json`** file!

3. **Use Connection References for All Connectors and Actions:**
   - A **Connection** holds actual credentials (e.g., *User1's OAuth token* or *Prod Service Principal secret*). Connections cannot be exported in a solution!
   - A **Connection Reference** is a solution-aware pointer included in your solution that says: *"This Agent Flow needs a ServiceNow connector."* When you import the Managed Solution into UAT or Prod via `deployment-settings.json`, you bind that **Connection Reference** to the UAT or Prod Service Principal connection without touching a single line of agent logic!

4. **Choose Between Power Platform Pipelines (In-Product Low-Code ALM) and Pro-Code CI/CD (GitHub Actions / Azure DevOps):**
   - **Power Platform Pipelines (in Managed Environments):** Best for low-code makers; provides one-click governed deployment from Dev -> Test -> Prod with pre-deployment approval gates and AI-generated deployment notes right inside the maker portal.
   - **GitHub Actions / Azure DevOps with Power Platform Build Tools & PAC CLI:** Best when you need **Git source-control branching**, **pull request code reviews on `.mcs.yml` YAML files**, **automated Copilot Studio Kit test execution**, or **coordinated multi-platform deployments** alongside Microsoft Foundry Bicep templates!

---

### Unit 4 & Unit 5: Design ALM Processes for Microsoft Foundry Agent Service & Custom AI Models (GenAIOps / MLOps)

When your solution includes **Microsoft Foundry Agents** and **Custom AI Models**, how do you design their ALM lifecycle?

#### 1. ALM for Microsoft Foundry Agent Service (Unit 4)
1. **Hub and Project Environment Isolation:**
   - Architect separate Microsoft Foundry projects (or separate Hubs across Azure Subscriptions: `sub-ai-dev`, `sub-ai-test`, `sub-ai-prod`) with strict **Azure RBAC** and **Managed Virtual Networks**.
2. **Infrastructure as Code (IaC) & Declarative Agent Manifests:**
   - Define all Foundry infrastructure (Foundry Hub, Project, Azure OpenAI model deployments, Azure AI Search, Application Insights, Key Vault, Managed Identities, and Azure API Management) in modular **Bicep** or **Terraform** templates stored in Git.
   - Store **Foundry Agent definitions** (system instructions, model name/version, temperature, OpenAPI/MCP tool definitions, vector store IDs, and Content Safety guardrail policy names) as version-controlled **YAML/JSON manifests or Python/C# SDK code** in Git.
3. **Automated Evaluation & Red-Teaming Gate in CI/CD:**
   - Every Pull Request or release pipeline in GitHub Actions / Azure DevOps automatically executes the **Microsoft Foundry Evaluation SDK** against the Golden Dataset and runs the **AI Red Teaming Agent**.
   - **Pipeline Quality Gate:** If `Groundedness < 4.2` or `Relevance < 4.0` or `Red Team Attack Success Rate > 1%`, **the CI/CD pipeline automatically fails and blocks deployment to Production!**

#### 2. ALM for Custom AI Models & Model Version Upgrades (Unit 5)
What happens when a base model is retiring, or you fine-tune a new version (`v2`) of your custom model?
1. **Model Registry & Immutable Versioning:** Register every trained or fine-tuned model in the **Microsoft Foundry / Azure ML Model Registry** with immutable version tags (`claims-classifier:v1`, `claims-classifier:v2`), training dataset lineage, hyperparameters, and evaluation metrics.
2. **Never Use Auto-Upgrade on Mission-Critical Production Endpoints Without Validation:**
   - Pin your production deployment to a specific model version (e.g., `gpt-4o-2024-11-20` rather than floating `latest`), or test new model versions in a **Staging / Shadow slot** first!
3. **Safe Production Rollout Patterns (Blue-Green, Canary & Shadow Deployment):**
   - **Shadow Testing (Dark Launch):** Mirror a percentage of live production prompts to the new model version `v2` in the background (without showing `v2`'s output to users) and compare latency/groundedness scores against `v1`.
   - **Canary / Traffic Splitting (Weighted Routing):** Use **Microsoft Foundry Managed Online Endpoints** or **Azure API Management (APIM)** to route **10% of live traffic to `v2`** and **90% to `v1`**. Monitor telemetry for 24 hours; if metrics stay healthy, shift 50% -> 100% to `v2` (or roll back to 100% `v1` in 1 second if an issue appears!).

---

### Unit 6 & Unit 7: Design ALM Processes for AI in Dynamics 365 (Finance & Supply Chain vs. Customer Experience & Service)

Exam AB-100 tests whether you know the architectural difference between ALM for **Dynamics 365 CRM (Customer Engagement)** and **Dynamics 365 ERP (Finance & Supply Chain Management)**:

| ALM Dimension | Dynamics 365 Customer Experience & Service (Sales, Customer Service, Contact Center, Field Service) | Dynamics 365 Finance & Supply Chain Management (F&O Apps) |
| :--- | :--- | :--- |
| **Underlying Platform** | Native **Microsoft Dataverse** & Power Platform. | **X++ / Application Object Tree (AOT)** runtime + linked **Dataverse / Power Platform environment** (Unified Admin Experience). |
| **How AI & Agent Customizations Are Packaged** | Packaged directly inside **Power Platform Managed Solutions** (Copilot Studio agents, Custom Topics, Prompt Actions, Business Terms config, Connectors, Contact Center routing rules). | **Two synchronized artifact streams:**<br>1. **F&O Deployable Packages** (for X++ extensions, custom business events, data entities) via Azure DevOps & LCS / Unified Admin.<br>2. **Power Platform Managed Solutions** (for the linked **Copilot for finance and operations apps** agent extensions, SharePoint knowledge pointers, and Copilot Studio plugins!). |
| **How Reference Data & Routing Configs Move Across Environments** | **Configuration Migration Tool (CMT)** or **PAC CLI (`pac data`)** for moving Business Terms, Omnichannel queues/workstreams, and Knowledge Articles with preserved GUIDs. | **Data Management Framework (DMF) Data Packages** for ERP configuration entities + **Power Platform Solutions / Environment Variables** for Dataverse/Copilot components. |
| **Key Cross-Platform ALM Rule** | Always deploy schema & custom connectors first, bind Connection References & Environment Variables via `deployment-settings.json`, then enable active flows/triggers. | **Synchronize release cadences!** If a Copilot Studio agent extension depends on a new custom F&O Data Entity or Business Event, the **F&O Deployable Package must be deployed to the target environment BEFORE or TOGETHER WITH the Power Platform Managed Solution**! |

---

## Part 3: Module 10 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 10.1
**Scenario:** Alpine Ski House has built a Microsoft Copilot Studio agent in its Development environment that connects to a Development SharePoint site (`https://alpineskihouse.sharepoint.com/sites/DevPolicies`) and uses a ServiceNow connector to create IT tickets. When promoting the agent to the UAT and Production environments via an automated Azure DevOps pipeline, the architect wants to ensure that:
1. Nobody can manually edit the agent's topics directly inside the UAT or Production environments, and
2. The agent automatically connects to the UAT/Production SharePoint sites and UAT/Production ServiceNow service accounts without modifying the agent's topics after import.

**What should you include in your ALM design?**
- **A.** Export the solution as an Unmanaged Solution and ask an admin to manually edit every topic in Production after import.
- **B.** Package the agent in a Managed Solution, use Environment Variables for the SharePoint site URLs, use Connection References for the ServiceNow connector, and supply environment-specific values via a `deployment-settings.json` file during pipeline import.
- **C.** Copy and paste the topic text manually between three browser tabs.
- **D.** Use Computer Use to click the SharePoint settings in Production.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **B**
- **Why B is Correct:** In Power Platform and Copilot Studio ALM: **Managed Solutions** lock components against ad-hoc edits in downstream (UAT/Prod) environments; **Environment Variables** parameterize environment-specific URLs (like SharePoint sites or Foundry endpoints); **Connection References** abstract connector authentication; and **`deployment-settings.json`** injects the target environment's values automatically during CI/CD import.
- **Why A, C, and D are Incorrect:** Unmanaged solutions and manual post-import edits in Production violate ALM governance and cause unmanaged layer drift.
</details>

---

### Question 10.2
**Scenario:** Wingtip Toys operates a mission-critical customer service agent in Microsoft Foundry currently running on `gpt-4o` version `v1`. A new model version `v2` has passed offline golden dataset evaluations in the Test environment. Now, you want to roll out `v2` to Production while minimizing risk to live customers: initially sending only 10% of live production traffic to `v2` and 90% to `v1`, comparing live groundedness and latency telemetry in Application Insights, and automatically shifting 100% back to `v1` if error rates rise.

**Which deployment strategy should you implement?**
- **A.** Canary deployment (weighted traffic splitting) using Microsoft Foundry Managed Online Endpoints or Azure API Management.
- **B.** Delete `v1` immediately at noon on Friday and deploy `v2` without a rollback plan.
- **C.** Unmanaged solution export in SharePoint Online.
- **D.** Disable Application Insights telemetry during the upgrade.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** Routing a small percentage (10%) of live production traffic to a new model version while keeping 90% on the stable version, monitoring live telemetry, and supporting instant traffic rollback is a **Canary deployment (weighted traffic splitting)** pattern.
- **Why B, C, and D are Incorrect:** Deleting `v1` without fallback creates an outage risk, SharePoint solutions don't host Foundry models, and disabling telemetry blinds operations during rollout.
</details>

---

### Question 10.3
**Scenario:** Tailspin Toys is extending the **Copilot for finance and operations apps** agent in Microsoft Copilot Studio to invoke a newly created custom X++ OData Data Entity (`TailspinVendorRiskEntity`) in Microsoft Dynamics 365 Supply Chain Management. When the release pipeline imports the Power Platform Managed Solution into the UAT environment before the Dynamics 365 Finance and Operations deployable package has been applied to UAT, the agent fails validation.

**How should you fix the cross-platform ALM release pipeline?**
- **A.** Coordinate the release pipeline so the Dynamics 365 Finance and Operations deployable package (containing the custom X++ Data Entity and Dual-Write/Virtual Table metadata) is deployed and synchronized in the target UAT environment prior to importing the dependent Power Platform Managed Solution.
- **B.** Convert the Production environment to an Unmanaged development environment.
- **C.** Remove all security roles from Microsoft Dataverse.
- **D.** Delete the X++ Data Entity from source control.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** When an AI solution spans **Dynamics 365 Finance & Supply Chain Management (F&O)** and **Power Platform / Copilot Studio**, backend F&O artifacts (deployable packages containing custom X++ data entities or business events) must be deployed and exposed to Dataverse **before** importing the Power Platform Managed Solution that references them.
- **Why B, C, and D are Incorrect:** None of these resolve cross-platform deployment ordering dependencies.
</details>
