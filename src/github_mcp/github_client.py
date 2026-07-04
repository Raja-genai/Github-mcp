import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

BASE_URL = "https://api.github.com"