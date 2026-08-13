# Structured Output Prompt

# Load environment variables from a .env file (e.g., API keys, secrets)
from dotenv import load_dotenv
load_dotenv()

# Import the Gemini chat model wrapper from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Import LangChain's prompt template utility
from langchain_core.prompts import ChatPromptTemplate

# Import Pydantic for defining structured data models (Movie schema here)
from pydantic import BaseModel

# Typing helpers for optional values and lists
from typing import List, Optional

# Import LangChain's parser that converts raw LLM output into Pydantic objects
from langchain_core.output_parsers import PydanticOutputParser


# Define a Movie schema using Pydantic
# This enforces structure: title must be str, release_year optional int, etc.
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# Create a parser that knows how to validate/convert model output into Movie objects
parser = PydanticOutputParser(pydantic_object=Movie)

# Initialize Gemini model (flash-lite version, optimized for speed)
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# Build a prompt template with system + human roles
# System: tells the model what to do (extract movie info in structured format)
# Human: provides the actual paragraph input
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', """
Extract movie information from the paragraph 
{format_instructions}
"""),
        ('human', """{paragraph}""")
    ]
)

# Example movie description (commented out for testing)
# para = "Interstellar is a visually stunning science fiction epic directed by Christopher Nolan..."

# Take user input for movie description
para = input("Give Movie Description: ")

# Fill the prompt template with actual values:
# - paragraph: user input
# - format_instructions: JSON schema instructions from parser
final_prompt = prompt.invoke(
    {
        "paragraph": para,
        "format_instructions": parser.get_format_instructions()
    }
)

# Send the prompt to Gemini model and get raw response
response = model.invoke(final_prompt)

# Print raw model output (usually JSON string)
print("Raw Model Output: ")
print(response.text)

print("\n")

# Parse raw JSON into structured Python object (Movie instance)
print("Structured Output: ")
movie_data = parser.parse(response.text)
print(movie_data)  # Default print shows field=value style
