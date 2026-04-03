import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.3",
    temperature=0.2,
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_llm(system_prompt, user_input):
    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ])
    return response.content
