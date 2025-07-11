
# Multi-Agent Research Assistant 🧠📚

> AI-powered system that reads PDFs & scrapes websites to answer complex multi-document research queries using GPT-4, LangChain Agents, and OpenAI Functions.

## 🔧 Tech Stack
- Python 3.10+
- LangChain Agents
- GPT-4 / 3.5
- FAISS
- PyMuPDF
- Playwright
- Streamlit UI

📸 Screenshots

<img width="656" height="316" alt="image" src="https://github.com/user-attachments/assets/8b3e402c-ed6d-4b0a-97ce-84f530914712" />





<img width="656" height="345" alt="image" src="https://github.com/user-attachments/assets/2fcbcb9f-9d08-4640-8931-694510a66337" />








## 🚀 How to Run
1. Install requirements:
```bash
pip install -r requirements.txt
playwright install
```

2. Add your `OPENAI_API_KEY` in `.env` file.

3. Run the app:
```bash
streamlit run app.py
```

## 📂 Project Structure
- `agents/`: Agent logic (PDF, Web, Controller)
- `tools/`: Tools for scraping, loading PDFs, vector memory
- `data/`: Sample input PDFs and URL list

## 📌 Example Questions
- "Compare findings from sample1 and sample2 PDFs."
- "What are the main policies mentioned in these websites?"

---
Made with ❤️ using GPT + LangChain Agents
