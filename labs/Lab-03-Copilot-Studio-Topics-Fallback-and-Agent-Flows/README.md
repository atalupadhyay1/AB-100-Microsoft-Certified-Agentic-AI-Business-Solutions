# Lab 03: Copilot Studio Task & Autonomous Agents, Custom Fallback Topics & Human Escalation

> **AB-100 Exam Alignment:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Modules Covered:** Module 05 & Module 06  
> **Estimated Time:** 35 minutes  
> **Level:** Intermediate

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Adventure Works Cycles** is deploying a **Customer & Order Operations Agent** in **Microsoft Copilot Studio** with two major architectural capabilities:

1. **Custom Fallback Topic & Automatic Human Escalation (`Fallback.mcs.yml`):**
   - Out of the box, if a customer asks an unrecognized question that is not in any Topic or Knowledge Source, the default Fallback topic simply says *"I didn't understand."*
   - You need to engineer a production-grade **Custom Fallback Topic** that:
     - Tracks a global retry counter (`Global.FallbackCount`),
     - Logs the unrecognized user utterance (`System.Activity.Text`) to **Azure Application Insights** via a custom telemetry event (`UnrecognizedUserQuery`) so the AI CoE can mine the backlog,
     - On the **1st unrecognized attempt** (`Global.FallbackCount == 1`), politely prompts the user to rephrase or choose a quick-reply category, and
     - On the **2nd consecutive unrecognized attempt** (`Global.FallbackCount >= 2`), automatically redirects to the **`Escalate` (Transfer to Human Agent)** topic, passing the conversation context to **Dynamics 365 Contact Center**!
2. **Event-Driven Autonomous Order Triage (`AutonomousOrderTriage.mcs.yml`):**
   - When a new high-value wholesale order (`OrderTotal > $10,000`) is created in **Microsoft Dataverse** with a shipping hold flag, the agent must wake up **autonomously** (without a human chat prompt), invoke a deterministic **Agent Flow** to check warehouse inventory and customer credit status, and either automatically release the hold or post a **Human-in-the-Loop (HITL)** approval item to the supervisor's **Agent Feed**.

---

## 2. Step-by-Step Hands-On Instructions in Microsoft Copilot Studio

### Task 1: Configure Generative Orchestration & Agent Identity (`agent.mcs.yml`)
1. Open **Microsoft Copilot Studio** (`https://copilotstudio.microsoft.com`) and select your **Development** environment (inside your custom Power Platform Solution `AdventureWorksAI`).
2. Select **Create -> New agent** and configure:
   - **Name:** `Adventure Works Order & Support Concierge`
   - **Orchestration Mode:** Enable **Use generative AI to determine how best to respond to users and events (Generative Orchestration)**.
   - **Settings -> Generative AI:** Select **High (Strict)** content moderation so the agent prioritizes grounded accuracy over creative extrapolation.
   - **Settings -> Advanced -> Application Insights:** Paste your Azure Application Insights **Connection String** and turn ON **Log activities** and **Log sensitive Activity properties** (for Dev/UAT debugging).

---

### Task 2: Customize the System `Fallback` Topic (`Fallback.mcs.yml`)
1. In your Copilot Studio agent, navigate to **Topics -> System** and open the **`Fallback`** topic.
2. Switch to the **Code editor (YAML)** view (top-right `...` menu -> **Open code editor**) or add the following nodes visually:
   - **Node 1 (Set Variable Value):** Set `Global.FallbackCount` to formula `Coalesce(Global.FallbackCount, 0) + 1`.
   - **Node 2 (Log Custom Telemetry Event):** Emit event `UnrecognizedUserQuery` with property `UserUtterance: System.Activity.Text`.
   - **Node 3 (Condition Branch on `Global.FallbackCount`):**
     - **If `Global.FallbackCount < 2`:** Send a friendly rephrase prompt with Quick Reply buttons (`Track Order`, `Warranty Claim`, `Speak to Representative`).
     - **Else (`Global.FallbackCount >= 2`):** Reset `Global.FallbackCount = 0`, inform the customer that you are transferring them to a live specialist with full conversation context, and **Redirect to System Topic `Escalate` (`Transfer to agent`)**.

---

### Task 3: Configure an Autonomous Event Trigger & Agent Flow (`AutonomousOrderTriage.mcs.yml`)
1. Navigate to the **Overview** page of your Copilot Studio agent and locate the **Triggers** section.
2. Select **+ Add trigger** -> Select **When a row is added, modified or deleted (Microsoft Dataverse)**:
   - **Change type:** `Added`
   - **Table name:** `Sales Orders (salesorders)`
   - **Filter rows (OData):** `aw_ordertotal gt 10000 and aw_shippinghold eq true`
3. Define the **Payload Instructions** sent to the autonomous agent when the trigger fires:
   - Pass the `salesorderid`, `aw_ordertotal`, and `customerid`.
   - Instruct the agent to invoke the **`VerifyInventoryAndCreditAgentFlow`** action:
     - If `creditStatus == 'Approved'` and `OrderTotal <= 25000`, automatically release the hold.
     - If `OrderTotal > 25000` or `creditStatus == 'ReviewRequired'`, log an exception to the **Agent Feed** and send an Adaptive Card approval request to the Finance Supervisor in Microsoft Teams.

---

## 3. Complete Solution Artifacts in `solution/`

All three production-ready Copilot Studio YAML definitions are in place in `solution/`:
- [`solution/agent.mcs.yml`](./solution/agent.mcs.yml) — Agent manifest, Generative Orchestration settings, and Application Insights wiring.
- [`solution/Fallback.mcs.yml`](./solution/Fallback.mcs.yml) — Complete custom Fallback topic with retry counter, telemetry logging, and automatic human escalation.
- [`solution/AutonomousOrderTriage.mcs.yml`](./solution/AutonomousOrderTriage.mcs.yml) — Complete autonomous Dataverse event trigger, reasoning prompt, and HITL escalation flow.
