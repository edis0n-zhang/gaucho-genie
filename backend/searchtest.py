from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import pinecone
import os

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Pinecone setup
pinecone.init(PINECONE_API_KEY, environment='gcp-starter')
index_name = "gaucho-genie"

# Create a new Pinecone index or connect to an existing one
index = pinecone.Index(index_name)

# Pinecone setup
pinecone.init(PINECONE_API_KEY, environment='gcp-starter')
index_name = "gaucho-genie"

# Create a new Pinecone index or connect to an existing one
index = pinecone.Index(index_name)

# Query the index
query = "Return the CMPSC courses with the lowest numbers"
xq = embeddings.embed_query(query)
# print(xq)
res = index.query([xq], top_k=5, include_metadata=True)

print(res)
