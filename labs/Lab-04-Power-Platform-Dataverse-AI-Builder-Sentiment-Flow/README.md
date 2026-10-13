# Lab 04: Using Copilot to Create Dataverse Tables, AI Builder Sentiment Analysis Flow & Canvas App AI

> **AB-100 Exam Alignment:** Domain 2 — Design AI-Powered Business Solutions (25–30%)  
> **Modules Covered:** Module 05 & Module 07  
> **Estimated Time:** 30 minutes  
> **Level:** Beginner to Intermediate

---

## 1. Lab Scenario & Business Objective (Humanized Context)

**Best For You Organics Company** collects thousands of customer product reviews across its retail stores and e-commerce app. Currently, customer experience managers read reviews manually in spreadsheets, often missing urgent negative reports about spoiled organic produce until days later.

As the Solution Architect, you need to build an end-to-end **Power Platform + AI Builder** solution:
1. **Task 1 — Create the `Customer Reviews` Table in Microsoft Dataverse using Copilot:** Use natural language in the Power Apps Maker Portal (`make.powerapps.com`) to generate a structured Dataverse table with AI-ready column descriptions, forms, and views.
2. **Task 2 — Build an Automated Sentiment Analysis & Routing Flow with AI Builder:** Trigger a flow whenever a new review row is added to Dataverse, invoke **AI Builder Sentiment Analysis** (and a custom **JSON Prompt Action**), store the `Sentiment` (`Positive`, `Neutral`, `Negative`) and `Confidence Score` back in Dataverse, and automatically route `Negative` reviews (`Confidence >= 0.75`) via urgent email and Microsoft Teams notification to the Quality Assurance team.
3. **Task 3 — Embed AI in a Power Apps Canvas App:** Allow store managers to analyze feedback on the spot using a Power Fx `Predict()` call and an **Agent Feed**.

---

## 2. Step-by-Step Hands-On Instructions

### Task 1: Use Copilot in the Maker Portal to Create the Dataverse Table
1. Sign in to the **Power Apps Maker Portal** (`https://make.powerapps.com`) and select your **Development** environment.
2. Open your unmanaged solution (`BestForYouOrganicsAI`) -> Select **+ New -> Table -> Describe the new table (Create with Copilot)**.
3. Enter the natural-language prompt:
   ```text
   Create a table named Customer Review to store customer product feedback for Best For You Organics Company. Include columns for Customer Name (Text), Customer Email (Email), Product SKU (Text), Review Text (Multiline Text), Sentiment Classification (Choice: Positive, Neutral, Negative), Confidence Score (Decimal 0.00 to 1.00), AI Summary and Root Cause (Multiline Text), and Escalation Status (Choice: Not Required, Pending QA Review, Resolved).
   ```
4. **Architect Verification Step (Crucial for AI Grounding!):**
   - Before clicking **Create**, review the generated schema and **enrich every column's `Description` metadata** (see `solution/dataverse-reviews-schema.json`). Remember from Module 02: Dataverse Copilot and Copilot Studio use column **Descriptions** and **Synonyms** to understand your schema!
5. Open the newly created `Customer Review` table -> Select **Forms -> Main Form** and **Views -> Active Customer Reviews** -> Add all AI output columns (`Sentiment Classification`, `Confidence Score`, `AI Summary and Root Cause`, `Escalation Status`) -> **Save and Publish**.

---

### Task 2: Build the Sentiment Analysis Flow using AI Builder
1. Inside your solution, select **+ New -> Automation -> Cloud flow -> Automated** (or create an **Agent Flow** inside Copilot Studio).
2. **Configure the Dataverse Trigger:**
   - **Connector:** `Microsoft Dataverse`
   - **Trigger:** `When a row is added, modified or deleted`
   - **Change type:** `Added`
   - **Table name:** `Customer Reviews (bfyo_customerreviews)`
   - **Scope:** `Organization`
3. **Add Step 2 — AI Builder Prebuilt Sentiment Analysis Action:**
   - Select **+ New step -> AI Builder -> Analyze positive or negative sentiment in text**.
   - **Language:** `English`
   - **Text:** Select dynamic content **`Review Text (bfyo_reviewtext)`** from the Dataverse trigger.
4. **Add Step 3 — Update the Dataverse Row with AI Results:**
   - Select **+ New step -> Microsoft Dataverse -> Update a row**.
   - **Table name:** `Customer Reviews`
   - **Row ID:** **`Customer Review (bfyo_customerreviewid)`**
   - **Sentiment Classification:** Map **`Overall text sentiment`** (`Positive`, `Neutral`, `Negative`).
   - **Confidence Score:** Map **`Probability overall text is negative`** (or dominant class score).
5. **Add Step 4 — Condition Branch for Negative Review Escalation:**
   - Add a **Condition** control:
     - `Overall text sentiment` **is equal to** `negative`
     - **AND** `Probability overall text is negative` **is greater than or equal to** `0.75`
   - **If Yes Branch:**
     - **Office 365 Outlook -> Send an email (V2)** to `qa-alerts@bestforyouorganics.com` with the `Review Text`, `Product SKU`, `Confidence Score`, and deep link to the Dataverse record.
     - Update `Escalation Status` to `Pending QA Review`.

---

### Task 3: Embed AI Builder in a Power Apps Canvas App (`OnSelect` Power Fx)
In your Canvas App for Store Managers, add a button **`btnAnalyzeFeedback`** and configure its `OnSelect` property with this exact **Power Fx formula**:

```powerfx
// Invoke prebuilt AI Builder Sentiment Model and Custom JSON Prompt Action directly from Canvas App
Set(
    varSentimentResult,
    'AI Builder Sentiment'.Predict(txtReviewInput.Text)
);
Set(
    varRootCauseJson,
    'Extract Organic Product Root Cause Prompt'.Predict(txtReviewInput.Text)
);

// Write structured result into Microsoft Dataverse
Patch(
    'Customer Reviews',
    Defaults('Customer Reviews'),
    {
        'Customer Name': txtCustomerName.Text,
        'Product SKU': txtProductSku.Text,
        'Review Text': txtReviewInput.Text,
        'Sentiment Classification': varSentimentResult.responsev2.predictionOutput.result.sentiment,
        'Confidence Score': varSentimentResult.responsev2.predictionOutput.result.sentimentScores.negative,
        'AI Summary and Root Cause': varRootCauseJson.StructuredOutput.rootCauseSummary,
        'Escalation Status': If(
            varSentimentResult.responsev2.predictionOutput.result.sentiment = "negative",
            'Escalation Status (Customer Reviews)'.'Pending QA Review',
            'Escalation Status (Customer Reviews)'.'Not Required'
        )
    }
);
Notify("Customer review analyzed with AI Builder and saved to Dataverse!", NotificationType.Success);
```

---

## 3. Complete Solution Artifacts in `solution/`

- [`solution/dataverse-reviews-schema.json`](./solution/dataverse-reviews-schema.json) — Complete AI-enriched Dataverse table, column, and metadata specification.
- [`solution/sentiment-routing-flow.json`](./solution/sentiment-routing-flow.json) — Complete Power Automate / Agent Flow definition integrating Dataverse, AI Builder Sentiment Analysis, Confidence Thresholding, and Email Routing.
