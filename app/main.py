import streamlit as st
from app.services.chat_service import ChatService
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import AIMessage, HumanMessage

st.set_page_config(
    page_title="Real-time Information Chatbot", 
    page_icon="🤖",
    layout="centered"
)

# Header
st.title("Real-time Information Chatbot")
st.write("Ask me anything and I'll search the web for answers!")

# Initialize session state for chat history and service
if "chat_initialized" not in st.session_state:
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    st.session_state.chat_service = ChatService(memory=memory)
    st.session_state.chat_initialized = True

# New Chat button in sidebar
with st.sidebar:
    st.title("Options")
    if st.button("New Chat", key="new_chat"):
        st.session_state.chat_service.clear_memory()
        st.rerun()

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_service.get_chat_history():
        if isinstance(message, HumanMessage):
            st.markdown(
                f"""
                <div style="background-color: #e6f7ff; padding: 10px; 
                border-radius: 5px; margin-bottom: 10px; text-align: right;">
                <b>You:</b> {message.content}
                </div>
                """, 
                unsafe_allow_html=True
            )
        elif isinstance(message, AIMessage):
            st.markdown(
                f"""
                <div style="background-color: #f0f0f0; padding: 10px; 
                border-radius: 5px; margin-bottom: 10px; text-align: left;">
                <b>Bot:</b> {message.content}
                </div>
                """, 
                unsafe_allow_html=True
            )

# User input
with st.form(key="message_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_message_input")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        with st.spinner("Pondering..."):
            try:
                response = st.session_state.chat_service.agent.run(user_input)
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)[:100]}..."
                st.session_state.chat_service.memory.chat_memory.add_ai_message(error_msg)

        st.rerun()