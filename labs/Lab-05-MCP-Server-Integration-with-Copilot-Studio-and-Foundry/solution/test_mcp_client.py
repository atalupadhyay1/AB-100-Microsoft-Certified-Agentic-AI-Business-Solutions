#!/usr/bin/env python3
"""
AB-100 Lab 05 Verification Script: Tests the Trey Research MCP Server
Simulates Copilot Studio / Microsoft Foundry dynamic tool discovery (`tools/list`),
resource reading (`resources/read`), and tool execution (`tools/call`).
"""

import json
from mcp_enterprise_server import TreyResearchMCPServer


def run_mcp_verification() -> None:
    server = TreyResearchMCPServer()
    print("=" * 84)
    print("AB-100 LAB 05: MODEL CONTEXT PROTOCOL (MCP) SERVER VERIFICATION SUITE")
    print("=" * 84)

    # 1. Dynamic Tool Discovery
    tools = server.list_tools()
    print(f"\n[1] MCP `tools/list` Discovery -> Found {len(tools)} Registered Tools:")
    for tool in tools:
        print(f"  - Tool Name  : {tool['name']}")
        print(f"    Description: {tool['description']}")

    # 2. Call Tool 1: Generate 3-Month Study Plan for AB-100
    print("\n[2] MCP `tools/call` -> Invoking `generate_certification_study_plan` for AB-100:")
    plan_result = server.call_tool(
        "generate_certification_study_plan",
        {"exam_code": "AB-100", "hours_per_week": 8, "weakest_domain": "Deploy"},
    )
    print(json.dumps(plan_result, indent=2))

    # 3. Call Tool 2: Check Real-Time ERP Stock
    print("\n[3] MCP `tools/call` -> Invoking `check_realtime_erp_stock` for SKU-QUANTUM-09:")
    stock_result = server.call_tool("check_realtime_erp_stock", {"sku": "SKU-QUANTUM-09"})
    print(json.dumps(stock_result, indent=2))

    # 4. Read MCP Governance Resource
    print("\n[4] MCP `resources/read` -> Reading `trey://governance/mcp-security-standards`:")
    resource = server.read_resource("trey://governance/mcp-security-standards")
    print(resource["text"])
    print("=" * 84)


if __name__ == "__main__":
    run_mcp_verification()
