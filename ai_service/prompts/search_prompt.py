from langchain.prompts import PromptTemplate
from langchain_core.messages import SystemMessage

# Add a more conversational prompt that encourages the agent to remember previous interactions
GENERIC_SEARCH_PROMPT_TEMPLATE = """You are a helpful assistant that answers user questions using up-to-date information from web search results.
Use the provided search results to answer the user's question. If the search results are not relevant or do not contain the answer, please say so.

Remember our conversation history to provide a coherent and contextual response:
{chat_history}

Search Results:
{search_results}

User Query: {input}

Answer:
"""

GENERIC_SEARCH_PROMPT = PromptTemplate(
    input_variables=["search_results", "input", "chat_history"],
    template=GENERIC_SEARCH_PROMPT_TEMPLATE,
)

# Define a system message for the agent to better handle conversation
SYSTEM_MESSAGE = SystemMessage(
    content="""You are a conversational assistant that remembers the conversation history and provides helpful answers. 
    When you don't know something or need more information, use web search to find relevant information."""
)