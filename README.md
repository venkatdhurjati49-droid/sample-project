# 🧠 AI Document Processor (Google ADK Assessment)

This project implements an **AI-powered document question-answering system** using the **Google Generative AI (Gemini)** SDK.  
It ingests PDF files, builds semantic embeddings, and answers questions with structured **JSON output** including **page-level references**.

---

## 🚀 Features
- 📄 PDF ingestion and text extraction (PyMuPDF)
- 🧩 Chunking and FAISS-based semantic search
- 🤖 Gemini-powered JSON answers with confidence and citations
- 🧱 Modular architecture (ingest / index / agent)
- 💬 CLI-based query interface
- 🌈 Optional FastAPI REST API version

---

## 🗂️ Project Structure

```
ai-pdf-adk-demo/
│
├── ingest/
│   ├── pdf_loader.py          # PDF → text
│   └── chunker.py             # Chunking into passages
│
├── index/
│   ├── vector_store.py        # Embeddings + FAISS index
│   └── build_index.py
│
├── agent/
│   ├── llm.py                 # Gemini client
│   ├── qa_agent.py            # Retrieval + reasoning logic
│   └── schema.py              # JSON response schema
│
├── demo_pdfs/                 # Sample PDFs
├── cli.py                     # CLI entry point
├── .env                       # Contains GOOGLE_API_KEY
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone & create environment
```bash
git clone https://github.com/venkatdhurjati49-droid/sample-project
cd ai-pdf-adk-demo

python -m venv .venv
source .venv/bin/activate     # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 2️⃣ Add your API key
Create a file named `.env` in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 3️⃣ Add PDFs
Place your documents in:
```
demo_pdfs/
```

### 4️⃣ Run the app
```bash
python cli.py
```

You’ll see:
```
Loading PDFs...
✅ Embeddings created
PDFs indexed. Ask a question (or 'exit'):
```

Then ask:
```
> What is dice rule?
```

Example output:
```json
{
  "query": "what is dice rule",
  "answers": [
    {
      "answer": "The dice game rules involve throwing five dice...",
      "confidence": 1.0,
      "references": [
        {
          "pdf": "Developer Exercise Dice Game.pdf",
          "page": 1,
          "snippet": "If there are any 3’s, all the 3’s are taken off..."
        }
      ]
    }
  ]
}
```

---

## ⚡ Optional: Run API Server
```bash
uvicorn app:app --reload --port 8000
```

Then query:
```
POST http://localhost:8000/ask?query=What is dice rule?
```

---

## 🧩 JSON Response Schema
```json
{
  "query": "string",
  "answers": [
    {
      "answer": "string",
      "confidence": 0.0,
      "references": [
        {"pdf": "string", "page": 1, "snippet": "string"}
      ]
    }
  ]
}
```

---

## 📽️ Demo Video

🎥 ((https://www.loom.com/share/e12dd8866c3d46749a5988efa1ddf9f7 ])


---

## 🏗️ Tech Stack
- **Language:** Python 3.12
- **LLM:** Gemini 2.5 Flash (`google-genai`)
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Index:** FAISS
- **PDF Parser:** PyMuPDF
- **Interface:** CLI (and optional FastAPI API)

