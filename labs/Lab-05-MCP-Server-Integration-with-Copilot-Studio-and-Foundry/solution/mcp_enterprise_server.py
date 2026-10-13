#!/usr/bin/env python3
"""
AB-100 Lab 05 Solution: Enterprise Model Context Protocol (MCP) Server
Implements JSON-RPC 2.0 MCP methods (`tools/list`, `tools/call`, `resources/list`, `resources/read`)
compatible with Microsoft Copilot Studio (`x-ms-agentic-protocol: mcp-streamable-1.0`) and Microsoft Foundry.
"""

from typing import Any, Dict, List


class TreyResearchMCPServer:
    """
    Self-contained MCP Server exposing Tools and Resources for Copilot Studio and Microsoft Foundry.
    """

    def list_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "generate_certification_study_plan",
                "description": (
                    "Generates a structured 3-month (12-week) Microsoft certification study plan "
                    "for Exam AB-100 or Exam AI-102 using official Microsoft Learn modules, "
                    "weighted toward the learner's weakest exam domain."
                ),
                "inputSchema": {
                    "type": "object",
                    "required": ["exam_code", "hours_per_week", "weakest_domain"],
                    "properties": {
                        "exam_code": {
                            "type": "string",
                            "enum": ["AB-100", "AI-102"],
                            "description": "Target Microsoft certification exam code (AB-100 or AI-102).",
                        },
                        "hours_per_week": {
                            "type": "integer",
                            "description": "Number of study hours available per week (for example, 8).",
                        },
                        "weakest_domain": {
                            "type": "string",
                            "enum": ["Plan", "Design", "Deploy"],
                            "description": "The domain where the learner needs extra hands-on practice.",
                        },
                    },
                },
            },
            {
                "name": "check_realtime_erp_stock",
                "description": (
                    "Queries real-time warehouse stock levels, reserved units, and restock lead time "
                    "in days for a specific product SKU in Trey Research ERP. Use this tool instead "
                    "of static knowledge search whenever live inventory availability is requested."
                ),
                "inputSchema": {
                    "type": "object",
                    "required": ["sku"],
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Exact Stock Keeping Unit identifier (for example, SKU-QUANTUM-09).",
                        }
                    },
                },
            },
        ]

    def list_resources(self) -> List[Dict[str, Any]]:
        return [
            {
                "uri": "trey://governance/mcp-security-standards",
                "name": "Trey Research MCP Security & DLP Standards",
                "mimeType": "text/markdown",
                "description": "Mandatory authentication, DLP endpoint filtering, and tool description standards for MCP servers.",
            }
        ]

    def read_resource(self, uri: str) -> Dict[str, Any]:
        if uri == "trey://governance/mcp-security-standards":
            return {
                "uri": uri,
                "mimeType": "text/markdown",
                "text": (
                    "# Trey Research MCP Governance Standard\n"
                    "1. Every MCP server must authenticate via Microsoft Entra ID OAuth 2.0 (OBO) or Managed Identity.\n"
                    "2. Register the MCP host in Power Platform DLP Endpoint Filtering allowlist.\n"
                    "3. Write distinct, non-overlapping tool descriptions for Generative Orchestration."
                ),
            }
        raise ValueError(f"Unknown MCP resource URI: {uri}")

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if name == "generate_certification_study_plan":
            exam = arguments.get("exam_code", "AB-100")
            hours = int(arguments.get("hours_per_week", 8))
            weakest = arguments.get("weakest_domain", "Deploy")

            if exam == "AB-100":
                roadmap = [
                    {
                        "month": "Month 1 (Weeks 1-4): Domain 1 - Plan AI-Powered Business Solutions (25-30%)",
                        "ms_learn_modules": [
                            "Module 01: Introduction to agentic AI business solutions",
                            "Module 02: Analyze requirements for AI-powered business solutions",
                            "Module 03: Design overall AI strategy for business solutions (CAF & AI CoE)",
                            "Module 04: Evaluate costs and benefits of AI solutions (TCO, ROI & Model Router)",
                        ],
                        "allocated_hours": hours * 3 if weakest != "Plan" else hours * 5,
                    },
                    {
                        "month": "Month 2 (Weeks 5-8): Domain 2 - Design AI-Powered Business Solutions (25-30%)",
                        "ms_learn_modules": [
                            "Module 05: Design AI agents for business solutions (Copilot Studio, D365, Foundry Tools)",
                            "Module 06: Design extensibility of AI solutions (MCP, Computer Use, Voice & Reasoning Mode)",
                            "Module 07: Orchestrate configuration of prebuilt agents and apps (D365 F&O & CE)",
                        ],
                        "allocated_hours": hours * 4 if weakest != "Design" else hours * 5,
                    },
                    {
                        "month": "Month 3 (Weeks 9-12): Domain 3 - Deploy AI-Powered Business Solutions (40-45%)",
                        "ms_learn_modules": [
                            "Module 08: Monitor, analyze, and tune AI agents (App Insights, Foundry Evaluators)",
                            "Module 09: Manage testing AI-powered business solutions (Copilot Studio Kit, RSAT)",
                            "Module 10: Design ALM process for AI-powered business solutions (Managed Solutions, CI/CD)",
                            "Module 11: Design responsible AI security, governance, risk management, and compliance",
                        ],
                        "allocated_hours": hours * 5 if weakest == "Deploy" else hours * 4,
                    },
                ]
            else:
                roadmap = [
                    {
                        "month": "Month 1 (Weeks 1-4): Azure AI Services, Vision & Document Intelligence",
                        "ms_learn_modules": [
                            "Plan and manage an Azure AI solution",
                            "Analyze images with Azure AI Vision",
                            "Extract data from forms with Azure Document Intelligence",
                        ],
                        "allocated_hours": hours * 4,
                    },
                    {
                        "month": "Month 2 (Weeks 5-8): NLP, Speech, Translator & Azure AI Search (RAG)",
                        "ms_learn_modules": [
                            "Build a Conversational Language Understanding (CLU) model",
                            "Create speech-enabled apps with Azure AI Speech",
                            "Implement knowledge mining with Azure AI Search",
                        ],
                        "allocated_hours": hours * 4,
                    },
                    {
                        "month": "Month 3 (Weeks 9-12): Generative AI & Agentic Solutions in Microsoft Foundry",
                        "ms_learn_modules": [
                            "Build generative AI solutions with Azure OpenAI in Microsoft Foundry",
                            "Develop AI agents with Microsoft Foundry Agent Service & Semantic Kernel",
                            "Evaluate and secure generative AI models with Azure AI Content Safety",
                        ],
                        "allocated_hours": hours * 4,
                    },
                ]

            return {
                "exam_code": exam,
                "duration": "3 Months (12 Weeks)",
                "weekly_commitment_hours": hours,
                "priority_focus_domain": weakest,
                "study_plan": roadmap,
            }

        if name == "check_realtime_erp_stock":
            sku = arguments.get("sku", "UNKNOWN")
            inventory_db = {
                "SKU-QUANTUM-09": {"available_units": 142, "reserved_units": 18, "warehouse": "Seattle-DC1", "restock_lead_days": 3},
                "SKU-SENSOR-44": {"available_units": 0, "reserved_units": 12, "warehouse": "Frankfurt-DC2", "restock_lead_days": 14},
            }
            record = inventory_db.get(
                sku,
                {"available_units": 25, "reserved_units": 2, "warehouse": "Atlanta-DC3", "restock_lead_days": 5},
            )
            return {"sku": sku, "status": "InStock" if record["available_units"] > 0 else "Backordered", **record}

        raise ValueError(f"Unknown MCP tool: {name}")
