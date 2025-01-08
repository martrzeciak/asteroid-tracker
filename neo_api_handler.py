import requests
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# NASA API Key (from .env for security)
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Base URL as a constant
BASE_URL = os.getenv("NEO_API_BASE_URL")

def fetch_asteroid_data(start_date=None, end_date=None):
    if not start_date:
        start_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if not end_date:
        end_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": NASA_API_KEY,
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Unable to fetch data, Status Code: {response.status_code}")