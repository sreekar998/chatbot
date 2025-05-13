import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

def create_search_agent(memory: ConversationBufferMemory):
    """Creates a Langchain agent for fetching and answering queries using Google web search."""
    llm = ChatOpenAI(
        model_name="gpt-4-turbo-preview", 
        temperature=0.2, 
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )
    
    # Initialize Google Search
    search = GoogleSearchAPIWrapper()
        
    tools = [
        Tool(
            name="Google Search",
            func=search.run,
            description="Useful for when you need to get up-to-date information about the world using Google Search.",
        )
    ]

    # Initialize the agent with memory
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