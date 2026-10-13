# AB-100 Complete Quizzes, Scenario Assessments & Full Mock Exam Hub

Welcome to the **Assessment & Practice Exam Suite** for **Exam AB-100: Microsoft Certified: Agentic AI Business Solutions Architect**.

Every single quiz, scenario case study, and practice exam question in this folder includes **the complete solution and a detailed architect-level rationale in place** (hidden inside collapsible `<details>` spoilers so you can test yourself first and then immediately verify your understanding!).

---

## Complete Assessment Directory

| File | Scope & Question Count | Target Score before Exam Day |
| :--- | :--- | :---: |
| **[`Module-Quizzes-01-to-11-With-Solutions.md`](./Module-Quizzes-01-to-11-With-Solutions.md)** | **55 Module Knowledge Check Questions** (5 questions per official module across Modules 01–11) with full solutions. | **85%+** (47 / 55) |
| **[`Domain-1-Plan-Practice-Quiz-and-Scenarios.md`](./Domain-1-Plan-Practice-Quiz-and-Scenarios.md)** | **Domain 1 (Plan: 25–30%)** — 15 Scenario Questions + 2 Full Enterprise Architecture Case Studies with complete solutions. | **80%+** |
| **[`Domain-2-Design-Practice-Quiz-and-Scenarios.md`](./Domain-2-Design-Practice-Quiz-and-Scenarios.md)** | **Domain 2 (Design: 25–30%)** — 15 Scenario Questions + 2 Full Enterprise Architecture Case Studies with complete solutions. | **80%+** |
| **[`Domain-3-Deploy-Practice-Quiz-and-Scenarios.md`](./Domain-3-Deploy-Practice-Quiz-and-Scenarios.md)** | **Domain 3 (Deploy: 40–45%)** — 20 Scenario Questions + 2 Full Enterprise Architecture Case Studies with complete solutions. | **85%+** |
| **[`Full-Length-AB-100-Mock-Exam-With-Solutions.md`](./Full-Length-AB-100-Mock-Exam-With-Solutions.md)** | **Full 60-Question Exam-Realistic AB-100 Mock Exam** (including 3 Multi-Question Enterprise Case Studies) weighted exactly to the October 2026 blueprint (27% Plan, 28% Design, 45% Deploy). | **750+ / 1000** (~78%+ raw score) |

---

## Architect's Exam-Day Strategy for AB-100

1. **Manage the 100-Minute Clock ruthlessly:**
   - Many candidates report that **Case Studies** (long multi-tab scenarios about a fictional enterprise's current environment, business requirements, technical constraints, and security rules) take significant reading time.
   - **Pro Tip for Case Studies:** Read the **question stem first**, then jump directly to the relevant section of the case study (e.g., *Security Requirements* or *Data Architecture*) rather than reading 2,000 words top-to-bottom before seeing what is asked!
2. **Use the "Microsoft Learn Open-Book Button" Wisely:**
   - You have access to `learn.microsoft.com` inside the Pearson VUE exam interface, **but the exam timer keeps running** while you search! Only open Microsoft Learn for 3–5 flagged questions to verify an exact connector/table name or SKU limit—never try to look up every question.
3. **Spot the Classic AB-100 Distractor Patterns:**
   - **Trap 1:** Recommending **Fine-Tuning** when the requirement is **up-to-date company facts or per-user ACL security trimming** (Correct answer: **RAG / Grounding with OBO or Azure AI Search security filters**).
   - **Trap 2:** Recommending **Computer Use (UI automation)** when a **REST API, Power Platform Connector, or MCP Server** already exists (Correct answer: **Always prefer APIs/MCP over UI automation**).
   - **Trap 3:** Recommending **Unmanaged Solutions** or manual edits in UAT/Production (Correct answer: **Managed Solutions + Environment Variables + Connection References**).
   - **Trap 4:** Relying on a **System Prompt instruction** (*"Do not share secret salaries"*) as a security boundary (Correct answer: **Enforce security at the Identity/Data/DLP layer via OBO, Entra Agent ID, Purview Sensitivity Labels, and Content Safety Prompt Shields**).
