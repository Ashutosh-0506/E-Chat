# utils/build_vector_store.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from pathlib import Path

import os

# 🧠 Load content
handbook_text = Path("data/handbook_cleaned_FULL.txt").read_text(encoding="utf-8")
direction_text = Path("data/direction_final.txt").read_text(encoding="utf-8")

# 🔪 Chunking config
splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=150,
    length_function=len,
)

# 📚 Split text into structured chunks with metadata
def chunk_with_metadata(text, source_label):
    sections = text.split("## SECTION:")
    documents = []

    for section in sections:
        if not section.strip():
            continue
        header, *content = section.strip().split("\n", 1)
        body = content[0] if content else ""
        chunks = splitter.create_documents([body])
        for chunk in chunks:
            chunk.metadata = {
                "source": source_label,
                "section": header.strip()
            }
        documents.extend(chunks)
    return documents

# 🔧 Apply chunking
handbook_docs = chunk_with_metadata(handbook_text, "handbook")
direction_docs = chunk_with_metadata(direction_text, "direction")

all_docs = handbook_docs + direction_docs
print(f"✅ Total chunks: {len(all_docs)}")

# 🧠 SentenceTransformer embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 🧱 FAISS vector store
vectordb = FAISS.from_documents(all_docs, embedding_model)
vectordb.save_local("data/faiss_index")

print("✅ FAISS index saved to: data/faiss_index/")
