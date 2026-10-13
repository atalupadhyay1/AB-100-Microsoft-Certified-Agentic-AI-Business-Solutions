# Lab 08: Agent Evaluation (Groundedness, Retrieval, Coherence, Relevance), AI Red Teaming & Content Safety Guardrails in Microsoft Foundry

> **AB-100 Exam Alignment:** Domain 3 — Deploy AI-Powered Business Solutions (40–45%)  
> **Modules Covered:** Module 08, Module 09, Module 11  
> **Estimated Time:** 40 minutes  
> **Level:** Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Woodgrove Bank** is preparing to promote its **Retail Banking & Mortgage Concierge Agent** in **Microsoft Foundry** (`https://ai.azure.com`) from UAT to Production. Before the Chief Risk Officer signs off on deployment, your architecture must pass three mandatory gates:

1. **Part A — Quantitative AI Quality Evaluation (`Groundedness`, `Retrieval`, `Coherence`, `Relevance`, `Tool Call Accuracy`):**
   - Run an automated evaluation over a Golden Dataset of customer queries and inspect which test rows fail Groundedness (hallucination) vs. Relevance vs. Retrieval.
2. **Part B — Automated AI Red Teaming (Adversarial Risk Scanning via PyRIT):**
   - Run an **AI Red Teaming** scan across risk categories (**Hate/Unfairness, Violence, Sexual, Self-Harm, Protected Material, Indirect Prompt Injection, PII Leakage**) and adversarial attack strategies (**Direct Jailbreak, Base64 Encoding, Character Space Injection, Roleplay Override, Cross-Prompt Injection [XPIA]**), measuring the **Attack Success Rate (ASR)**.
3. **Part C — Configuring Guardrails, Prompt Shields & Blocklists in Microsoft Foundry:**
   - Configure **Azure AI Content Safety Guardrails** (`guardrails_and_blocklist_config.json`) with **Prompt Shields** (User Prompt Injection + Document XPIA Shield), **Groundedness Detection**, and a **Custom Blocklist** blocking competitor bank names (`ContosoBank`, `FabrikamCredit`) and prohibited investment advice triggers.

---

## 2. Step-by-Step Hands-On Walkthrough in Microsoft Foundry (`ai.azure.com`)

### Task 1: Run Quality Evaluators in Microsoft Foundry
1. Sign in to **Microsoft Foundry** (`https://ai.azure.com`) and open your project (`prj-woodgrove-mortgage-uat`).
2. In the left navigation menu, select **Evaluation -> + New evaluation**:
   - **Target:** Select **Agent** (`Woodgrove Mortgage Concierge v1.2`) or upload a Golden Dataset `.jsonl` file containing `query`, `context`, `response`, and `ground_truth`.
   - **Select AI Quality Evaluators (Judge Model: `gpt-4o`):**
     - **Groundedness** (Threshold: $\ge 4.0 / 5.0$)
     - **Retrieval** (Threshold: $\ge 4.0 / 5.0$)
     - **Relevance** (Threshold: $\ge 4.0 / 5.0$)
     - **Coherence & Fluency** (Threshold: $\ge 4.0 / 5.0$)
     - **Intent Resolution & Tool Call Accuracy**
3. Review the completed evaluation scorecard:
   - Identify any row where **Retrieval = 5.0** but **Groundedness = 2.0** (diagnosing generation extrapolation!) and tune the system prompt / lower temperature to `0.0`.

---

### Task 2: Perform Automated AI Red Teaming in Microsoft Foundry
1. In the left navigation menu, select **Evaluation -> AI red teaming -> + Create red team scan** (or use `RedTeam` from `azure-ai-evaluation`):
   - **Risk Categories to Scan:**
     - `Violence`, `HateUnfairness`, `Sexual`, `SelfHarm`, `ProtectedMaterial`, `IndirectPromptInjection`, `SensitiveDataLeakage`.
   - **Attack Strategies (Converters) to Apply:**
     - `Baseline (Direct Prompt)`
     - `Base64 Encoding`
     - `ROT13 / Caesar Cipher`
     - `Leetspeak / Character Spacing`
     - `Roleplay / Persona Adoption ("DAN")`
     - `Indirect Document Injection (XPIA)`
2. Inspect the resulting **Attack Success Rate (ASR %)** matrix:
   - Production Gate Requirement: **Overall ASR must be $< 1.0\%$** after Guardrails are attached!

---

### Task 3: Configure Guardrails + Content Safety Filters in Microsoft Foundry
1. In the left navigation menu, select **Guardrails + controls -> Content filters -> + Create content filter** (`woodgrove-strict-banking-guardrail`):
   - **Input Filter (Prompt):**
     - Set **Hate, Violence, Sexual, Self-Harm** threshold to **Low (Block Low, Medium, and High severity)**.
     - Turn ON **Prompt Shields for Jailbreak (User Prompts)** -> Action: **Block**.
     - Turn ON **Prompt Shields for Indirect Attacks (Documents / Grounding Data)** -> Action: **Block**.
   - **Output Filter (Completion):**
     - Set **Hate, Violence, Sexual, Self-Harm** threshold to **Low (Block)**.
     - Turn ON **Protected Material (Text & Code)** -> Action: **Block**.
     - Turn ON **Groundedness Detection (Hallucination Shield)** -> Action: **Block / Annotate**.
2. Select **Blocklists -> + Create blocklist** (`woodgrove-competitors-and-investment-blocklist`):
   - Add exact terms (`ContosoBank`, `FabrikamCredit`) and regex patterns prohibiting guaranteed stock return promises.
   - Attach both the Content Filter and the Blocklist to your model deployment and Foundry Agent!

---

### Task 4: Run the Complete Evaluation, Red Teaming & Guardrail Suite Locally
Execute the runnable Python verification harness in your terminal:
```bash
python3 labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/solution/agent_evaluation_suite.py
```

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/agent_evaluation_suite.py`](./solution/agent_evaluation_suite.py) — Runnable evaluation and AI Red Teaming harness computing Groundedness, Retrieval, Relevance, Coherence, and Attack Success Rate (ASR) before vs. after Guardrails.
- [`solution/guardrails_and_blocklist_config.json`](./solution/guardrails_and_blocklist_config.json) — Complete Microsoft Foundry Guardrail, Prompt Shield, Groundedness Detection, and Blocklist configuration manifest.
