from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# createting the endpoint
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm=llm)

respone = model.invoke("Hello how are you?")
print(respone.content)