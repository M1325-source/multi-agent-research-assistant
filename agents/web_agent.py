
from tools.web_scraper import scrape_url
from tools.memory_store import vector_memory
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter

llm = OpenAI(temperature=0)

class WebAgent:
    def run(self, query):
        with open("data/urls.txt", "r") as f:
            urls = f.readlines()
        content = ""
        for url in urls:
            content += scrape_url(url.strip())[:2000]  # limit characters

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = splitter.split_text(content)

        vector_memory.add_texts(docs)
        results = vector_memory.similarity_search(query, k=5)
        context = " ".join([res.page_content for res in results])
        return llm.predict(f"Context: {context}\n\nQuestion: {query}")

web_agent = WebAgent()
