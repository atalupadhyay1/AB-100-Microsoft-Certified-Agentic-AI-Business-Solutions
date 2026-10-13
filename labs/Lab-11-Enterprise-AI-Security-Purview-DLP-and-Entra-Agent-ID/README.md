# Lab 11: Enterprise AI Security — Microsoft Entra Agent ID, Purview DSPM for AI, Power Platform DLP & Indirect Prompt Injection Defense

> **AB-100 Exam Alignment:** Domain 3 — Deploy AI-Powered Business Solutions (Responsible AI, Security, Governance & Compliance)  
> **Modules Covered:** Module 11  
> **Estimated Time:** 40 minutes  
> **Level:** Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Lamna Healthcare Company** is rolling out agentic AI across its clinical administration, HR, and finance departments. Before the Chief Information Security Officer (CISO) approves tenant-wide production launch, you must configure four defense-in-depth governance controls:

1. **Task 1 — Microsoft Entra Agent ID & Zero-Secret Workload Identity:** Assign a dedicated **Microsoft Entra Agent ID** (with a mandatory human sponsor and least-privilege RBAC) to every autonomous agent so agents never share human user passwords or static client secrets.
2. **Task 2 — Power Platform Data Loss Prevention (DLP) & Connector Endpoint Filtering:** Configure a Power Platform DLP policy that separates **Business** connectors (`Dataverse`, `SharePoint`, `Dynamics 365`, `Approved MCP Server`) from **Non-Business** and **Blocked** connectors, and restricts the `HTTP / MCP` connector strictly to `https://mcp.lamnahealthcare.com/*` so an agent can never exfiltrate data to an attacker's domain.
3. **Task 3 — Microsoft Purview DSPM for AI, Sensitivity Label Inheritance & EU Data Residency:** Configure **Microsoft Purview Data Security Posture Management (DSPM) for AI** to audit all Copilot/Agent prompts, enforce **Sensitivity Label Inheritance** when summarizing labeled SharePoint files, block agents from reading `Board-Restricted-PHI` files, and verify **Data Zone Standard** residency compliance.
4. **Task 4 — Spotlighting & Indirect Prompt Injection (XPIA) Defense Validator:** Run a local Python defense harness (`prompt_injection_defense_validator.py`) demonstrating how **Spotlighting delimiters** + **Document Prompt Shields** + **DLP Outbound Domain Blocking** stop an Indirect Prompt Injection (XPIA) hidden inside an external PDF referral document.

---

## 2. Step-by-Step Hands-On Instructions

### Task 1: Register and Govern a Microsoft Entra Agent ID
1. Sign in to the **Microsoft Entra Admin Center** (`https://entra.microsoft.com`) or **Microsoft Foundry Control Plane (`ai.azure.com`)**.
2. Navigate to **Identity -> Agents (Microsoft Entra Agent ID)**:
   - Register the autonomous agent identity **`agent-lamna-claims-triage-prod`**.
   - Assign **Human Sponsor / Owner:** `Dr. Evelyn Carter (VP Clinical Operations)`.
   - Assign **Least-Privilege Azure & Dataverse RBAC:** Grant `Cognitive Services OpenAI User` on the regional Foundry resource and a scoped Dataverse security role (`Lamna Claims Triage Reader/Writer` — with zero access to Employee Payroll tables).
   - Configure **Microsoft Entra Conditional Access for Agents:** Require compliant Azure Managed Virtual Network origin and enable instant automated revocation if **Microsoft Defender for Cloud** flags anomalous tool invocation patterns.

---

### Task 2: Configure Power Platform DLP Policy & Connector Endpoint Filtering
1. Sign in to the **Power Platform Admin Center** (`https://admin.powerplatform.microsoft.com`) -> **Policies -> Data policies -> + New Policy** (`Lamna-Strict-Agentic-DLP`):
   - **Business Data Group:** `Microsoft Dataverse`, `SharePoint`, `Dynamics 365 Customer Service`, `Azure Key Vault`, `HTTP with Microsoft Entra ID (preauthorized)`.
   - **Blocked Group:** Public social media connectors, unapproved third-party file sharing, anonymous webhooks.
2. **Configure Connector Endpoint Filtering & Action Control:**
   - Select the `HTTP with Microsoft Entra ID` / `Custom MCP Connector` -> **Configure connector -> Connector endpoints**:
     - **Rule 1:** `Allow` -> `https://mcp.lamnahealthcare.com/*`
     - **Rule 2 (Default Catch-All):** `Deny` -> `*` (Blocks all other outbound URLs!).
   - Under **Connector actions**, disable `DELETE` operations so the agent can only execute `GET` and approved `POST` actions.

---

### Task 3: Configure Microsoft Purview DSPM for AI & Sensitivity Label Inheritance
1. Sign in to the **Microsoft Purview Portal** (`https://purview.microsoft.com`) -> Open **Solutions -> DSPM for AI (AI Hub)**:
   - Turn ON **Collection of prompts and responses** for Microsoft 365 Copilot, Declarative Agents, Copilot Studio, and Microsoft Foundry.
   - Review the **Oversharing Assessment** for SharePoint sites connected to agents and remediate any site shared with `"Everyone except external users"` that contains PHI/PII.
2. Navigate to **Information Protection -> Labels** and **Data Loss Prevention -> Policies**:
   - Create a Purview DLP policy targeting location **`Microsoft 365 Copilot and Copilot Studio agents`**:
     - **Condition:** Content contains Sensitivity Label **`Highly Confidential - Restricted Board / Unmasked PHI`**.
     - **Action:** **Block Copilot and agents from processing item**.
   - Verify **Automatic Sensitivity Label Inheritance:** When an agent summarizes a document labeled **`Confidential - Lamna Internal`**, the generated output and conversation context automatically inherit that label and its access restrictions.

---

### Task 4: Run the Indirect Prompt Injection (XPIA) Defense Validator Locally
Execute the runnable Python defense validator in your terminal:
```bash
python3 labs/Lab-11-Enterprise-AI-Security-Purview-DLP-and-Entra-Agent-ID/solution/prompt_injection_defense_validator.py
```

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/dlp-and-purview-governance.json`](./solution/dlp-and-purview-governance.json) — Complete enterprise security manifest for Microsoft Entra Agent ID, Power Platform DLP Endpoint Filtering, Purview DSPM for AI, and Data Residency controls.
- [`solution/prompt_injection_defense_validator.py`](./solution/prompt_injection_defense_validator.py) — Runnable multi-layered defense validator demonstrating Spotlighting delimiter wrapping, Document XPIA detection, Sensitivity Label enforcement, and DLP outbound URL filtering.
