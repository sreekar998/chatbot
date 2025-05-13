def format_chat_history(history):
    formatted_history = []
    for msg in history:
        if hasattr(msg, 'type') and msg.type == "human":
            formatted_history.append(f"**User:** {msg.content}")
        elif hasattr(msg, 'type') and msg.type == "ai":
            formatted_history.append(f"**Bot:** {msg.content}")
    return formatted_history