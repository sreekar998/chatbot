# Real-time Information Chatbot

## Overview

This project is a real-time information chatbot built using Streamlit, Langchain, and a language model (like GPT). The chatbot is designed to fetch and answer user queries using tools like Google Search, providing up-to-date information.  It also incorporates conversation memory, allowing it to maintain context and provide more coherent responses across multiple interactions.

## Features

* **Real-time Information Retrieval:** The chatbot can fetch information from the web using tools like Google Search.
* **Conversational Memory:** The chatbot remembers previous interactions, providing context for more natural conversations.
* **Streamlit Interface:** The chatbot has a user-friendly interface built with Streamlit, allowing for easy interaction.
* **Langchain Integration:** Langchain is used to manage the agent, tools, and memory, providing a robust framework for building the chatbot.

## Technical Architecture

The project consists of the following main components:

* **`app/main.py`:** This is the main application file, responsible for:
    * Setting up the Streamlit UI.
    * Initializing the Langchain agent and memory.
    * Handling user input and displaying chatbot responses.
* **`app/services/chat_service.py`:** This file defines the `ChatService` class, which:
    * Manages the Langchain agent.
    * Processes user messages.
    * Retrieves the chat history.
* **`ai_service/agents/search_agent.py`:** This file defines the Langchain agent and its tools (e.g., Google Search).
* **`ai_service/memories/chat_memory.py`**: This file sets up the type of memory used. Currently uses `ConversationBufferMemory`.

## Prerequisites

Before running the application, ensure you have the following:

* **Python 3.11:** The project is developed using Python 3.11.
* **Poetry:** Poetry is used for managing dependencies.  Install it from [https://python-poetry.org/](https://python-poetry.org/).
* **OpenAI API Key:** You'll need an OpenAI API key to use the GPT language model.  Obtain one from [https://openai.com/](https://openai.com/).
* **Google Search API Key (Optional):** If you want to use Google Search, you'll need a Google Cloud account and set up the Custom Search API.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd chatbot
    ```

2.  **Set up the Environment:**
    Poetry will automatically create a virtual environment.

3.  **Install Dependencies:**
    ```bash
    poetry install
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the project root and add your API keys:
    ```
    OPENAI_API_KEY=<your_openai_api_key>
    #GOOGLE_API_KEY=<your_google_api_key> # Optional
    #GOOGLE_CSE_ID=<your_google_cse_id>     # Optional
    ```
    Replace the placeholder values with your actual API keys.  The Google Search API keys are optional if you don't intend to use the search functionality.

## Running the Application

To start the chatbot, run the following command:

```bash
streamlit run app/main.py
This will launch the Streamlit application in your default web browser.UsageChat Interface: The application will display a chat interface where you can type your queries.Real-time Responses: The chatbot will process your queries and provide real-time responses, fetching information from the web if necessary.Conversation History: The chatbot remembers previous interactions, allowing you to have a more natural conversation.New Chat: Clicking the "New Chat" button on the sidebar will clear the conversation history and start a new session.