from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

# API KEYS, URLS, TOKENS, ETC

# Hugging Face
HUGGINGFACE_API_KEY: str = config["HF_API"] # Read
HF_TOKEN: str = config["HF_TOKEN"] # Write