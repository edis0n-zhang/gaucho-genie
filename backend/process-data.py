import json
import openai
import pinecone
import requests
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Pinecone

# load .env file and retrieve API key
load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Pinecone setup
pinecone.init(PINECONE_API_KEY, environment='gcp-starter')
index_name = "gaucho-genie"

# Create a new Pinecone index or connect to an existing one
index = pinecone.Index(index_name)

# Variables for the loop
quarters = ["20241"]
file = open('subject_codes.csv', 'r')
subject_codes = file.read().split(', ')

# limit string length to reduce metadata size
def limit_string_length(input_string, max_length):
    if len(input_string) > max_length:
        return input_string[:max_length]
    return input_string

# convert quarter code to string for better readability
def quarter_code_to_string(quarter_code):
    year = str(quarter_code[:4])
    quarter_season = str(quarter_code[4])

    if quarter_season == "1":
        quarter_season = "Winter"
    elif quarter_season == "2":
        quarter_season = "Spring"
    elif quarter_season == "3":
        quarter_season = "Summer"
    elif quarter_season == "4":
        quarter_season = "Fall"

    return f"{year} {quarter_season}"

# load course difficulty data from csv and make dictionary
file = open('course_difficulty_ratings.csv', 'r')
course_difficulty = {}

for line in file:
    line = line.split(',')
    key = " ".join(line[0].split())
    value = line[1].strip()
    course_difficulty[key] = value

# Load the JSON data
for quarter in quarters:
    for subject in subject_codes:
        with open(f"{quarter}-classes/{subject}.json", 'r') as file:
            data = json.load(file)

        classes = data.get("classes", [])

        for class_info in classes:
            quarter_string = quarter_code_to_string(quarter)
            courseId = " ".join(class_info['courseId'].split())
            title = str(class_info['title'])
            description = str(class_info['description'])
            college = str(class_info['college'])
            subjectArea = str(class_info['subjectArea'].strip())
            unitsFixed = str(class_info['unitsFixed'])
            deptCode = str(class_info['deptCode'].strip())
            generalEducation = str(class_info['generalEducation'])

            # dump json into a string
            class_string = f"""{courseId} {quarter_string} Overview:
            The course is titled {title}.
            It is offered by the {college} college and is in the {subjectArea} subject area.
            It is worth {unitsFixed} units and is in the {deptCode} department.
            It offers the following general education credits: {generalEducation}.
            Please refer to the key when interpreting the general education credits.
            The course description is as follows: {description}
            The course difficulty is {course_difficulty.get(courseId, "not found")}.
            """

            # get embedding for class_string
            embedding = embeddings.embed_query(class_string)

            # Ensure embedding length matches Pinecone index's dimension
            assert len(embedding) == 1536, f"Embedding length does not match Pinecone index dimension {len(embedding)}"

            # Prepare the data for Pinecone (id, vector pair)
            vector_id = f"{' '.join(class_info['courseId'].split())} {quarter}"  # Assuming courseId is unique and used as ID
            print(vector_id)

            # Metadata def
            metadata = {
                "quarter": quarter,
                "courseId": courseId,
                "title": title,
                "description": description,
                "college": college,
                "subjectArea": subjectArea,
                "unitsFixed": unitsFixed,
                "deptCode": deptCode,
                "generalEducation": generalEducation,
                "text" : class_string
            }

            # Perform the upsert operation
            index.upsert(vectors=[{
                "id" : vector_id,
                "values" : embedding,
                "metadata" : metadata
            }])
