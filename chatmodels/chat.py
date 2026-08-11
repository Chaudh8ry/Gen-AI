from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-3.1-flash-lite")

reponse = model.invoke("self help book vs fictional books which one is better?")

# prints model details
# print(model)

print(reponse.content)