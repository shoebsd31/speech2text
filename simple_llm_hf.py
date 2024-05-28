import os
#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub

# Set up the environment with the respective API key
#os.environ["OPENAI_API_KEY"] = "" # if you are using OpenAI

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "" # The access token goes here

# Choose between different LLM models

# The "temperature" is a hyperparameter that influences the randomness of the model's output. A lower value (like 0.1) yields more deterministic output, while a higher value results in more randomness.
# The "max_new_tokens" parameter sets a limit on the maximum number of new tokens (words/characters) that the model can generate as output.

llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct",model_kwargs={"temperature": 0.1, "max_new_tokens": 600})

# You can also use OpenAI GPT models
#llm = OpenAI(model_name="gpt-3.5-turbo")

#insert your input
text = "How to read a book effectively?"

output = llm(text)
print(output)