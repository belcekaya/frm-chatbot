# set up the environment
import os
import sys
import pinecone
from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain

# Replicate API token
os.environ['REPLICATE_API_TOKEN'] = "r8_9KKJLO5qNQAG8nV7Ov176gRIga0Qxq710aez5"

# Initialize Pinecone
pinecone.init(api_key='3c595725-d56e-48fb-9b0c-779c20effd17', environment='gcp-starter')