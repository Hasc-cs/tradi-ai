import os
from dotenv import load_dotenv
#from langchain.chat_models import chatollama
#from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import init_chat_model


load_dotenv()

model_name = os.getenv("MODEL_NAME")
if not model_name:
    raise ValueError("MODEL_NAME is not set. Check your .env file.")

llm = init_chat_model(model=model_name, temperature=0.1)

messages = [
    ({"role": "system", "content": "You are a helpful assistant."})
]

while True:
    question = input("You: ").strip()

    if not question:
        continue
    if question.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    messages.append({
           "role": "user",
          "content": question
    })
    response = llm.invoke(messages)
    messages.append(({"role": "assistant", "content": response.content}))

    print("AI:", response.content)