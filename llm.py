from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
  model="gpt-4-turbo",
  temperature=0.7,
  max_tokens=100,
  verbose=True
)

response = llm.stream("Hello, how are you?")
# print(response)
for chunk in response:
  print(chunk.content, end="", flush=True)