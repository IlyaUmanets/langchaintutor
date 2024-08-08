from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Instantiate the model
llm = ChatOpenAI(
  temperature=0.7,
  model="gpt-4-turbo"
)

# Prompt template

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "generate a list of 10 synonyms for the following word. Return the results as a comma seperated list."),
    ("human", "{input}")
  ]
)

# Create LLM Chain
chain = prompt | llm

response = chain.invoke({"input": "happy"})
print(type(response.content))

