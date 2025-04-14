import os
import requests
from questions import get_question
from dotenv import load_dotenv

load_dotenv()

webhook = os.getenv("DISCORD_WEBHOOK")
question = get_question()

payload = {"content": f"📌 **Daily Question**\n\n{question}"}

try:
    response = requests.post(webhook, json=payload)
    if response.status_code == 204:
        print("✅ Question sent!")
    else:
        print(f"❌ Failed to send: {response.status_code} - {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")
