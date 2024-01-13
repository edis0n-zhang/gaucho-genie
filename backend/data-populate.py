import requests
import json
import os
from dotenv import load_dotenv

# load .env file and retrieve API key
load_dotenv()
api_key = os.getenv('UCSB_API_KEY')

# API call to retrieve data
url = "https://api.ucsb.edu/academics/curriculums/v3/classes/search?quarter=20241&pageNumber=1&pageSize=10&includeClassSections=true"
headers = {
    "accept": "application/json",
    "ucsb-api-version": "3.0",
    "ucsb-api-key": api_key,
}

response = requests.get(url, headers=headers)
formatted_json = json.dumps(response.json(), indent=4)

# Specify the file name
file_name = "response_data.txt"

# Write the formatted JSON to the file
with open(file_name, 'w') as file:
    file.write(formatted_json)

print(f"Data saved to {file_name}")
