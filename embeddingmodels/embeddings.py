from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
vector = embeddings.embed_query("Hello Ji kaisai ho aap sab?")

print("---------------------------------------------------------------------------------")
print(len(vector))
print("---------------------------------------------------------------------------------")
print(vector)