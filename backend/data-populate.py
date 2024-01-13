import requests
import json
import os
from dotenv import load_dotenv

# load .env file and retrieve API key
load_dotenv()
api_key = os.getenv('UCSB_API_KEY')

# Pull CSV of Subject Codes and break into list
file = open('subject_codes.csv', 'r')
subject_codes = file.read().split(', ')

print(subject_codes)
quarters = ["20221", "20222", "20223", "20224", "20231", "20232", "20233", "20234", "20241"]

# print(f"subject codes: {subject_codes}")
for quarter in quarters:
    for subject_code in subject_codes:
        # API call to retrieve data
        url = f"https://api.ucsb.edu/academics/curriculums/v3/classes/search?quarter={quarter}&subjectCode={subject_code}&objLevelCode=U&pageNumber=1&pageSize=100&includeClassSections=true"
        headers = {
            "accept": "application/json",
            "ucsb-api-version": "3.0",
            "ucsb-api-key": api_key,
        }

        response = requests.get(url, headers=headers)
        formatted_json = json.dumps(response.json(), indent=4)

        # if folder doesn't exist, create it
        if not os.path.exists(f"{quarter}-classes"):
            os.makedirs(f"{quarter}-classes")

        # Create file name
        file_name = f"{quarter}-classes/{subject_code}.json"
        print(file_name)

        if not os.path.exists(file_name):
            mode = 'w'  # Create a new file if it doesn't exist
        else:
            mode = 'a'  # Append to the file if it already exists

        # Write the formatted JSON to the file
        with open(file_name, mode) as file:
            file.write(formatted_json)

        print(f"File created successfully: {file_name}")
