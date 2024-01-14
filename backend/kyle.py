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

def prepare_data_for_llm(query, results):
    if not results:
        return f"Query: {query}\n\nNo results found."

    response_prompt = f"Query: {query}\n\nResults:\n {results}"

    return response_prompt

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment="gcp-starter",  # next to api key in console
)

# Index and embeddings setup
index_name = "gaucho-genie"
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
index = pinecone.Index(index_name)
docsearch = Pinecone.from_existing_index(index_name, embeddings)

chat = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo-0613")

# Conversation history
conversation_history = []

while True:
    # Get user query
    query = input("Enter your query: ")

    # Perform similarity search
    result = docsearch.similarity_search(query)

    # Prepare data for language model
    response_prompt = prepare_data_for_llm(query, result)
    conversation_history.append(HumanMessage(content=f"{query} \n\n Please answer by utilizing the information provided: \n\n {response_prompt}"))

    

    # Generate system response
    messages = [
        # System's understanding of its role
        SystemMessage(content="""
           You are a helpful course planning assistant.
        You are given a query and a list containing important information formatted as such 'ID: {id} Info: {metadata}'.
        You must return the most relevant courses to the query as well as provide a short description based on the knowledge you have.

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

        The course data is formatted as such:
        {courseId} {quarter_string} Overview:
        The course is titled {title}.
        It is offered by the {college} college and is in the {subjectArea} subject area.
        It is worth {unitsFixed} units and is in the {deptCode} department.
        It offers the following general education credits: {generalEducation}.
        Please refer to the key when interpreting the general education credits.
        The course description is as follows: {description}
        The course is {difficuty}.
        """),
        *conversation_history  # Add all previous messages
    ]

    # Get response from chat model
    res = chat.invoke(messages)

    # Print and store the system response
    print(f"\n\nChatbot Response: {res.content}\n\n")
    conversation_history.append(SystemMessage(content=res.content))
    # Calculating the total length of the conversation history
    total_length = sum(len(message.content) for message in conversation_history)

    if total_length > 2000:
        
        # Create a text representation of the conversation history
        history_text = "\n".join([msg.content for msg in conversation_history])

        # Prepare the summarization prompt
        summarize_prompt = (
            "You are a helpful course planning assistant. "
            "I have a conversation history that needs to be summarized and the summary must be less than 2000 characters. "
            "Please keep track of the most recent courses that you have mentioned in the summary and the context of the conversation, especially more recent information. "
            "Important info to includes recent course codes mentioned and the order that you mentioned them. Do not forget those courses"
            "Be as detailed as possible but keep it under 2000 characters"
            "Here is the conversation history:\n\n" + history_text
        )

        # Call the chat model for summarization
        res2 = chat.invoke([SystemMessage(content=summarize_prompt)])
        conversation_history.clear()
        conversation_history.append(SystemMessage(content = res2.content))
        # Print the summarized history
        print("\n\nSummarized history\n\n")
        print(res2.content)

