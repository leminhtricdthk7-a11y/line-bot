import os
import requests

TOKEN = os.getenv("LINE_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "to": "GROUP_ID_HERE",
    "messages": [
        {"type": "text", "text": "Hello from GitHub Actions"}
    ]
}

requests.post(
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    json=data
)