from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_community.chat_message_histories.upstash_redis import UpstashRedisChatMessageHistory
import os

history = UpstashRedisChatMessageHistory(
  url=os.getenv("REDIS_UPSTASH_URL"),
  token=os.getenv("REDIS_UPSTASH_TOKEN"),
  session_id="chat1", # should be a uniq ID for each conversation,
  ttl=360
)

model = ChatOpenAI(
  model = "gpt-3.5-turbo-0125",
  temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are friendly AI assistant"),
  MessagesPlaceholder(variable_name="chat_history"),
  ("human", "{input}")
])

memory = ConversationBufferMemory(
  memory_key="chat_history",
  return_messages=True,
  chat_memory=history
)

chain = LLMChain(
  llm=model,
  prompt=prompt,
  memory=memory,
  verbose=True
)

msg2 = {
  "input": "what is my name"
}
response2 = chain.invoke(msg2)
print(response2)
