from ai_service.agents.search_agent import create_search_agent
from langchain_core.messages import AIMessage, HumanMessage

class ChatService:
    def __init__(self, memory):
        self.memory = memory
        self.agent = create_search_agent(memory=self.memory)

    def process_message(self, user_message):
        """Process a user message and get response from agent."""
        try:
            response = self.agent.run(user_message)
            return response
        except Exception as e:
            return f"Error processing message: {str(e)}"
    
    def get_chat_history(self):
        """Return the messages from memory."""
        return self.memory.chat_memory.messages
    
    def clear_memory(self):
        """Clear the memory when starting a new chat."""
        self.memory.clear()