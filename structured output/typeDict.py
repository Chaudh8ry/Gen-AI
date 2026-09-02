# Creating structured output using TypeDict: 
# TypedDict is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# Literal restricts values to specific strings
# Annotated allows us to add descriptions/instructions for each field
# Optional means the field can be None (not always required)
from typing import TypedDict, Literal, Annotated, Optional

# making the schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"],"Return the sentiment of the review"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# Wrap the model with structured output enforcement using our Review schema
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh""")

print(result)

# Example: Access specific fields from the structured output
# print("Summary: ", result['summary'])
# print("Sentiment: ", result['sentiment'])