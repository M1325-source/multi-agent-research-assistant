
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings()
vector_memory = FAISS.from_texts([], embedding)
