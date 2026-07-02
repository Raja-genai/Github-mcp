import requests
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(
    "https://api.github.com/user/repos",
    headers=headers
)

print(response.status_code)

for repo in response.json():
    print(repo["name"])