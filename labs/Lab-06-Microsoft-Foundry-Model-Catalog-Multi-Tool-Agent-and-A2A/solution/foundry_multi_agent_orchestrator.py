#!/usr/bin/env python3
"""
AB-100 Lab 06 Solution: Microsoft Foundry Multi-Tool Agent & Agent2Agent (A2A) Orchestrator
Demonstrates:
1. Model Catalog Leaderboard & Trade-off selection (Quality vs. Cost vs. Latency).
2. Foundry Multi-Tool Agent (Code Interpreter deterministic math + File Search RAG + Version History).
3. Agent2Agent (A2A) Orchestrator-Specialist pattern using Agent Cards and structured task handoff.
"""

import json
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentCardA2A:
    agent_id: str
    name: str
    version: str
    endpoint_url: str
    skills: List[str]
    auth_scheme: str = "MicrosoftEntraAgentID"


@dataclass
class ExecutionTraceSpan:
    step_number: int
    component: str
    operation: str
    latency_ms: int
    tokens_used: int
    output_summary: str


class FoundryMultiAgentSystem:
    def __init__(self) -> None:
        self.traces: List[ExecutionTraceSpan] = []
        self.specialist_cards: Dict[str, AgentCardA2A] = {
            "clinical-stats-agent": AgentCardA2A(
                agent_id="entra-agent-id-stats-01",
                name="Contoso Clinical Biostatistics Agent",
                version="1.2.0",
                endpoint_url="https://foundry.contosopharma.com/a2a/clinical-stats",
                skills=["code_interpreter_statistics", "cohort_confidence_intervals"],
            ),
            "regulatory-policy-agent": AgentCardA2A(
                agent_id="entra-agent-id-reg-02",
                name="Contoso Regulatory & Protocol Grounding Agent",
                version="2.0.1",
                endpoint_url="https://foundry.contosopharma.com/a2a/regulatory-policy",
                skills=["file_search_protocol_rag", "eu_fda_compliance_check"],
            ),
        }

    def run_code_interpreter_tool(self, recovery_days: List[int]) -> Dict[str, float]:
        n = len(recovery_days)
        mean_val = sum(recovery_days) / n
        variance = sum((x - mean_val) ** 2 for x in recovery_days) / (n - 1)
        std_dev = math.sqrt(variance)
        margin_95 = 1.96 * (std_dev / math.sqrt(n))
        result = {
            "sample_size": n,
            "mean_days": round(mean_val, 2),
            "std_dev_days": round(std_dev, 2),
            "ci_95_lower": round(mean_val - margin_95, 2),
            "ci_95_upper": round(mean_val + margin_95, 2),
        }
        self.traces.append(
            ExecutionTraceSpan(
                step_number=len(self.traces) + 1,
                component="clinical-stats-agent (Code Interpreter Tool)",
                operation="execute_python_sandbox",
                latency_ms=340,
                tokens_used=285,
                output_summary=json.dumps(result),
            )
        )
        return result

    def run_file_search_tool(self, query: str) -> Dict[str, str]:
        citation = {
            "source_file": "Clinical_Trial_Protocol_v4.pdf",
            "page": "Page 18, Section 4.2",
            "grounded_excerpt": "Phase-2 adverse event and cohort recovery summaries must be submitted within 15 calendar days of cohort completion.",
            "query": query,
        }
        self.traces.append(
            ExecutionTraceSpan(
                step_number=len(self.traces) + 1,
                component="regulatory-policy-agent (File Search Vector Store)",
                operation="hybrid_semantic_search",
                latency_ms=190,
                tokens_used=410,
                output_summary=f"Cited {citation['source_file']} ({citation['page']})",
            )
        )
        return citation

    def orchestrate_user_request(self, user_prompt: str, cohort_data: List[int]) -> Dict[str, Any]:
        print("=" * 86)
        print("AB-100 LAB 06: MICROSOFT FOUNDRY MULTI-TOOL AGENT & A2A ORCHESTRATION TRACE")
        print("=" * 86)
        print(f"\nUser Prompt: {user_prompt}")

        print("\n[A2A Discovery] Registered Specialist Agent Cards:")
        for key, card in self.specialist_cards.items():
            print(f"  - {card.name} (v{card.version}) | Identity: {card.agent_id} | Skills: {card.skills}")

        # Delegate Step 1 via A2A to Clinical Stats Specialist (Code Interpreter)
        stats_output = self.run_code_interpreter_tool(cohort_data)

        # Delegate Step 2 via A2A to Regulatory Policy Specialist (File Search RAG)
        rag_output = self.run_file_search_tool("Phase-2 cohort recovery reporting deadline")

        # Synthesize final response
        self.traces.append(
            ExecutionTraceSpan(
                step_number=len(self.traces) + 1,
                component="Foundry Orchestrator Agent (v1.0.0)",
                operation="synthesize_grounded_response",
                latency_ms=480,
                tokens_used=520,
                output_summary="Synthesized statistical result + protocol citation.",
            )
        )

        print("\n[Execution Trace Log (Foundry Control Plane / Application Insights)]:")
        print("-" * 86)
        for span in self.traces:
            print(
                f"  Step {span.step_number}: {span.component:<48} | "
                f"{span.latency_ms:>4} ms | {span.tokens_used:>4} tok | {span.output_summary}"
            )

        final_response = {
            "agent_version": "Contoso-Clinical-Orchestrator-v1.0.0",
            "statistical_analysis": stats_output,
            "regulatory_requirement": rag_output["grounded_excerpt"],
            "inline_citation": f"[{rag_output['source_file']}, {rag_output['page']}]",
            "total_latency_ms": sum(s.latency_ms for s in self.traces),
            "total_tokens": sum(s.tokens_used for s in self.traces),
        }
        print("\n[Final Grounded Agent Response]:")
        print(json.dumps(final_response, indent=2))
        print("=" * 86)
        return final_response


if __name__ == "__main__":
    system = FoundryMultiAgentSystem()
    system.orchestrate_user_request(
        user_prompt="Calculate recovery statistics for cohort [12, 14, 11, 19, 13, 15, 12, 14] and check Phase-2 reporting deadline.",
        cohort_data=[12, 14, 11, 19, 13, 15, 12, 14],
    )
