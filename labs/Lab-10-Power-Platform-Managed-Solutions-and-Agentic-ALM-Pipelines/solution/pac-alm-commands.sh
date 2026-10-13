#!/usr/bin/env bash
# ==============================================================================
# AB-100 Lab 10 Solution: Power Platform CLI (`pac`) Agentic ALM Automation
# Converts an Unmanaged Development Solution (Canvas App + Copilot Studio Agent
# + AI Builder Flow + Dataverse Table) into Source Control & a Managed Solution
# ==============================================================================
set -euo pipefail

SOLUTION_NAME="FabrikamAgenticCustomerOperations"
DEV_ENV_URL="https://fabrikam-dev.crm.dynamics.com"
UAT_ENV_URL="https://fabrikam-uat.crm.dynamics.com"
PROD_ENV_URL="https://fabrikam-prod.crm.dynamics.com"

echo "[Step 1] Authenticating to Development Environment using Service Principal..."
pac auth create --name "Fabrikam-Dev" --url "${DEV_ENV_URL}" --applicationId "${CLIENT_ID}" --clientSecret "${CLIENT_SECRET}" --tenant "${TENANT_ID}"

echo "[Step 2] Publishing all customizations in Development..."
pac solution publish

echo "[Step 3] Exporting Unmanaged Solution (for Git unpacking) and Managed Solution (for validation)..."
pac solution export --name "${SOLUTION_NAME}" --path "./artifacts/${SOLUTION_NAME}_unmanaged.zip" --managed false --overwrite
pac solution export --name "${SOLUTION_NAME}" --path "./artifacts/${SOLUTION_NAME}_managed.zip" --managed true --overwrite

echo "[Step 4] Unpacking Solution into Git-friendly source files (including Copilot Studio .mcs.yml topics)..."
pac solution unpack --zipfile "./artifacts/${SOLUTION_NAME}_unmanaged.zip" --folder "./src/solutions/${SOLUTION_NAME}" --packagetype Both --allowDelete true

echo "[Step 5] Running Power Platform Solution Checker static analysis gate..."
pac solution check --path "./artifacts/${SOLUTION_NAME}_managed.zip" --outputDirectory "./artifacts/checker-results"

echo "[Step 6] Packing source files into an immutable Managed Solution artifact..."
pac solution pack --zipfile "./artifacts/${SOLUTION_NAME}_packed_managed.zip" --folder "./src/solutions/${SOLUTION_NAME}" --packagetype Managed

echo "[Step 7] Generating template deployment-settings.json for Environment Variables & Connection References..."
pac solution create-settings --solution-zip "./artifacts/${SOLUTION_NAME}_packed_managed.zip" --settings-file "./config/uat-deployment-settings.json"

echo "[Step 8] Importing Managed Solution into UAT Environment with Environment Variables & Connection References..."
pac auth create --name "Fabrikam-UAT" --url "${UAT_ENV_URL}" --applicationId "${CLIENT_ID}" --clientSecret "${CLIENT_SECRET}" --tenant "${TENANT_ID}"
pac solution import --path "./artifacts/${SOLUTION_NAME}_packed_managed.zip" --settings-file "./config/uat-deployment-settings.json" --activate-plugins true --force-overwrite true

echo "[Complete] Managed Solution successfully promoted to UAT!"
