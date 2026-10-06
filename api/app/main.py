import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model_name = os.getenv("MODEL_NAME")
if not model_name:
    raise ValueError("MODEL_NAME is not set. Check your .env file.")

llm = init_chat_model(model=model_name, temperature=0.1)

messages = [
    SystemMessage(content="You are a helpful Corvit AI Assistant!")
]

while True:
    question = input("You: ").strip()

    if not question:
        continue
    if question.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=question))
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("AI:", response.content)