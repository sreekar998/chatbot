from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.chat_service import ChatService 
from langchain.memory import ConversationBufferMemory

app = FastAPI(title="Langchain Search Agent API")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chat_service = ChatService(memory=memory)

class Query(BaseModel):
    text: str

class Response(BaseModel):
    response: str

@app.get("/")
async def read_root():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the Langchain Search Agent API"}

@app.post("/query/", response_model=Response)
async def query_agent(query: Query):
    """
    Endpoint to query the Langchain search agent.
    """
    try:
        agent_response = chat_service.process_message(query.text) 
        return {"response": agent_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/")
async def get_history():
    """
    Endpoint to retrieve the chat history.
    """
    return {"history": chat_service.get_chat_history()} 

@app.delete("/history/")
async def clear_history():
    """
    Endpoint to clear the chat history.
    """
    chat_service.clear_memory() 
    return {"message": "Chat history cleared"}