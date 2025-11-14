import os
from pathlib import Path
from google import genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv

# Always load .env from project root
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

def get_client():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("❌ GOOGLE_API_KEY missing in .env")
    return genai.Client(api_key=key)

def ask_json(prompt: str, schema: dict):
    """
    Sends a structured request to Gemini and expects JSON output following the given schema.
    """
    client = get_client()

    cfg = GenerateContentConfig(
        temperature=0.2,
        response_mime_type="application/json",
        response_schema=schema,
    )

    # Use the stable and available model
    result = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt,
        config=cfg
    )

    return result.text  # Already JSON per config
