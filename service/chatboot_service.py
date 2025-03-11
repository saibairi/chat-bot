from fastapi import Request
from langchain_ollama import OllamaLLM

async def chatboot_service(request: Request)->str:
    # method-1: basic approch (1 min )
    llm = OllamaLLM(model="mistral")  # Use your preferred model (other llms llama3,mistral)
    response = llm.invoke(request)
    return response

    # # method-2 : Use Streaming for Faster UI Updates (37sec)
    # llm = OllamaLLM(model="mistral")
    # stream = llm.stream(request)
    # response = ""
    # for chunk in stream:
    #     response += chunk
    # return response

    # method- 3: Reduce Token Generation (32sec)
    # llm = OllamaLLM(model="mistral", max_tokens=200)  # Use your preferred model (other llms llama3,mistral)
    # response = llm.invoke(request)
    # return response