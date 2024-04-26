import requests
import streamlit as st


import requests


def get_openai_response(input_text):
    """
    Sends a POST request to the OpenAI server to get a response based on the input text.

    Args:
        input_text (str): The input text to be sent to the OpenAI server.

    Returns:
        str: The response content received from the OpenAI server.
    """
    response = requests.post('http://localhost:8000/essay/invoke',
                             json={'input': {'topic': input_text}})

    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post('http://localhost:8000/poem/invoke',
                             json={'input': {'topic': input_text}})

    return response.json()['output']

 # streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))