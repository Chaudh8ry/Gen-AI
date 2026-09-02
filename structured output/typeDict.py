# Creating structured output using TypeDict: 
# TypedDict is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict

# making the schema
class Review(TypedDict):
    summary: str
    sentiment: str

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also the UI looks Outdated")

print("Summary: ",result['summary'])
print("Sentiment: ",result['sentiment'])