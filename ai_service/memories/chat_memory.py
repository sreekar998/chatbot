from langchain.memory import ConversationBufferMemory

def load_chat_memory():
    """Loads a simple in-memory chat history buffer."""
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
