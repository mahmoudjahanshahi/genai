# pylint: disable=all
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure Azure OpenAI service client 
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key = os.environ['AZURE_OPENAI_API_KEY'],  
  api_version = os.environ['AZURE_OPENAI_API_VERSION']
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
prompt = "Complete the following: Once upon a time there was an old dog in a cave."
behavior = "you are a persian poet."
messages = [{"role": "user", "content": prompt}, {"role": "system", "content": behavior}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.