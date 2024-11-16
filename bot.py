import requests
import schedule
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read URL from .env
url = os.getenv("BACKEND_URL")

# Check if URL is correctly loaded
if not url:
    raise ValueError("Environment variable 'BACKEND_URL' not set in .env")

def fetch_data():
    print("Sending GET request...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET request successful: {response.json()}")
        else:
            print(f"GET request failed. HTTP Status: {response.status_code}")
    except Exception as e:
        print(f"Something went wrong: {e}")

# Schedule task every 10 minutes
schedule.every(10).minutes.do(fetch_data)

print("Bot started. Sending GET request every 10 minutes...")

# Infinite loop to keep the bot running
while True:
    schedule.run_pending()
    time.sleep(1)
