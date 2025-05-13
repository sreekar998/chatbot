from langchain.memory import ConversationBufferWindowMemory

def load_chat_memory(k: int = 5):
    """Loads a chat history buffer with a limited window."""
    return ConversationBufferWindowMemory(k=k, memory_key="chat_history", return_messages=True)