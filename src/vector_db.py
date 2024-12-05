
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
import os
import logging

class VectorDB:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.instructor_embeddings = OpenAIEmbeddings()
        logging.info(f"VectorDB initialized with file path: {self.file_path}")

    def create(self, csv_file: str):
        """Create a vector database from the given CSV file"""
        loader = CSVLoader(file_path=csv_file, source_column="prompt")
        data = loader.load()

        # Create a FAISS instance for vector database
        vectordb = FAISS.from_documents(documents=data, embedding=self.instructor_embeddings)

        # Save the vector database locally
        vectordb.save_local(self.file_path)
        logging.info(f"Vector database created and saved at {self.file_path}")

    # def load(self):
    #     """Load the vector database from the saved file"""
    #     if not os.path.exists(self.file_path):
    #         raise FileNotFoundError(f"Vector database file {self.file_path} not found!")
        
    #     vectordb = FAISS.load_local(self.file_path, self.instructor_embeddings)
    #     logging.info(f"Vector database loaded from {self.file_path}")
    #     return vectordb

    def load(self):
        """Load the vector database from the saved file"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Vector database file {self.file_path} not found!")
        
        # Enable dangerous deserialization for trusted files
        vectordb = FAISS.load_local(self.file_path, self.instructor_embeddings, allow_dangerous_deserialization=True)
        logging.info(f"Vector database loaded from {self.file_path}")
        return vectordb

