import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY: Final[str] = os.getenv("GOOGLE_API_KEY", "")

BACKEND_AGENT_A2A_URL: Final[str] = os.getenv("BACKEND_AGENT_A2A_URL", "http://localhost:8001")

BACKEND_URL: Final[str] = os.getenv("BACKEND_URL", '')

ADK_MODEL: Final[str] = os.getenv("ADK_MODEL", 'gemini-2.5-flash') 