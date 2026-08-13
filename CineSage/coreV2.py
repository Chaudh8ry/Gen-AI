# Structured Output Prompt
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

prompt = ChatPromptTemplate.from_messages(
    [('system',"""
Extract mvie information from the paragraph 
{format_instructions}
"""),('human',"""{paragraph}""")]
)

# """Interstellar is a visually stunning science fiction epic directed by Christopher Nolan Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity as Earth faces environmental collapse. The movie was widely appreciated for its emotional depth, scientific accuracy, and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb and is often considered one of the greatest sci-fi films of the 21st century."""

para = input("Give Movie Description: ")

final_prompt = prompt.invoke(
    {"paragraph": para,
     'format_instructions':parser.get_format_instructions}
)

response = model.invoke(final_prompt)

print(response.text)