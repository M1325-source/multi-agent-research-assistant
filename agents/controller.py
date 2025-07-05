
from langchain.agents import initialize_agent, Tool
from agents.document_agent import document_agent
from agents.web_agent import web_agent
from tools.memory_store import vector_memory

tools = [
    Tool(name="PDF Reader", func=document_agent.run, description="Reads and analyzes PDF documents."),
    Tool(name="Web Scraper", func=web_agent.run, description="Scrapes and analyzes web content."),
]

agent = initialize_agent(
    tools=tools,
    llm=document_agent.llm,
    agent="openai-functions",
    memory=vector_memory,
    verbose=True
)

def ask_question(question: str):
    return agent.run(question)
