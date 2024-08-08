# langchaintutor
A langchain code I wrote while passing YouTube tutorial - https://www.youtube.com/watch?v=ekpnVh-l3YA&t=1s

# Installation

Rename `.env.example` to `.env`

## Required Environment variables

OpenAI - https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key
- `OPENAI_API_KEY` 

Langchain - https://docs.smith.langchain.com/how_to_guides/setup/create_account_api_key
- `LANGCHAIN_API_KEY` 
- `LANGCHAIN_TRACING_V2`
- `LANGCHAIN_ENDPOINT`
- `LANGCHAIN_PROJECT`

Tavily - https://docs.tavily.com/docs/tavily-api/python-sdk

- `TAVILY_API_KEY`

Upstash - https://upstash.com/docs/introduction
- `REDIS_UPSTASH_URL` 
- `REDIS_UPSTASH_TOKEN`

## Required packages

```sh
  pip install langchain
  pip install langchain-cli
  pip install langchain_community
  pip install python-dotenv
  pip install faiss-cpu
  pip install upstash_redis
```

## Here's an example of usage

<img width="1459" alt="Screenshot 2024-08-08 at 12 41 28" src="https://github.com/user-attachments/assets/da70b41e-5845-459d-b618-ae72173c67f4">
