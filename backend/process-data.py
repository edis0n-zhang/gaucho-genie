import json
import openai
import pinecone
import requests
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# load .env file and retrieve API key
load_dotenv()
pinecone_api_key = os.getenv('PINECONE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

embeddings = OpenAIEmbeddings()

# Pinecone setup
pinecone.init(pinecone_api_key, environment='gcp-starter')
index_name = "gaucho-genie"

# Create a new Pinecone index or connect to an existing one
index = pinecone.Index(index_name)

# Load the JSON data
with open("20241-classes/ANTH.json", 'r') as file:
    data = json.load(file)

classes = data.get("classes", [])

for class_info in classes:
    print("BEFORE")

    # dump json into a string
    class_string = json.dumps(class_info, indent=4)

    # get embedding for class_string
    embedding = embeddings.embed_query(class_string)

    # Ensure embedding length matches Pinecone index's dimension
    assert len(embedding) == 1536, f"Embedding length does not match Pinecone index dimension {len(embedding)}"

    # Prepare the data for Pinecone (id, vector pair)
    vector_id = class_info['courseId'].strip()  # Assuming courseId is unique and used as ID
    vector_data = (vector_id, embedding)

    # Perform the upsert operation
    index.upsert(vectors=[vector_data])
