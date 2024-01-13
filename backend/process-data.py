import json
import openai
import pinecone
import requests

# Load the JSON data
with open("20241-classes/ANTH.json", 'r') as file:
    data = json.load(file)

classes = data.get("classes", [])

for class_info in classes:
    class_string = json.dumps(class_info, indent=4)
    print(class_string)
