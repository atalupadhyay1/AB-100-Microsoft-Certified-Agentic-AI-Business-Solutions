#!/usr/bin/env python3
"""
AB-100 Lab 01 Solution: Enterprise TCO, ROI %, Payback Period & Model Router Simulator
Demonstrates:
1. Full 3-Year TCO (CapEx + OpEx) and ROI calculation for an agentic business solution.
2. Cost & latency optimization achieved by deploying a Microsoft Foundry Model Router
   (routing simple queries to an SLM like Phi-4 / GPT-4o-mini and complex queries to a Frontier Model).
"""

from dataclasses import dataclass


@dataclass
class ModelTier:
    name: str
    cost_per_1k_requests_usd: float
    avg_latency_ms: int


def simulate_roi_and_model_router() -> None:
    print("=" * 86)
    print("NORTHWIND TRADERS - AB-100 ENTERPRISE ROI, TCO & MODEL ROUTER FINANCIAL SIMULATOR")
    print("=" * 86)

    # Workload parameters
    monthly_enquiries = 120_000
    human_cost_per_enquiry_usd = 6.50
    autonomous_deflection_rate = 0.45  # 45% fully resolved by agent
    assisted_time_saving_rate = 0.20   # 20% time saved on remaining 55% of tickets

    # Upfront Implementation CapEx
    upfront_capex = {
        "Data Readiness & SharePoint/Dataverse Remediation": 35_000,
        "Agent Architecture, Copilot Studio & Foundry Build": 75_000,
        "Security Review, Purview DLP & AI Red Teaming": 15_000,
        "Change Management & User Prompt Training": 20_000,
    }
    total_capex = sum(upfront_capex.values())

    # Base Monthly Platform OpEx (excluding model tokens)
    base_monthly_opex = {
        "Azure AI Search + Dataverse Capacity": 2_200,
        "Application Insights Telemetry & Content Safety Guardrails": 950,
        "AI CoE Continuous Evaluation & Maintenance Labor": 4_500,
    }
    fixed_monthly_opex = sum(base_monthly_opex.values())

    # Model Tiers (including multi-turn prompt + RAG context + completion tokens per enquiry)
    slm_tier = ModelTier(name="Phi-4 / GPT-4o-mini (SLM Tier)", cost_per_1k_requests_usd=1.80, avg_latency_ms=220)
    frontier_tier = ModelTier(name="GPT-5 / o3 Reasoning (Frontier Tier)", cost_per_1k_requests_usd=42.00, avg_latency_ms=2400)

    # Traffic distribution: 75% simple (FAQ, Order Status, Address Update), 25% complex reasoning
    simple_share = 0.75
    complex_share = 0.25

    # Scenario A: All 120,000 requests sent to Frontier Model (No Model Router)
    monthly_model_cost_no_router = (monthly_enquiries / 1000.0) * frontier_tier.cost_per_1k_requests_usd
    avg_latency_no_router = frontier_tier.avg_latency_ms

    # Scenario B: Microsoft Foundry Model Router (75% -> SLM, 25% -> Frontier)
    monthly_model_cost_with_router = (
        (monthly_enquiries * simple_share / 1000.0) * slm_tier.cost_per_1k_requests_usd
        + (monthly_enquiries * complex_share / 1000.0) * frontier_tier.cost_per_1k_requests_usd
    )
    avg_latency_with_router = int(
        simple_share * slm_tier.avg_latency_ms + complex_share * frontier_tier.avg_latency_ms
    )

    # Monthly Gross Business Benefits
    deflected_enquiries = monthly_enquiries * autonomous_deflection_rate
    remaining_enquiries = monthly_enquiries * (1.0 - autonomous_deflection_rate)
    monthly_gross_benefit = (
        deflected_enquiries * human_cost_per_enquiry_usd
        + remaining_enquiries * human_cost_per_enquiry_usd * assisted_time_saving_rate
    )

    print("\n1. MODEL ROUTER OPTIMIZATION COMPARISON (120,000 Enquiries / Month):")
    print("-" * 86)
    print(f"  Without Model Router (100% Frontier Model): ${monthly_model_cost_no_router:10,.2f}/mo | Avg Latency: {avg_latency_no_router} ms")
    print(f"  With Foundry Model Router (75% SLM / 25% Frontier): ${monthly_model_cost_with_router:6,.2f}/mo | Avg Latency: {avg_latency_with_router} ms")
    token_savings_pct = (1.0 - (monthly_model_cost_with_router / monthly_model_cost_no_router)) * 100
    print(f"  -> Monthly Inference Savings: ${monthly_model_cost_no_router - monthly_model_cost_with_router:,.2f}/mo ({token_savings_pct:.1f}% cost reduction!)")

    # 3-Year TCO & ROI Calculation (Using Model Router Architecture)
    total_monthly_opex = fixed_monthly_opex + monthly_model_cost_with_router
    annual_opex = total_monthly_opex * 12
    annual_gross_benefit = monthly_gross_benefit * 12
    monthly_net_benefit = monthly_gross_benefit - total_monthly_opex

    year1_tco = total_capex + annual_opex
    year1_roi_pct = ((annual_gross_benefit - year1_tco) / year1_tco) * 100
    three_year_tco = total_capex + (annual_opex * 3)
    three_year_benefits = annual_gross_benefit * 3
    three_year_roi_pct = ((three_year_benefits - three_year_tco) / three_year_tco) * 100
    payback_months = total_capex / monthly_net_benefit

    print("\n2. EXECUTIVE TCO & ROI FINANCIAL SUMMARY (WITH MODEL ROUTER):")
    print("-" * 86)
    print(f"  Upfront Implementation CapEx        : ${total_capex:14,.2f}")
    print(f"  Monthly Recurring OpEx (All-In)     : ${total_monthly_opex:14,.2f} / month")
    print(f"  Monthly Quantified Labor Savings    : ${monthly_gross_benefit:14,.2f} / month")
    print(f"  Monthly Net Benefit                 : ${monthly_net_benefit:14,.2f} / month")
    print(f"  Year 1 Total Cost of Ownership (TCO): ${year1_tco:14,.2f}")
    print(f"  Year 1 ROI (%)                      : {year1_roi_pct:13.1f} %")
    print(f"  3-Year Total Cost of Ownership (TCO): ${three_year_tco:14,.2f}")
    print(f"  3-Year Total Quantified Benefits    : ${three_year_benefits:14,.2f}")
    print(f"  3-Year Net Present Value / Gain     : ${three_year_benefits - three_year_tco:14,.2f}")
    print(f"  3-Year ROI (%)                      : {three_year_roi_pct:13.1f} %")
    print(f"  Break-Even Payback Period           : {payback_months:13.2f} months (~{int(payback_months * 30)} days)")
    print("=" * 86)


if __name__ == "__main__":
    simulate_roi_and_model_router()
