#import streamlit as st
#from google import genai

# Configure Gemini Client with API Key
#client = genai.Client(api_key="GOOGLE_API_KEY")

# Initialize Gemini Model
#chat = client.chats.create(model="gemini-2.0-flash")
#model = genai.GenerativeModel(name="gemini-pro")

# Streamlit UI
#st.title("🤖 AI Chatbot with Gemini")
#st.write("Powered by Google Gemini AI")

# Chat History
#if "messages" not in st.session_state:
    #st.session_state.messages = []

# Display Chat History
#for message in st.session_state.messages:
    #with st.chat_message(message["role"]):
        #st.markdown(message["content"])

# User Input
#user_input = st.chat_input("Type your message...")
#if user_input:
    # Display User Message
   # st.session_state.messages.append({"role": "user", "content": user_input})
   # with st.chat_message("user"):
       # st.markdown(user_input)

    # Get AI Response
   # response = chat.send_message_stream(user_input)
   # response = model.generate_content(user_input)
   # for chunk in response:
      # print(chunk.text, end="")
    #for message in chat._curated_history:
            # print(f'role - ', message.role, end=":")
            # print(message.parts[0].text)

    # Display AI Response
   # st.session_state.messages.append({"role": "assistant", "content": bot_reply})
   # with st.chat_message("assistant"):
       # st.markdown(bot_reply)

import streamlit as st
from google import genai

# Configure Gemini Client with API Key

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")
#client = genai.GenerativeModel("gemini-1.5-flash")  # Using Gemini Flash for faster responses

# Streamlit UI
st.title("🤖 AI Chatbot with Gemini")
st.write("Powered by Google Gemini AI")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")
if user_input:
    # Display User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI Response (Streaming)
    response = chat.send_message_stream(user_input)

    # Collect streamed response
    bot_reply = ""
    for chunk in response:
        if chunk.text:
            bot_reply += chunk.text + " "

    # Display AI Response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply.strip()})
    with st.chat_message("assistant"):
        st.markdown(bot_reply.strip())
