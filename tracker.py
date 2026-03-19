import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# YouTube API key
API_KEY = "AIzaSyCyE7_90eTzXOq-j38cVA2I7tptYnkSsa4"

# Video ID
VIDEO_ID = "QV10FTozMSk"

# Google Sheet ID
SHEET_ID = "1mX1ijnuB2fypPv7bzeGiafk8TblTqwjI04vY9toswc4"

# JSON file name
SERVICE_FILE = "buoyant-yew-451605-n6-d38a101e95c7.json"

# Google Sheet connection
scope = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(SERVICE_FILE, scopes=scope)

client = gspread.authorize(creds)

sheet = client.open_by_key(SHEET_ID).sheet1

# YouTube API call
url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"

response = requests.get(url).json()

views = response["items"][0]["statistics"]["viewCount"]

time_now = datetime.now().strftime("%H:%M:%S")

# Append data to sheet
sheet.append_row([time_now, views])

print("Data added:", time_now, views)
