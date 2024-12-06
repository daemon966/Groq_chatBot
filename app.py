import streamlit as st
import os
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')  # Use `getenv` to handle missing key gracefully

def main():
    st.title("Groq Chat App")

    # Sidebar for model selection and settings
    st.sidebar.title('Select an LLM')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider(
        'Conversational memory length:', 1, 10, value=5
    )

    # Initialize memory for conversation
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Input for user questions
    user_question = st.text_area("Ask a question:")

    # Manage chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        memory.save_context(
            {'input': message['human']},
            {'output': message['AI']}
        )

    # Initialize the Groq chat object
    if not groq_api_key:
        st.error("GROQ_API_KEY is not set in the environment.")
        return

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )

    # Set up the conversation chain
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    # Handle user input and generate responses
    if user_question:
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response['response'])

if __name__ == "__main__":
    main()
