import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

openai_api_key = os.environ["OPENAI_API_KEY"]

def get_openai_response(question):
    llm = OpenAI(openai_api_key=openai_api_key,temperature=0.6)
    response = llm.invoke(question)
    return response

st.set_page_config(page_title="Q&A Bot", page_icon="🤖", layout="wide")

st.header("Q&A Bot")

question = st.text_input("Question")
if st.button("Submit"):
    st.write("Generating answer...")
    st.write("Aka's Bot: ")
    response = get_openai_response(question)
    st.write(response)

