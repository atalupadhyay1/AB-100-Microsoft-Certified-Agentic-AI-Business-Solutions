#!/usr/bin/env python3
"""
AB-100 Lab 01 Solution: 5-Dimension Grounding Data Quality Auditor
Evaluates candidate enterprise knowledge sources across the official AB-100 dimensions:
1. Accuracy
2. Relevance
3. Timeliness
4. Cleanliness
5. Availability
"""

from dataclasses import dataclass
from typing import List


@dataclass
class KnowledgeAsset:
    name: str
    source_type: str
    domain_topic: str
    target_agent_scope: str
    is_duplicate_or_draft: bool
    refresh_latency_minutes: int
    required_freshness_minutes: int
    has_ocr_text_layer: bool
    has_acl_permissions_configured: bool
    schema_validation_pass_rate: float  # 0.0 to 1.0


def evaluate_grounding_readiness(assets: List[KnowledgeAsset]) -> None:
    print("=" * 84)
    print("NORTHWIND TRADERS - AB-100 5-DIMENSION GROUNDING DATA QUALITY AUDIT REPORT")
    print("=" * 84)

    dimension_scores = {
        "Accuracy": [],
        "Relevance": [],
        "Timeliness": [],
        "Cleanliness": [],
        "Availability": [],
    }

    for asset in assets:
        issues = []

        # 1. Accuracy
        if asset.schema_validation_pass_rate < 0.98:
            issues.append(
                f"[ACCURACY] Validation pass rate is {asset.schema_validation_pass_rate:.0%} (<98%). "
                "Remediate upstream ERP/CRM validation rules and enforce Single Source of Truth."
            )
            dimension_scores["Accuracy"].append(50)
        else:
            dimension_scores["Accuracy"].append(100)

        # 2. Relevance
        if asset.domain_topic != asset.target_agent_scope:
            issues.append(
                f"[RELEVANCE] Asset topic '{asset.domain_topic}' does not match agent scope "
                f"'{asset.target_agent_scope}'. Scope SharePoint folder or add metadata filters."
            )
            dimension_scores["Relevance"].append(30)
        else:
            dimension_scores["Relevance"].append(100)

        # 3. Timeliness
        if asset.refresh_latency_minutes > asset.required_freshness_minutes:
            issues.append(
                f"[TIMELINESS] Refresh interval ({asset.refresh_latency_minutes} min) exceeds "
                f"business freshness SLA ({asset.required_freshness_minutes} min). "
                "Switch from static RAG indexing to a real-time Connector or MCP Tool call!"
            )
            dimension_scores["Timeliness"].append(25)
        else:
            dimension_scores["Timeliness"].append(100)

        # 4. Cleanliness
        if asset.is_duplicate_or_draft:
            issues.append(
                "[CLEANLINESS] Obsolete draft or duplicate version detected in active index. "
                "Archive deprecated versions out of the grounded SharePoint library."
            )
            dimension_scores["Cleanliness"].append(20)
        else:
            dimension_scores["Cleanliness"].append(100)

        # 5. Availability
        if not asset.has_ocr_text_layer or not asset.has_acl_permissions_configured:
            avail_reason = []
            if not asset.has_ocr_text_layer:
                avail_reason.append("Scanned image PDF lacks text layer (run Azure AI Document Intelligence Layout OCR)")
            if not asset.has_acl_permissions_configured:
                avail_reason.append("Missing On-Behalf-Of (OBO) / Entra ID ACL mapping")
            issues.append(f"[AVAILABILITY] {'; '.join(avail_reason)}.")
            dimension_scores["Availability"].append(20)
        else:
            dimension_scores["Availability"].append(100)

        status = "READY FOR GROUNDING" if not issues else "REMEDIATION REQUIRED"
        print(f"\nAsset: {asset.name} ({asset.source_type}) -> [{status}]")
        if issues:
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("  - Passes all 5 grounding quality dimensions (Accuracy, Relevance, Timeliness, Cleanliness, Availability).")

    print("\n" + "-" * 84)
    print("SUMMARY SCORECARD BY AB-100 DATA QUALITY DIMENSION:")
    print("-" * 84)
    for dim, scores in dimension_scores.items():
        avg_score = sum(scores) / len(scores)
        bar = "#" * int(avg_score // 5)
        print(f"  {dim:<15}: {avg_score:5.1f}% | {bar:<20} |")
    print("=" * 84)


if __name__ == "__main__":
    sample_enterprise_assets = [
        KnowledgeAsset(
            name="Return_Policy_2026_APPROVED.pdf",
            source_type="SharePoint Online",
            domain_topic="Customer Returns & Warranty",
            target_agent_scope="Customer Returns & Warranty",
            is_duplicate_or_draft=False,
            refresh_latency_minutes=60,
            required_freshness_minutes=1440,
            has_ocr_text_layer=True,
            has_acl_permissions_configured=True,
            schema_validation_pass_rate=1.0,
        ),
        KnowledgeAsset(
            name="Return_Policy_2021_DRAFT_OLD.pdf",
            source_type="SharePoint Online",
            domain_topic="Customer Returns & Warranty",
            target_agent_scope="Customer Returns & Warranty",
            is_duplicate_or_draft=True,  # Fails Cleanliness!
            refresh_latency_minutes=60,
            required_freshness_minutes=1440,
            has_ocr_text_layer=True,
            has_acl_permissions_configured=True,
            schema_validation_pass_rate=1.0,
        ),
        KnowledgeAsset(
            name="Live_Warehouse_Inventory_Nightly_Dump.csv",
            source_type="Blob Storage CSV",
            domain_topic="Customer Returns & Warranty",
            target_agent_scope="Customer Returns & Warranty",
            is_duplicate_or_draft=False,
            refresh_latency_minutes=1440,  # 24 hours old!
            required_freshness_minutes=1,  # Real-time stock check needed! Fails Timeliness!
            has_ocr_text_layer=True,
            has_acl_permissions_configured=True,
            schema_validation_pass_rate=0.91,  # Fails Accuracy!
        ),
        KnowledgeAsset(
            name="Employee_Cafeteria_Menus_2025.docx",
            source_type="SharePoint Online",
            domain_topic="Facilities & Dining",  # Fails Relevance!
            target_agent_scope="Customer Returns & Warranty",
            is_duplicate_or_draft=False,
            refresh_latency_minutes=60,
            required_freshness_minutes=1440,
            has_ocr_text_layer=True,
            has_acl_permissions_configured=True,
            schema_validation_pass_rate=1.0,
        ),
        KnowledgeAsset(
            name="Scanned_Carrier_Claims_Manual_1999.pdf",
            source_type="On-Premises File Share",
            domain_topic="Customer Returns & Warranty",
            target_agent_scope="Customer Returns & Warranty",
            is_duplicate_or_draft=False,
            refresh_latency_minutes=120,
            required_freshness_minutes=1440,
            has_ocr_text_layer=False,  # Fails Availability!
            has_acl_permissions_configured=False,
            schema_validation_pass_rate=0.99,
        ),
    ]
    evaluate_grounding_readiness(sample_enterprise_assets)
