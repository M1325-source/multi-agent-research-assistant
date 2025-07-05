
from tools.pdf_loader import extract_text_from_pdf
from tools.memory_store import vector_memory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

class DocumentAgent:
    def run(self, query):
        text = extract_text_from_pdf("data/sample1.pdf") + extract_text_from_pdf("data/sample2.pdf")
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = splitter.split_text(text)

        vector_memory.add_texts(docs)
        results = vector_memory.similarity_search(query, k=5)
        context = " ".join([res.page_content for res in results])
        return llm.predict(f"Context: {context}\n\nQuestion: {query}")

document_agent = DocumentAgent()
