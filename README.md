# Real-time Information Chatbot

*   **`app/main.py`:** This file contains the Streamlit application for the chatbot interface.
*   **`app/api.py`:** This file defines the FastAPI application for the chatbot API endpoints.
*   **`app/services/chat_service.py`:** This file contains the ChatService class, which manages the chat logic and interacts with the Langchain agent.
*   **`ai_service/agents/search_agent.py`:** This file defines the Langchain agent and its tools.
*   **`ai_service/memories/chat_memory.py`**: This file sets up the type of memory used. Currently uses `ConversationBufferWindowMemory`.

## Prerequisites

Before running the application, ensure you have the following:

*   **Python 3.11:** The project is developed using Python 3.11.
*   **Poetry:** Poetry is used for managing dependencies. Install it from [https://python-poetry.org/](https://python-poetry.org/).
*   **OpenAI API Key:** You'll need an OpenAI API key to use the GPT language model. Obtain one from [https://openai.com/](https://openai.com/).
*   **Google Search API Key :** You'll need a Google Cloud account and set up the Custom Search API.

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

    Create a `.env` file in the project root and add your OpenAI API key and Google Search API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key
    GOOGLE_CSE_ID=your_google_cse_id
    ```

## Running the Application

### Running the FastAPI API

1.  **Start the Uvicorn server:**

    ```bash
    uvicorn app.api:app --reload
    ```

    This will launch the FastAPI application.
2.  **Access the API endpoints:**

    You can access the API endpoints using tools like `curl` or Postman.
    *   **Root Endpoint:** `http://127.0.0.1:8000/`
    *   **Query Endpoint (POST):** `http://127.0.0.1:8000/query/`
        *   Example `curl` command:

            ```bash
            curl -X POST -H "Content-Type: application/json" -d '{"text": "your query"}' http://127.0.0.1:8000/query/
            ```
    *   **History Endpoint (GET):** `http://127.0.0.1:8000/history/`
    *   **Clear History Endpoint (DELETE):** `http://127.0.0.1:8000/history/`
3.  **Access Swagger UI:**

    You can access the Swagger UI for the API at `http://127.0.0.1:8000/docs`.

### Running the Streamlit Application

1.  **Start the Streamlit application:**

    ```bash
    streamlit run app/main.py
    ```

    This will launch the Streamlit application in your default web browser.

## Usage

### Chat Interface (Streamlit)

*   The application will display a chat interface where you can type your queries.
*   The chatbot will process your queries and provide real-time responses, fetching information from the web if necessary.
*   The chatbot remembers previous interactions, allowing you to have a more natural conversation.
*   Clicking the "New Chat" button on the sidebar will clear the conversation history and start a new session.

### API Endpoints (FastAPI)

*   **/query/**: Sends a query to the chatbot and receives a response.
*   **/history/**: Retrieves the chat history.
*   **/history/**: Clears the chat history.