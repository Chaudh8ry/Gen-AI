from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


print("Select Your AI's Mood")
print("press 1 for ANGRY Mode")
print("press 2 for FUNNY Mode")
print("press 3 for SAD Mode")

choice = int(input("Tell me Your Response: "))

if choice == 1:
    mode = "You are a ANGRY AI agent. You respond Aggresively and Impatiently."
elif choice == 2:
    mode = "You are a FUNNY AI agen. You respond with Humour and Jokes."
elif choice == 3:
    mode = "You are a SAD AI agent. You resposne in very sadistic tone."

chatHistory = [
    SystemMessage(content=mode)
]

print("-----------Type 0 to exit-------------")
while True:
    prompt = input("You: ")
    chatHistory.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(chatHistory)
    chatHistory.append(AIMessage(content=response.text))
    print("Bot: ",response.text)

print(chatHistory)