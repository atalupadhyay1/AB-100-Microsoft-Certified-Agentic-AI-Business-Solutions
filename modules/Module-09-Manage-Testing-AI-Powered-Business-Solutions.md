# Module 09: Manage Testing AI-Powered Business Solutions

> **Official Course Mapping:** Course AB-100T00-A / Learning Path: *Architect AI solutions for business productivity*  
> **AB-100 Exam Domain:** Domain 3 — Deploy AI-Powered Business Solutions (40–45%)  
> **Official Units Preserved:** All 8 Units (Introduction -> Recommend Process & Metrics to Test Agents -> Create Validation Criteria for Custom AI Models -> Validate Effective Copilot Prompt Best Practices -> Design End-to-End Test Scenarios Across Multiple Dynamics 365 Apps -> Build a Strategy for Creating Test Cases Using Copilot -> Module Assessment -> Summary)  
> **Associated Hands-On Lab:** [Lab 08: Foundry Agent Evaluation, Red Teaming & Guardrails](../labs/Lab-08-Foundry-Agent-Evaluation-Red-Teaming-and-Guardrails/README.md)

---

## Part 1: Humanized Conceptual Foundation (Beginner Level)

### Why You Cannot Test an AI Agent Like a Calculator (`2 + 2 == 4`)

In traditional software testing, you write an exact assertion:
`assert calculate_tax(100.00) == 8.25`
If it returns `8.25`, the test passes. If it returns anything else, the test fails.

Now imagine testing a Customer Service AI Agent. You ask: *"How long do I have to return an unopened sweater?"*
- **Run 1:** *"You may return unopened clothing within 30 days of purchase with a receipt."*
- **Run 2:** *"Our return window for unworn items is 30 calendar days, provided you have proof of purchase."*

If you wrote a traditional exact string-match test (`assert response == "You have 30 days."`), **both Run 1 and Run 2 would FAIL**, even though both answers are 100% accurate, helpful, and polite!
Conversely, what if Run 3 says: *"You have 30 days, and we will also give you a free $500 gift card!"*—a traditional test checking `"30 days" in response` would **PASS**, even though the agent just hallucinated a $500 giveaway!

That is why testing Agentic AI requires a brand-new **AI Evaluation & Testing Pyramid**: combining **Semantic / AI-Graded Quality Evaluators (LLM-as-a-Judge)**, **Deterministic Tool/Action Verification**, **Adversarial AI Red Teaming**, and **End-to-End Cross-App Scenario Testing**.

---

## Part 2: Official Unit-by-Unit Deep Dive (Intermediate to Advanced Level)

### Unit 1 & Unit 2: Recommend the Process and Metrics to Test Agents

#### 1. The 5 Core AI Quality & RAG Evaluation Metrics in Microsoft Foundry & Copilot Studio Kit
Every AB-100 candidate must know the exact difference between these evaluation metrics:

| Evaluation Metric | What It Measures (Plain English) | Inputs Required by Evaluator | Failure Example |
| :--- | :--- | :--- | :--- |
| **1. Groundedness** | Does every factual claim in the agent's response come *strictly* from the retrieved source documents (context), with zero fabricated facts? | `Response` + `Retrieved Context` | Context says *"Refunds take 5–7 business days."* Agent says *"Refunds take 24 hours."* -> **Low Groundedness (Hallucination!)** |
| **2. Relevance** | Does the agent's response directly and completely answer the user's actual question/intent? | `User Query` + `Response` | User asks *"How do I cancel my subscription?"* Agent replies with a 100% factual paragraph about how the company was founded in 1998. -> **High Groundedness, but Low Relevance!** |
| **3. Retrieval Score (Context Relevance)** | Did the search engine (Azure AI Search / SharePoint) pull the right document chunks for the user's question? | `User Query` + `Retrieved Context` | User asks about dental insurance, and the RAG pipeline retrieves chunks about parking garage rules. -> **Low Retrieval Score!** |
| **4. Coherence & Fluency** | **Coherence:** Do the sentences flow logically and organize ideas clearly?<br>**Fluency:** Is the grammar, spelling, and syntax natural and readable? | `Response` (and `Query` for Coherence) | Garbled JSON fragments, cut-off sentences, or contradictory paragraphs. |
| **5. Task Adherence / Tool Call Accuracy (Intent Resolution)** | Did the agent follow its system instructions and invoke the **correct tool/connector with the correct parameters** in the right sequence? | `System Prompt` + `User Query` + `Tool Definitions` + `Agent Trace` | User says *"Cancel Order #402"* and the agent calls `GetOrderStatus(402)` instead of `CancelOrder(402)`. -> **Low Tool Call Accuracy!** |

#### 2. Recommended Tools for Automated Agent Testing
1. **Copilot Studio Kit (Power CAT) for Microsoft Copilot Studio Agents:**
   - Allows architects to define **Test Sets** containing hundreds of test utterances and expected responses/actions.
   - Supports **four test validation types** in Copilot Studio Kit:
     - **Exact Match:** For deterministic cards or status codes.
     - **Keyword / Regex Match:** Verifying specific policy numbers or URLs appear.
     - **Attachment / Adaptive Card Match:** Verifying the right UI card rendered.
     - **Generative AI Answers / Semantic Similarity & Groundedness (via Azure OpenAI / Foundry):** Grading whether the free-text generative response matches the expected meaning!
   - Enriches results with **Application Insights** telemetry (exact topic triggered, latency, and confidence score).
2. **Microsoft Foundry Evaluation SDK (`azure-ai-evaluation`) & Foundry Portal:**
   - Runs batch evaluations over a **Golden Dataset (`.jsonl`)** before deployment (CI/CD gate) and continuous evaluations on live production traces.
   - Includes **AI Red Teaming Agent (powered by PyRIT — Python Risk Identification Tool for generative AI)** to automatically simulate adversarial attacks (jailbreaks, prompt injections, Base64/ROT13 encoding bypasses, PII extraction) across risk categories (**Hate/Unfairness, Sexual, Violence, Self-Harm, Protected Material, Indirect Prompt Injection**).

---

### Unit 3: Create Validation Criteria for Custom AI Models

When your architecture includes a **Custom AI Model** (whether a fine-tuned SLM/LLM in Microsoft Foundry, a custom **Azure AI Document Intelligence** extraction model, or a custom **AI Builder Prediction / Classification** model), you must define formal **Validation Criteria** before promoting the model to Production:

```
+-----------------------------------------------------------------------------------+
|            VALIDATION GATE CRITERIA FOR CUSTOM AI MODELS                          |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. DATA SPLIT HYGIENE                                                            |
|     • Strictly separate Training Set (70%), Validation/Tuning Set (15%), and      |
|       held-out Blind Test Set / Golden Dataset (15%).                             |
|     • Zero data leakage between training and test sets!                           |
|                                                                                   |
|  2. QUANTITATIVE ACCURACY & QUALITY METRICS                                       |
|     • Classification / Intent / NER Models: Precision, Recall, F1-Score,          |
|       Confusion Matrix across all classes (including rare edge classes).          |
|     • Custom Document Intelligence: Field-level Extraction Accuracy & Confidence  |
|       Score thresholds (e.g., if confidence < 0.85 -> route to Human Review).     |
|     • Fine-Tuned Generative Models: Groundedness, Relevance, Semantic Similarity  |
|       (BLEU/ROUGE/BERTScore/AI-Assisted Grading) vs. baseline base model.         |
|                                                                                   |
|  3. NON-FUNCTIONAL & OPERATIONAL CRITERIA                                         |
|     • Latency SLA: Time-to-First-Token (TTFT) and P95 End-to-End Latency.         |
|     • Cost per 1,000 requests vs. baseline.                                       |
|                                                                                   |
|  4. RESPONSIBLE AI, FAIRNESS & SAFETY GATES                                       |
|     • Subgroup Fairness Parity (no accuracy drop across demographic/regional      |
|       cohorts).                                                                   |
|     • Attack Success Rate (ASR) on AI Red Teaming < threshold (e.g., < 1%).       |
+-----------------------------------------------------------------------------------+
```

> **Exam Tip on Precision vs. Recall vs. F1-Score:**
> - **High Precision** matters when **False Positives are expensive** (e.g., an autonomous agent automatically freezing a VIP customer's bank account for suspected fraud—you want to be sure when you freeze it!).
> - **High Recall** matters when **False Negatives are dangerous** (e.g., screening medical images or flagging high-risk legal clauses for a human lawyer to review—you don't want to miss any real risk!).
> - **F1-Score** is the harmonic mean of Precision and Recall, best when classes are imbalanced.

---

### Unit 4: Validate Effective Copilot Prompt Best Practices

How do you systematically test and validate that a **System Prompt** or **AI Builder Prompt Action** follows best practices and won't break in production?
1. **A/B Prompt Variant Testing (Prompt Flow / Foundry Variants):**
   - Never judge a prompt by typing 2 casual test messages in a chat box!
   - Create 2 or 3 **Prompt Variants** (`Variant_A`, `Variant_B`, `Variant_C`) and run all of them against a **Golden Test Dataset of 100+ diverse inputs** (including normal queries, ambiguous queries, typos, multilingual inputs, empty/missing fields, and adversarial prompt injection attempts).
2. **Determinism & Reproducibility Checks:**
   - Test prompts at low temperature (`0.0` to `0.2`) across multiple runs (`seed` parameter where supported) to verify output stability.
   - For structured outputs (JSON), validate 100% schema compliance against a strict JSON Schema validator.
3. **Boundary & Negative Testing ("Knowing When to Say I Don't Know"):**
   - At least 20% of your prompt validation test cases should ask questions **outside the scope** of the provided grounding data or business rules, verifying that the prompt abstains gracefully rather than hallucinating.

---

### Unit 5: Design End-to-End Test Scenarios for AI Solutions Using Multiple Dynamics 365 Apps

When an AI solution spans multiple Dynamics 365 apps (for example, **Dynamics 365 Sales** + **Dynamics 365 Customer Service** + **Dynamics 365 Supply Chain Management** + **Dynamics 365 Finance**), unit-testing a single prompt in isolation is not enough. You must design **End-to-End (E2E) Cross-Application Test Scenarios**:

#### Blueprint for Cross-Dynamics 365 End-to-End Testing
1. **Test Data Synchronization & Virtual Table / Dual-Write Integrity:**
   - Verify that when a Copilot Studio agent updates an order line in **Dynamics 365 Sales (Dataverse)**, the **Dual-Write / Virtual Table** integration reflects the change accurately in **Dynamics 365 Supply Chain Management** within expected latency, and rolls back cleanly if a business validation rule in F&O rejects the change (e.g., credit limit exceeded in **Dynamics 365 Finance**).
2. **Test Cross-App Role & Permission Propagation (End-to-End OBO Security):**
   - Test the exact same multi-app scenario under **three different user security personas**:
     - *Persona 1:* A Sales Representative (has access to D365 Sales Opportunities, but **no** access to D365 Finance payroll ledgers).
     - *Persona 2:* A Customer Service Representative (has access to Cases and RMAs).
     - *Persona 3:* An External Customer on Web Chat (anonymous/B2C scoped access).
   - Verify that the orchestrator agent never leaks data from a restricted Dynamics 365 app to an unauthorized persona!
3. **Test End-to-End Business Process State Transitions:**
   - Example E2E Test Scenario (*"Delayed Order Escalation to Credit Memo"*):
     - **Step 1 (D365 SCM):** Supplier Communications Agent processes a vendor email delaying Purchase Order `PO-881` by 14 days.
     - **Step 2 (D365 Customer Service):** Case Management Agent identifies impacted customer orders and alerts the Customer Service workspace.
     - **Step 3 (Copilot Studio + D365 Finance):** Customer requests a partial 10% shipping fee credit; the Task Agent verifies policy eligibility and creates a pending Credit Adjustment in D365 Finance for supervisor approval.
4. **Automated Regression Tooling for Dynamics 365 & Power Platform:**
   - Combine **Copilot Studio Kit** (for conversational & generative assertions), **Power Apps Test Engine / Playwright** (for Canvas & Model-Driven UI automation), and **Regression Suite Automation Tool (RSAT)** (for Dynamics 365 Finance and Supply Chain Management business processes).

---

### Unit 6: Build a Strategy for Creating Test Cases by Using Copilot

One of the smartest productivity accelerators for an AB-100 Solution Architect is **using generative AI (Copilot) to generate comprehensive test cases, synthetic golden datasets, and adversarial edge cases**!

#### The 4-Step Architect Strategy for AI-Generated Test Cases
1. **Seed from Real Requirements, Policies & Anonymized Transcripts:**
   - Feed your requirement specifications, SharePoint policy PDFs, OpenAPI schemas, and PII-scrubbed historical support logs to a **Test Case Generator Prompt** (in Microsoft 365 Copilot, GitHub Copilot, or Microsoft Foundry Simulator).
2. **Generate Stratified Test Personas & Edge Cases Automatically:**
   - Instruct Copilot to generate test cases across **five mandatory strata**:
     - **Happy Path (Standard Queries):** Clear, single-intent questions with exact grounding matches.
     - **Multi-Intent & Chained Tool Queries:** Utterances requiring two or more tool calls in sequence.
     - **Ambiguous / Typos / Colloquial Slang:** Incomplete inputs testing whether the agent asks clarifying questions.
     - **Out-of-Scope / Unanswerable Queries:** Questions not in the knowledge base, testing abstention (*"I don't have that information"*).
     - **Adversarial & Boundary Inputs:** Prompt injection attempts, numbers just above/below approval limits (`$9,999` vs. `$10,001`).
3. **Mandatory Human SME Curation ("Golden Dataset Sign-Off"):**
   - **CRITICAL EXAM RULE:** Never use AI-generated test cases as your final production gate without **Human Subject Matter Expert (SME) validation**! If an LLM generates both the test question and the "expected answer" without human review, it can bake its own hallucinations into the test suite. Domain SMEs must review and sign off on the **Golden Dataset**.
4. **Prevent Model Self-Preference Bias:**
   - When using an LLM-as-a-Judge evaluator to grade responses, use deterministic ground-truth assertions alongside a strong, calibrated evaluator model rubric.

---

## Part 3: Module 09 Assessment (Knowledge Check Quiz with Complete Solutions)

### Question 9.1
**Scenario:** Northwind Traders is testing a new HR Benefits Agent built in Microsoft Copilot Studio. When a tester asks *"How do I enroll my newborn child in dental insurance?"*, the agent retrieves the correct 2026 Dental Enrollment PDF chunk. However, instead of explaining the newborn enrollment steps, the agent responds with a 100% factually accurate summary of the company's history of dental benefits since 1995 (which was in the first paragraph of the same PDF chunk).

**Which evaluation metric will score LOW for this response, and which will score HIGH?**
- **A.** Groundedness will score HIGH; Relevance will score LOW.
- **B.** Groundedness will score LOW; Relevance will score HIGH.
- **C.** Retrieval Score will score 0.0; Fluency will score 0.0.
- **D.** Attack Success Rate (ASR) will score HIGH.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** Because every fact in the agent's response (the 1995 history) came directly from the retrieved PDF chunk without fabrication, **Groundedness** is **HIGH**. However, because the response failed to answer the user's actual question about enrolling a newborn child, **Relevance** is **LOW**.
- **Why B is Incorrect:** It reverses Groundedness and Relevance.
- **Why C & D are Incorrect:** The right PDF chunk was retrieved, the text was fluent, and no adversarial attack occurred.
</details>

---

### Question 9.2
**Scenario:** Bellows College wants to accelerate QA testing for a new Student Financial Aid Agent by using Microsoft 365 Copilot and the Microsoft Foundry simulator to automatically generate 500 synthetic test questions and expected reference answers from the college's 200-page Financial Aid Handbook PDF. A junior developer proposes immediately using these 500 unreviewed synthetic pairs as the sole pass/fail gate for production deployment.

**As the Solution Architect, what must you add to this test case generation strategy?**
- **A.** Require domain Subject Matter Experts (financial aid officers) to review, curate, and sign off on the AI-generated test cases and expected reference answers to establish a verified Golden Dataset, and include adversarial/out-of-scope test strata.
- **B.** Delete all test cases and rely only on production user complaints.
- **C.** Train the production agent directly on the test set so it memorizes all 500 test questions.
- **D.** Disable all automated testing in CI/CD pipelines.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** Using Copilot/simulators to draft test cases across happy-path, ambiguous, out-of-scope, and adversarial strata is a great accelerator, but **domain SMEs must curate and validate the expected ground-truth answers** so hallucinated expectations do not pollute the Golden Dataset.
- **Why B & D are Incorrect:** Skipping pre-production automated testing violates enterprise quality governance.
- **Why C is Incorrect:** Training a model on the test set (**data leakage**) invalidates the evaluation completely!
</details>

---

### Question 9.3
**Scenario:** Contoso Suites is designing end-to-end automated regression testing for an AI solution that spans a Microsoft Copilot Studio agent, a Dynamics 365 Customer Service model-driven app, and Dynamics 365 Finance and Supply Chain Management (F&O). You need to recommend the right Microsoft testing toolset across all three layers.

**Which combination of tools should you recommend?**
- **A.** Copilot Studio Kit for agent conversation/generative answer validation, Power Apps Test Engine (Playwright) for model-driven/canvas UI validation, and Regression Suite Automation Tool (RSAT) for Dynamics 365 Finance and Supply Chain Management business processes.
- **B.** Microsoft Paint, Notepad, and Windows Calculator.
- **C.** Azure AI Vision Spatial Analysis only.
- **D.** SharePoint Admin Center only.

<details>
<summary><strong>Click to Reveal Solution & Architect Rationale</strong></summary>

- **Correct Answer:** **A**
- **Why A is Correct:** **Copilot Studio Kit** validates agent utterances, topic matching, and AI-graded response quality; **Power Apps Test Engine** automates Power Apps / Dynamics 365 CE UI testing; and **RSAT (Regression Suite Automation Tool)** is the official automated regression tool for Dynamics 365 Finance and Supply Chain Management.
- **Why B, C, and D are Incorrect:** None of those tools perform cross-application automated functional or AI quality regression testing.
</details>
