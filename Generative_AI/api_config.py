import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# Find project root (where .env lives)
root_dir = Path(__file__).resolve().parent.parent
env_path = root_dir / '.env'

# Load .env from root if it exists
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "your_groq_api_key_here":
    raise ValueError("GROQ_API_KEY not found or still set to placeholder. Please check your .env file.")

client = Groq(api_key=api_key)