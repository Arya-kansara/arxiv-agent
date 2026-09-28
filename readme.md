# arXiv Research Assistant using LangGraph + RAG

## Project Overview

This project is an AI-powered research assistant that can understand arXiv papers using Retrieval-Augmented Generation (RAG).

The user can provide:

* arXiv ID (e.g. `1706.03762`)
* arXiv URL
* Topic (e.g. `Recent RAG papers`)

The agent retrieves the paper, downloads the PDF, extracts the text, creates semantic embeddings, stores them in FAISS, generates an Executive Briefing, and answers questions using the paper's content.

## Architecture

State Graph Flow:

`Understand → Retrieve → Download → Parse → Chunk → Embed → Brief → QA`

### Shared State (AgentState)

* query
* is_topic_search
* paper
* pdf_path
* full_text
* chunks
* vectorstore
* brief
* messages

## Tech Stack

* LangGraph
* Python
* Sentence Transformers
* FAISS
* PyMuPDF
* arXiv API
* Ollama (Gemma 3 1B)

## Setup

### Clone

```bash
git clone <your-repository-url>
cd arxiv-agent
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama model

```bash
ollama pull gemma3:1b
```

### Run

```bash
python app.py
```

## Example Run

### Input

```text
1706.03762
```

### Executive Briefing Output

* Why this paper matters
* Problem Statement
* Method / Approach
* Key Results
* Limitations
* Suggested Follow-up Questions

### Sample QA

**Q:** What is multi-head attention?

**A:** Multi-head attention runs several attention heads in parallel, allowing the Transformer to learn different relationships between tokens simultaneously.

---

**Q:** Title of the paper?

**A:** Attention Is All You Need

---

**Q:** Who won the 2023 Cricket World Cup?

**A:** The retrieved context does not contain the answer.

## Design Decisions & Tradeoffs

### Why LangGraph?

Instead of writing one long script, I separated the workflow into independent nodes. Every node has one responsibility and shares the same AgentState, making the pipeline easier to maintain and extend.

### Why Sentence Transformers + FAISS?

Sentence Transformers generate semantic embeddings, while FAISS performs fast similarity search over the paper chunks. This allows the system to retrieve only the most relevant context before sending it to the LLM.

### Why Ollama?

I replaced cloud APIs with Ollama to avoid rate limits and keep the project fully runnable locally using free tools.

### Known Limitations

* Figure and table extraction from PDFs can introduce noisy text.
* Retrieval quality depends on chunking and embedding quality.
* Small local LLMs may produce shorter or less detailed answers than larger cloud models.

### Future Improvements

* Hybrid search (BM25 + Vector Search)
* Better PDF layout extraction
* Citation-aware answers
* Multi-paper comparison
