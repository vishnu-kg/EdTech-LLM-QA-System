# qa_chain.py
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
import logging
from langchain import OpenAI

class QAChain:
    def __init__(self, api_key: str):
        self.llm = model=OpenAI(temperature=0.9, max_tokens=500)
        self.prompt_template = """
        Given the following context and a question, generate an answer based on this context only.
        In the answer try to provide as much text as possible from the "response" section in the source document context without making much changes.
        If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

        CONTEXT: {context}

        QUESTION: {question}
        """
        self.prompt = PromptTemplate(template=self.prompt_template, input_variables=["context", "question"])

    def create_chain(self, retriever):
        """Create the retrieval-based QA chain"""
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            input_key="query",
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )
