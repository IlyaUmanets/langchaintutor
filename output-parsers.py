from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

model = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)

def call_string_output_parser():
  prompt = ChatPromptTemplate.from_messages([
    ("system", "tell me a joke about the following subject."),
    ("human", "{input}")
  ])

  parser = StrOutputParser()
  chain = prompt | model | parser

  return chain.invoke({"input": "dog"})

# print(call _string_output_parser())
def call_list_output_parser():
  prompt = ChatPromptTemplate.from_messages([
    ("system", "generate a list of 10 synonyms for the following word. Return the results as a comma seperated list."),
    ("human", "{input}")
  ])

  parser = CommaSeparatedListOutputParser()
  chain = prompt | model | parser

  return chain.invoke({"input": "happy"})

def call_json_output_parser():
  prompt = ChatPromptTemplate.from_messages([
    ("system", "extract information from the following phrase. \nFormatting Instructions: {format_instructions}"),
    ("human", "{phrase}")
  ])

  class Person(BaseModel):
    name: str = Field(description="The name of recipe")
    ingredients: list = Field(description="ingredients")

  parser = JsonOutputParser(pydantic_object=Person)

  chain = prompt | model | parser

  return chain.invoke({
    "phrase": "the ingrediends for a Margarita are tequila, triple sec, and lime juice.",
    "format_instructions": parser.get_format_instructions()
  })


print(call_json_output_parser())
