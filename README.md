# 🧠 KAIRA

> **Enterprise Knowledge Graph & Hybrid GraphRAG Platform**

KAIRA is an AI-powered Enterprise Knowledge Platform that ingests both **structured** and **unstructured** enterprise data, constructs a **Knowledge Graph** in Neo4j, generates **vector embeddings** in ChromaDB, and provides intelligent question answering using a **Hybrid GraphRAG** retrieval pipeline.

---

# 🚀 Features

- 📄 Structured Data Ingestion
  - Excel (.xlsx, .xls)
  - CSV
  - JSON

- 📚 Unstructured Data Ingestion
  - PDF
  - DOCX
  - PPTX
  - TXT

- 🧠 AI-Powered Entity Extraction

- 🔗 Automatic Relationship Extraction

- 🌐 Enterprise Knowledge Graph Generation

- 📊 Neo4j Graph Database Integration

- 🔍 ChromaDB Vector Database

- 🤖 Hybrid GraphRAG Retrieval

- 💬 Natural Language Question Answering

- ⚡ FastAPI Backend

- 🎨 Streamlit Frontend

---

# 🏗️ Architecture

```
                   User

                     │

                     ▼

              Streamlit Frontend

                     │

                     ▼

               FastAPI Backend

          ┌──────────┴──────────┐

          ▼                     ▼

     Ingestion API         Query API

          │                     │

          ▼                     ▼

    Ingestion Agent      Retrieval Agent

          │                     │

          ▼                     ▼

   Structured Pipeline   Query Planning

          │                     │

          ▼                     ▼

 Unstructured Pipeline   Hybrid Retrieval

          │                     │

          └──────────┬──────────┘

                     ▼

              Knowledge Graph

                     │

        ┌────────────┴────────────┐

        ▼                         ▼

     Neo4j                   ChromaDB

        ▼                         ▼

     Graph Data              Vector Search
```

---

# 📂 Project Structure

```
KAIRA/

├── agents/
├── api/
├── config/
├── data/
├── embeddings/
├── graph/
├── ingestion/
├── llm/
├── models/
├── retrieval/
├── structured/
├── unstructured/
├── uploads/
├── utils/
├── vector_db/
├── tests/

├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

## Backend

- Python
- FastAPI

## Frontend

- Streamlit

## LLM

- Google Gemini

## Knowledge Graph

- Neo4j

## Vector Database

- ChromaDB

## Data Processing

- Pandas
- PyPDF
- python-docx

---

# 🔄 Workflow

## Ingestion Pipeline

```
Document

↓

File Detection

↓

File Classification

↓

Structured / Unstructured Pipeline

↓

Metadata Extraction

↓

Entity Extraction

↓

Relationship Extraction

↓

Knowledge Graph

↓

Neo4j

↓

Chunk Generation

↓

Embedding Generation

↓

ChromaDB
```

---

## Retrieval Pipeline

```
User Question

↓

Intent Classification

↓

Entity Identification

↓

Schema Loading

↓

Cypher Query Generation

↓

Graph Retrieval

↓

Vector Retrieval

↓

Hybrid Retrieval

↓

Context Building

↓

Answer Generation
```

---

# 📡 API Endpoints

## Health

```
GET /health
```

---

## Document Ingestion

```
POST /ingestion
```

Example

```json
{
    "file_path":"uploads/structured/document.xlsx"
}
```

---

## Query

```
POST /query
```

Example

```json
{
    "question":"What is Jane Doe's email?"
}
```

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

Example

```
GEMINI_API_KEY=YOUR_API_KEY

NEO4J_URI=bolt://localhost:7687

NEO4J_USERNAME=neo4j

NEO4J_PASSWORD=YOUR_PASSWORD
```

---

## Start FastAPI

```bash
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

```bash
streamlit run streamlit_app.py
```

---

# 📈 Current Status

- ✅ Structured Data Pipeline
- ✅ Unstructured Data Pipeline
- ✅ Knowledge Graph Generation
- ✅ Neo4j Integration
- ✅ ChromaDB Integration
- ✅ Embedding Generation
- ✅ Hybrid GraphRAG Retrieval
- ✅ FastAPI APIs
- ✅ Streamlit Frontend (In Progress)

---

# 🔮 Future Enhancements

- Cross-Encoder Re-ranking
- Multi-document Retrieval
- Duplicate Document Detection
- LLM Provider Abstraction (OpenAI, Gemini, Anthropic)
- Advanced Graph Analytics
- Role-Based Access Control
- Enterprise Authentication

---

# 👨‍💻 Author

**Durga Prasad Peddimeni**

B.Tech Computer Science & Engineering

Enterprise Knowledge Graph & Hybrid GraphRAG Platform

---

# ⭐ If you found this project useful, consider giving it a star!
