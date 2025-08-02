from langchain_openai import ChatOpenAI

def get_gpt_response(prompt, openai_api_key):
    llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.5)
    return llm.invoke(prompt).content