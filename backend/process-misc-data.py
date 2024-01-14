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

for file in os.listdir(f"misc_info"):
    fileName, _ = os.path.splitext(file)  # Extract file name without extension
    with open(f"misc_info/{file}", 'r') as file:
        print(fileName)
        data = str(file.read())
        embedding = embeddings.embed_query(data)
        metadata = {
            "type" : "misc_info",
            "name" : fileName,
            "text" : data
        }
        index.upsert(vectors=[{
            "id" : fileName,
            "values" : embedding,
            "metadata" : metadata
        }])
