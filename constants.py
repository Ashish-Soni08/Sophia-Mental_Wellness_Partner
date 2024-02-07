from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(config)
# API KEYS, URLS, TOKENS, ETC

# ## Anyscale Endpoints
# ANYSCALE_API_KEY: str = config["ANYSCALE_API"]

## Hugging Face
HF_API_KEY: str = config["HF_API"] # Read
HF_TOKEN: str = config["HF_TOKEN"] # Write

## LangChain(langsmith)
LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]

## Pinecone
PINECONE_API_KEY: str = config["PINECONE_API"]