import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType
from ai_service.memories.chat_memory import load_chat_memory
from dotenv import load_dotenv

load_dotenv()

def create_search_agent(memory):
    """Creates a Langchain agent that uses Google Search."""
    llm = ChatOpenAI(
        model_name="gpt-4-turbo-preview",
        temperature=0.2,
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )
    search = GoogleSearchAPIWrapper()
    tools = [
        Tool(
            name="Google Search",
            func=search.run,
            description="Useful for when you need to get up-to-date information about the world using Google Search."
        )
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3,
    )
    return agent

if __name__ == "__main__":
    memory = load_chat_memory(k=5)  # Use the function to get the memory object, limiting to 5 interactions
    agent = create_search_agent(memory=memory)