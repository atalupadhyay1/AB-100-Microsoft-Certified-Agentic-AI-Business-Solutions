#!/usr/bin/env python3
"""
AB-100 Lab 06 Solution: Predictive AI Services (Microsoft Foundry Tools)
Demonstrates unified pre-processing & post-processing via a single AI Services endpoint:
1. Azure AI Language: PII Detection & Redaction (before sending text to an LLM or KB index).
2. Azure AI Translator: Multilingual Translation with Custom Terminology Glossary.
3. Azure AI Speech: Voice Mode SSML formatting for natural telephony synthesis.
"""

import re
from typing import Dict, List, Tuple


def redact_pii_azure_ai_language(raw_text: str) -> Tuple[str, List[Dict[str, str]]]:
    """
    Simulates Azure AI Language PII Redaction (`kind: PiiEntityRecognition`).
    """
    detected_entities = []
    redacted = raw_text

    patterns = [
        ("US_SSN", r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]"),
        ("Email", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[REDACTED_EMAIL]"),
        ("PhoneNumber", r"\b\d{3}-\d{3}-\d{4}\b", "[REDACTED_PHONE]"),
        ("PatientMRN", r"\bMRN-\d{6}\b", "[REDACTED_MRN]"),
    ]
    for category, regex, mask in patterns:
        for match in re.finditer(regex, redacted):
            detected_entities.append({"category": category, "text": match.group(0), "mask": mask})
        redacted = re.sub(regex, mask, redacted)

    return redacted, detected_entities


def translate_with_custom_glossary(redacted_text: str, target_lang: str = "de") -> str:
    """
    Simulates Azure AI Translator with Custom Translator glossary preservation.
    """
    if target_lang == "de":
        return (
            "[DE - Azure AI Translator] Patientendatensatz [REDACTED_MRN] meldete leichte Kopfschmerzen "
            "nach Einnahme von ContosoCardioPlus. Kontakt unter [REDACTED_PHONE] oder [REDACTED_EMAIL]."
        )
    return redacted_text


def build_azure_ai_speech_ssml(case_code: str, spoken_message: str) -> str:
    """
    Generates Azure AI Speech SSML for Copilot Studio Voice Mode / Contact Center IVR.
    Uses <say-as interpret-as="characters"> so alphanumeric IDs are spoken clearly.
    """
    return f"""<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
  <voice name="en-US-AvaMultilingualNeural">
    <prosody rate="1.0" pitch="0%">
      Thank you for calling Contoso Pharmaceuticals Medical Information Desk.
      Your adverse event reference code is <say-as interpret-as="characters">{case_code}</say-as>.
      <break time="400ms"/>
      {spoken_message}
    </prosody>
  </voice>
</speak>"""


if __name__ == "__main__":
    print("=" * 86)
    print("AB-100 LAB 06: PREDICTIVE AI SERVICES (MICROSOFT FOUNDRY TOOLS) PIPELINE")
    print("=" * 86)

    sample_clinical_note = (
        "Patient record MRN-492810 (SSN 412-88-9012) reported mild headache after taking "
        "ContosoCardioPlus. Follow up at 206-555-0199 or patient.jane@example.com."
    )
    print(f"\n[1] Raw Input Text:\n  {sample_clinical_note}")

    redacted_text, entities = redact_pii_azure_ai_language(sample_clinical_note)
    print(f"\n[2] Azure AI Language PII Redaction Output (Safe for Grounding/LLM):\n  {redacted_text}")
    print(f"    Detected PII Entities ({len(entities)}): {entities}")

    translated = translate_with_custom_glossary(redacted_text, target_lang="de")
    print(f"\n[3] Azure AI Translator Output (German Regulatory Filing):\n  {translated}")

    ssml_payload = build_azure_ai_speech_ssml(
        case_code="AE9042",
        spoken_message="A clinical safety specialist has been notified and will review your report.",
    )
    print(f"\n[4] Azure AI Speech SSML Payload (for Voice Mode / Contact Center):\n{ssml_payload}")
    print("=" * 86)
