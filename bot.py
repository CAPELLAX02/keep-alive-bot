import requests
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("BACKEND_URL")

def fetch_data():
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            print(f"GET request successfull: {response.json()}")
        else:
            print(f"GET request failed. HTTP Status: {response.status_code}")
    except Exception as e:
        print(f"Something went wrong: {e}")

# schedule.every(5).seconds.do(fetch_data)
schedule.every(10).minutes.do(fetch_data)

print("Bot started. Sending GET request in every 10 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)