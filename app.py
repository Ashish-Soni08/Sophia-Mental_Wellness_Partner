import os
from pprint import pprint

from constants import ANYSCALE_API_KEY

from llama_index.llms import Anyscale
from llama_index.llms import ChatMessage
from llama_index.llms.anyscale_utils import anyscale_modelname_to_contextsize

size = anyscale_modelname_to_contextsize("Meta-Llama/Llama-Guard-7b")
print(size)

## Meta
llama_guard = Anyscale(api_key = ANYSCALE_API_KEY, model = "Meta-Llama/Llama-Guard-7b")
pprint(llama_guard)



## Mistral AI
# llm = Anyscale(api_key = ANYSCALE_API_KEY, model = "mistralai/Mistral-7B-Instruct-v0.1")

# message = ChatMessage(role="user", content="What year is it?")
# resp = llm.chat([message])
# print(resp)