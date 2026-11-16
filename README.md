# GenAI Document Assistant — RAG Application

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about a PDF document and receive context-based answers using Google Gemini.

## Live Demo

[Open GenAI Document Assistant](https://rag-application-k54d.onrender.com/)

## Project Overview

This application uses RAG to retrieve relevant information from a PDF document and provide answers using a Large Language Model (LLM).

Instead of answering entirely from the model's general knowledge, the application uses retrieved document content as context to generate more relevant answers.

## Features

- PDF document processing
- Text chunking with overlap
- Text embeddings using Google Gemini
- Vector storage using ChromaDB
- Similarity-based document retrieval
- Context-based answer generation
- Conversation history within the Streamlit session
- Fallback response when the answer is unavailable in the document

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- PyPDF
- Google GenAI SDK
- Python Dotenv

## RAG Architecture

1. Extract text from the PDF.
2. Split the extracted text into smaller chunks.
3. Generate embeddings for the text chunks.
4. Store embeddings and document metadata in ChromaDB.
5. Convert the user's question into an embedding.
6. Retrieve the three most relevant document chunks.
7. Pass the retrieved context to Gemini.
8. Generate an answer based on the provided document context.

## Project Structure

```text
RAG_Application/
│
├── documents/
│   └── GenAI_Rag_guide.pdf
│
├── vector_db/
│   └── ChromaDB data
│
├── app.py
├── read_pdf.py
├── chunk_text.py
├── embeddings.py
├── vector_store.py
├── search_documents.py
├── generate_answer.py
├── main.py
│
├── requirements.txt
└── .gitignore
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AbhiGlitch/RAG_Application.git
cd RAG_Application
```

### 2. Create a virtual environment

```bash
python -m venv myvenv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
myvenv\Scripts\Activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
streamlit run app.py
```

## Git Ignore

The `.gitignore` file prevents unnecessary and sensitive files from being uploaded to GitHub.

Excluded files:
- `.env` – API keys and environment variables
- `myvenv/` – Python virtual environment
- `__pycache__/` – Python cache files
- `*.pyc` – Compiled Python files

## Deployment

The application is deployed using Render.

- Source code: GitHub
- Hosting: Render
- LLM: Google Gemini

## Example

**Question:**

What is RAG?

**Answer:**

RAG stands for Retrieval-Augmented Generation. It combines information retrieval with language generation to provide answers using relevant information from a knowledge source.

## Current Limitations

- Follow-up questions may not retrieve the correct context when they depend on earlier questions.
- Answers are limited to the information available in the provided PDF.

## Future Improvements

- Query contextualization for better follow-up question retrieval.
- Support for multiple PDF documents.
- FastAPI-based backend integration.
- Improved retrieval and evaluation.
