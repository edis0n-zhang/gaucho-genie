from langchain.vectorstores.pinecone import Pinecone
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import pinecone
import os

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment="gcp-starter",  # next to api key in console
)

index_name = "gaucho-genie"

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

index = pinecone.Index(index_name)

docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = input()

result = docsearch.similarity_search(query)

print(result)

def prepare_data_for_llm(query, results):
    if not results:
        return f"Query: {query}\n\nNo results found."

    response_prompt = f"Query: {query}\n\nResults:\n {results}"

    return response_prompt

response_prompt = prepare_data_for_llm(query, result)

chat = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo-0613")

messages = [
    SystemMessage(
        content="""
        You are a helpful course planning assistant at UCSB.
        You are given a query and a list containing important information formatted as such 'ID: {id} Info: {metadata}'.
        Provide a response to the query using the information provided.

        If the information is a course here is helpful information on how it is formatted, use this to help you generate a better response:

        Course ID's are formatted as the following:
        SUBJECT_ID COURSE_NUMBER
        For example : CMPSC 8 is the course ID for Intro to Computer Science.

        Course ID's lower than 100 are lower division undergraduate courses and 1xx courses are upper division undergraduate courses.

        General education codes are formatted as the following:
        geCollege is the college the general education requirement is for (e.g L&S is the College of Letters and Science and ENGR is the College of Engineering)
        geCode is the code for the general education requirement
        geCode meanings:
            A - English Reading and Composition
            B - Foreign Language
            C - Science, Mathematics, and Technology
            D - Social Science
            E - Culture and Thought
            F - Arts
            G - Literature
            EUR - European Traditions
            WRT - Writing
            NWC - World Cultures
            QNT - Quantitative Relationships
            ETH - Ethnicity

        The course difficulty is rated on a scale of 1-10 with 1 being the easiest and 10 being the hardest.
        When giving a response and including course difficulty, round to the nearest integer.
        You should factor the Course ID level into the difficulty, the higher the number the more difficult the class likely is.

        The course data is formatted as such:
        {courseId} {quarter_string} Overview:
        The course is titled {title}.
        It is offered by the {college} college and is in the {subjectArea} subject area.
        It is worth {unitsFixed} units and is in the {deptCode} department.
        It offers the following general education credits: {generalEducation}.
        Please refer to the key when interpreting the general education credits.
        The course description is as follows: {description}
        The course is {difficuty}.
        """
    ),
    HumanMessage(
        content=f"{query} \n\n Please answer by utilizing the information provided: \n\n {response_prompt}"
    ),
]

res = chat(messages)

print(res)
