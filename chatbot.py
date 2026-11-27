import torch

import os
from dotenv import load_dotenv
load_dotenv()

# Streamlit page setup
import streamlit as st
st.title("Generative AI Chatbot")

# Initialize chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


from langchain_groq import ChatGroq
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
# Input box

user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_prompt
    })

    response = llm.invoke([
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        *st.session_state.chat_history
    ])

    assistant_response = response.content

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    with st.chat_message("assistant"):
        st.markdown(assistant_response)