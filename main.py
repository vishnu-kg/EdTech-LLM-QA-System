import sys
import os
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

from src.vector_db import VectorDB
from src.qa_chain import QAChain
import logging
from dotenv import load_dotenv

load_dotenv()  # This will load variables from the .env file
api_key = os.getenv("OPENAI_API_KEY")


# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize VectorDB and QAChain with required configurations
vector_db = VectorDB(file_path="faiss_index")
qa_chain = QAChain(api_key=api_key)

st.title("EDTECH Q&A 🌱")

btn = st.button("Create Knowledgebase")

if btn:
    try:
        vector_db.create('codebasics_faqs.csv')
    except Exception as e:
        st.error(f"Error creating knowledgebase: {e}")
        logging.error(f"Error creating knowledgebase: {e}")

question = st.text_input("Question: ")

if question:
    try:
        vectordb = vector_db.load()
        retriever = vectordb.as_retriever(score_threshold=0.7)
        chain = qa_chain.create_chain(retriever)
        response = chain(question)
        
        st.header("Answer")
        st.write(response["result"])
    except Exception as e:
        st.error(f"Error processing the question: {e}")
        logging.error(f"Error processing the question: {e}")
