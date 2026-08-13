from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

prompt = ChatPromptTemplate.from_messages([("system", """
You are an information extraction assistant specialized in analyzing movie descriptions.

Your task is to read the given movie description and extract all useful and relevant information from it.

Extract the following information:

- Movie Name
- Release Year
- Director
- Genre(s)
- Main Cast
- Plot / Story
- Setting or Main Location (if mentioned)
- Main Theme(s)
- IMDb Rating (if mentioned)
- Music / Composer (if mentioned)
- Critical Reception
- Awards or Achievements (if mentioned)
- Notable Facts
- Overall Sentiment / Reception
- Short Summary
"""),
("human","""
1. Extract information only from the provided text.
2. Do not invent or assume information that is not explicitly mentioned.
3. If a piece of information is not available, write "Not mentioned".
4. For genres, provide a list of relevant genres.
5. For cast, include the actor's name and character name only if the character name is mentioned.
6. Keep the Plot / Story concise while preserving the important details.
7. The Short Summary should be 2-3 sentences and give a quick understanding of what the movie is about and how it was received.
8. Keep the extracted information clear, concise, and easy to read.
9. Separate factual information from opinions or critical reception.
10. Do not include unnecessary details or repeat the same information multiple times.

Movie Description:

{movie_description}
""")]
)

# """Interstellar is a visually stunning science fiction epic directed by Christopher Nolan Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity as Earth faces environmental collapse. The movie was widely appreciated for its emotional depth, scientific accuracy, and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb and is often considered one of the greatest sci-fi films of the 21st century."""

paragraph = input("Give Movie Description: ")

final_prompt = prompt.invoke(
    {"movie_description": paragraph}
)

response = model.invoke(final_prompt)

print(response.text)