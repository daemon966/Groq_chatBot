Groq Chat App

A chatbot application built using Streamlit, LangChain, and Groq for conversational AI. This app enables users to interact with a conversational agent powered by advanced language models, providing engaging and intelligent responses.
Features

    Interactive chatbot interface.
    Supports multiple language models (e.g., mixtral-8x7b-32768, llama2-70b-4096).
    Adjustable conversational memory length for context-aware responses.
    Tracks and displays chat history during a session.

Technologies Used

    Streamlit: For building the web-based user interface.
    LangChain: For managing conversational flows and memory.
    Groq: For leveraging AI models in conversations.
    Python Libraries:
        os
        dotenv
        langchain
        langchain_groq
        streamlit

Installation
Step 1: Clone the Repository

git clone https://github.com/your-repo-name/groq-chat-app.git
cd groq-chat-app

Step 2: Set Up Environment

    Create a .env file in the root directory:

touch .env

Add your Groq API Key to the .env file:

    GROQ_API_KEY=your_groq_api_key_here

Step 3: Install Dependencies

Make sure Python 3.9+ is installed. Then, run:

pip install -r requirements.txt

Usage
Run the Application

Start the Streamlit app by running:

streamlit run app.py

Open the App

After running the command, you will see a URL (e.g., http://localhost:8501). Open this in your browser.
App Workflow

    Select the language model from the sidebar.
    Adjust the conversational memory length using the slider.
    Enter your question in the text area and hit Enter.
    The chatbot will respond, and your conversation history will be displayed.

Directory Structure

groq-chat-app/
│
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment file for secrets
├── README.md               # Documentation

Requirements

    Python 3.9+
    Groq API key
    Supported AI models from Groq

Customizations

    Add or modify available models in the sidebar under:

model = st.sidebar.selectbox(
    'Choose a model',
    ['mixtral-8x7b-32768', 'llama2-70b-4096']
)

Adjust the default conversational memory length in:

    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

Contributing

Feel free to fork this repository, make updates, and submit pull requests. Contributions are welcome!
