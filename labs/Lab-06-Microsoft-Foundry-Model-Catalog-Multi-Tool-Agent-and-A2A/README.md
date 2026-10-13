# Lab 06: Microsoft Foundry Model Catalog, Multi-Tool Agent, Predictive AI Services & A2A Orchestration

> **AB-100 Exam Alignment:** Domain 2 — Design AI-Powered Business Solutions & Domain 1 — Strategy  
> **Modules Covered:** Module 03, Module 05, Module 06  
> **Estimated Time:** 45 minutes  
> **Level:** Intermediate to Advanced

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Contoso Pharmaceuticals** is establishing its enterprise AI factory in **Microsoft Foundry** (`https://ai.azure.com`). As the Lead Solution Architect, you must guide the engineering team through four practical capabilities in Microsoft Foundry:

1. **Part A — Model Catalog, Benchmarks & Serverless Deployment:** Evaluate foundation models (`GPT-5 / GPT-4o`, `Phi-4`, `Llama-3.3`, `Mistral`) using the **Microsoft Foundry Model Catalog Leaderboard** and **Quality vs. Cost / Latency Trade-Off Charts**, then deploy a chat model and a **Model Router**.
2. **Part B — Creating and Versioning a Multi-Tool Foundry Agent:** Build a versioned agent in **Microsoft Foundry Agent Service** equipped with **Code Interpreter** (for deterministic Python math/charts), **File Search** (vector store RAG), and **Web Search / Custom OpenAPI Tools**, and inspect execution **Traces** and **Thread Memory**.
3. **Part C — Agent2Agent (A2A) Multi-Agent Orchestration:** Connect an **Orchestrator Agent** to two **Specialist Agents** (Clinical Trial Data Specialist & Regulatory Compliance Specialist) using **A2A Agent Cards** and task delegation.
4. **Part D — Predictive AI Services (Microsoft Foundry Tools):** Use a single unified **Azure AI Services (Foundry Tools)** multi-service endpoint to perform **PII Redaction** (Azure AI Language), **Multilingual Translation** (Azure AI Translator), and **Speech Synthesis / Transcription** (Azure AI Speech) before sensitive medical notes reach an LLM!

---

## 2. Step-by-Step Hands-On Walkthrough in Microsoft Foundry (`ai.azure.com`)

### Task 1: Compare Models on the Leaderboard & Deploy from the Model Catalog
1. Sign in to the **Microsoft Foundry Portal** (`https://ai.azure.com`) and open or create a **Foundry Hub and Project** (`prj-contoso-pharma-dev`).
2. In the left navigation pane, select **Model catalog** -> **Model benchmarks (Leaderboard)**:
   - Compare models across **Quality Index** (Reasoning, Coding, Question Answering), **Safety / Harm Resistance**, **Throughput (Tokens/sec)**, and **Estimated Cost per 1M Tokens**.
   - Switch to the **Trade-off chart** view (`Quality vs. Cost` and `Quality vs. Latency`):
     - Notice how **Microsoft Phi-4 / GPT-4o-mini** sits in the top-left "High Efficiency" quadrant (low cost, sub-second latency) for classification/extraction, while **GPT-5 / o3-mini** leads the "Deep Reasoning" quadrant.
3. Select your target model -> Select **Deploy** -> Choose deployment type:
   - **`DataZoneStandard` (EU or US)** or **`Regional Standard`** (when strict data residency is required!), or **`Provisioned Throughput (PTU)`** (when guaranteed latency/throughput is required).

---

### Task 2: Create a Multi-Tool Agent, Inspect Traces & Manage Version History
1. In the Microsoft Foundry project left menu, select **Agents -> + New agent**:
   - **Agent Name:** `Contoso Clinical Operations Agent`
   - **Model Deployment:** Select your deployed chat model (`gpt-4o` or `gpt-5-chat`).
   - **System Instructions:** Define identity, scope, citation rules, and tool mandates.
2. **Add Multiple Tools to the Agent:**
   - **Knowledge -> + Add -> File Search:** Upload `Clinical_Trial_Protocol_v4.pdf` to create a managed Vector Store.
   - **Knowledge -> + Add -> Grounding with Bing Search** *(Note: Only for public medical literature queries; keep disabled for confidential internal patient data!)*.
   - **Actions -> + Add -> Code Interpreter:** Enables the agent to write and execute sandboxed Python code for statistical dosage calculations and chart generation.
   - **Actions -> + Add -> OpenAPI 3.0 tool / MCP Server:** Connect enterprise APIs.
3. **Test in the Agent Playground & Inspect Traces, Memory, and Versions:**
   - Open **Try in playground** and enter:
     > *"Calculate the mean, standard deviation, and 95% confidence interval for patient cohort recovery days [12, 14, 11, 19, 13, 15, 12, 14] using Code Interpreter, and check our Clinical Trial Protocol PDF for the Phase-2 reporting deadline."*
   - Select **Thread logs / Traces** at the top of the playground:
     - Inspect each span in the trace: `ThreadCreated` -> `RunStep: ToolCall (code_interpreter)` -> `RunStep: ToolCall (file_search)` -> `MessageCompleted`, along with exact prompt/completion token counts and latency!
   - Select **Save version** to create an immutable agent version snapshot (`v1.0.0`) before making prompt changes.

---

### Task 3: Run the A2A Multi-Agent Orchestrator & Predictive AI Services Locally
Execute both complete Python solutions in your terminal to see **Multi-Tool + A2A Orchestration** and **Foundry Tools Predictive AI (PII Redaction + Translation + Speech SSML)** in action:

```bash
python3 labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/foundry_multi_agent_orchestrator.py
python3 labs/Lab-06-Microsoft-Foundry-Model-Catalog-Multi-Tool-Agent-and-A2A/solution/pii_and_predictive_services.py
```

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/foundry_multi_agent_orchestrator.py`](./solution/foundry_multi_agent_orchestrator.py) — Implements Model Catalog trade-off selection, Multi-Tool Foundry Agent execution (Code Interpreter + File Search), and **Agent2Agent (A2A)** Orchestrator-Specialist delegation with OpenTelemetry-style trace logging.
- [`solution/pii_and_predictive_services.py`](./solution/pii_and_predictive_services.py) — Implements unified **Microsoft Foundry Tools** pre-processing: PII detection & redaction (Azure AI Language), multilingual translation with custom glossary (Azure AI Translator), and SSML voice output preparation (Azure AI Speech).
